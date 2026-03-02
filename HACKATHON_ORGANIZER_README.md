# Hackathon Organizer Guide

Instructions for preparing and running the Fever design hackathon.

## Pre-hackathon checklist

### 1. Grant access to the fever_replica repo

The repo `emilianoechevarriafever/fever_replica` is **private**. Participants need explicit access to fork it. You have two options:

**Option A -- Add participants as collaborators** (preferred for fork + GitHub Pages workflow):
```bash
# Add one participant at a time:
gh api repos/emilianoechevarriafever/fever_replica/collaborators/GITHUB_USERNAME -X PUT -f permission=read
```
Once added, they can fork the repo and deploy via GitHub Pages.

**Option B -- Share the project files via Google Drive / USB / zip**:
- Zip the `fever_replica` folder (or upload to a shared Google Drive).
- Tell participants: "Download the `fever_replica` folder from [Drive link] and open it in Cursor."
- In this scenario, participants will work locally (localhost) and can optionally create their own GitHub repo during setup.

**Note**: If you share the files via Drive, also include the setup prompt (`HACKATHON_SETUP_PROMPT.md`) in the same folder.

### 2. Prepare the Design System Toolkit for sharing

The repo `Feverup/AI-Product-Design-Toolkit` is **private**. Participants outside the Feverup GitHub org cannot clone it. You have two options:

**Option A -- Add participants to the Feverup org** (preferred if they are Fever employees):
- Go to https://github.com/orgs/Feverup/people and invite them.
- They will be able to clone the toolkit automatically during setup.

**Option B -- Share via Google Drive / USB / zip**:
- Clone the toolkit locally: `git clone https://github.com/Feverup/AI-Product-Design-Toolkit.git`
- Zip the folder (or upload to a shared Google Drive).
- Tell participants: "Download the `AI-Product-Design-Toolkit` folder from [Drive link] and rename it to `design-system-toolkit` inside your project root."

### 3. Confirm participants have Cursor installed

- Cursor version: latest stable (any version with Agent mode).
- Model: Auto or Claude 4.6 Opus High recommended.
- No specific extensions required (the project is plain HTML/CSS/JS).

### 4. Distribute the setup prompt

Share the file `HACKATHON_SETUP_PROMPT.md` with all participants via Slack, email, or the shared Drive. They paste its entire content into a new Cursor Agent chat.

### 5. (Optional) Figma seats

If participants need to reference Figma designs:
- They need a Figma **Dev** or **Designer** seat on the Fever workspace.
- The setup prompt will configure the Figma MCP connection automatically.
- If they do not have a seat, they can still work -- they just cannot pull designs from Figma directly.

---

## Access matrix

This table shows what works depending on what access a participant has:

| Capability | GitHub CLI + repo collaborator | Feverup org member | Figma seat | None of the above |
|---|---|---|---|---|
| **Fork fever_replica** | Yes (if added as collaborator) | Yes (if added as collaborator) | -- | No (needs Drive/zip copy) |
| **GitHub Pages deploy** | Yes (on their fork or own repo) | Yes | -- | No (localhost only) |
| **Clone Design Toolkit** | Only if Feverup org | Yes | -- | No (needs Drive/zip copy) |
| **Figma MCP** | -- | -- | Yes | No (manual screenshots) |
| **Local development** | Yes | Yes | Yes | Yes (always works) |
| **Cursor Rule (design system)** | Yes | Yes | Yes | Yes (embedded in prompt) |

**Minimum viable setup**: A participant with NO GitHub, NO Figma, and NO collaborator access can still participate. They will:
1. Get both the `fever_replica` files and the `design-system-toolkit` from the shared Drive/zip.
2. Work on localhost.
3. Optionally create their own private GitHub repo during setup (if they have `gh`).
4. Have full design system context via the Cursor Rule (tokens are inlined).

---

## Troubleshooting FAQ

### "GitHub Pages shows 404"

- Pages takes 1-2 minutes to deploy after enabling. Wait and refresh.
- Verify Pages is enabled: `gh api repos/OWNER/fever_replica/pages --jq '.html_url'`.
- Verify the source branch is `main`: `gh api repos/OWNER/fever_replica/pages --jq '.source'`.
- If it says `build_type: workflow`, switch to legacy: `gh api repos/OWNER/fever_replica/pages -X PUT -f build_type=legacy -f source[branch]=main -f source[path]=/`.

### "Permission denied forking fever_replica" / "Could not resolve to a Repository"

The `fever_replica` repo is private. The participant has not been added as a collaborator. Two options:
- Add them: `gh api repos/emilianoechevarriafever/fever_replica/collaborators/THEIR_USERNAME -X PUT -f permission=read`
- Give them the project files via the shared Drive/zip. The setup prompt will guide them to create their own repo.

### "gh: command not found"

The participant does not have GitHub CLI installed. Two options:
- Install it: `brew install gh` (macOS) or see https://cli.github.com/.
- Skip it and work with HTTPS clone + localhost. The setup prompt handles this automatically.

### "Figma MCP is not connecting"

- Verify `.cursor/mcp.json` exists in the project root with the correct content.
- Restart Cursor after creating the file.
- The participant must approve the MCP connection when Cursor prompts them.
- If the participant does not have a Figma seat, MCP will not work regardless of the config.

### "Permission denied cloning AI-Product-Design-Toolkit"

The repo is private. The participant needs either:
- Feverup org membership on GitHub, or
- A local copy from the shared Drive folder.

### "My changes are not showing on GitHub Pages"

After editing, the participant must commit and push:
```bash
git add -A && git commit -m "description" && git push origin main
```
Pages re-deploys automatically from `main`. Wait ~60 seconds.

### "I accidentally broke the site"

Since every participant works on their own fork, they can always reset:
```bash
git checkout main
git reset --hard origin/main
```
Or re-fork from the original repo.

---

## What participants get after setup

| Component | Location |
|-----------|----------|
| Fever website clone | Project root (`index.html`, `plan.html`, etc.) |
| Design system tokens + docs | `design-system-toolkit/` folder |
| AI context (Cursor Rule) | `.cursor/rules/fever-hackathon.mdc` |
| Figma connection (optional) | `.cursor/mcp.json` |
| Live deployment (optional) | `https://USERNAME.github.io/fever_replica/` |
| Local server (fallback) | `http://localhost:8000` |
