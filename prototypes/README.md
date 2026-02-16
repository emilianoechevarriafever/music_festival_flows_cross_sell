# Prototypes isolation and deploy

This folder contains two fully separated static prototypes:

- `prototypes/queen/`
- `prototypes/coldplay/`

Each prototype has:

- its own `index.html`
- its own `img/` folder copy
- independent internal links (no dependency on `/home`)

## Vercel setup (one-time)

Create **2 Vercel projects** from the same repository:

1. Project name example: `prototype-queen`
   - Root Directory: `prototypes/queen`
2. Project name example: `prototype-coldplay`
   - Root Directory: `prototypes/coldplay`

Recommended settings:

- Framework Preset: `Other`
- Build Command: empty
- Output Directory: empty

After this, each prototype deploys to a different URL and can evolve independently.
