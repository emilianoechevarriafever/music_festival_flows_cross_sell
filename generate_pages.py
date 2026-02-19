#!/usr/bin/env python3
import os

FOOTER_HTML = '''  <div class="footer">
    <div class="footer-cols">
      <div class="footer-col">
        <h5>About Fever</h5>
        <ul>
          <li><a href="press.html">Press</a></li>
          <li><a href="careers.html">Careers</a></li>
          <li><a href="gift-cards.html">Gift Cards</a></li>
          <li><a href="help-center.html">Help Center</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Partner with us</h5>
        <ul>
          <li><a href="fever-zone.html">Fever Zone</a></li>
          <li><a href="list-event.html">List your event</a></li>
          <li><a href="affiliate.html">Affiliate Program</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-cols">
      <div class="footer-col">
        <h5>Follow us</h5>
        <ul>
          <li><a href="#">Instagram</a></li>
          <li><a href="#">TikTok</a></li>
          <li><a href="#">Twitter / X</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Support 24/7</h5>
        <ul>
          <li><a href="contact.html">Contact us</a></li>
          <li><a href="faqs.html">FAQs</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <a href="terms.html">Terms of Use</a> | <a href="privacy.html">Privacy Policy</a> | <a href="cookies.html">Cookie Policy</a>
      <div style="margin-top:8px;text-align:right;">&copy;2026 &ndash; Fever</div>
    </div>
  </div>'''

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Fever</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
    :root {{
      --color-primary: #0079ca;
      --color-primary-weak: #E6F4FF;
      --color-text-main: #031419;
      --color-text-secondary: #536b75;
      --color-text-subtle: #536b75;
      --color-border: #E6EAEE;
      --color-bg-neutral: #F5F7F9;
      --font: 'Montserrat', sans-serif;
    }}
    html {{ scroll-behavior: smooth; -webkit-tap-highlight-color: transparent; }}
    body {{ font-family: var(--font); background: #fff; color: var(--color-text-main); max-width: 480px; margin: 0 auto; min-height: 100vh; display: flex; flex-direction: column; }}
    .nav {{ position: sticky; top: 0; z-index: 100; background: #fff; display: flex; align-items: center; justify-content: space-between; padding: 12px 16px; border-bottom: 1px solid var(--color-border); }}
    .nav-logo {{ font-family: var(--font); font-weight: 800; font-size: 22px; color: var(--color-text-main); text-decoration: none; letter-spacing: -0.5px; }}
    .nav-back {{ display: flex; align-items: center; gap: 6px; text-decoration: none; color: var(--color-text-main); font-size: 14px; font-weight: 600; }}
    .nav-back svg {{ width: 20px; height: 20px; }}
    .page-hero {{ background: var(--color-bg-neutral); padding: 40px 16px 32px; }}
    .page-hero h1 {{ font-size: 28px; font-weight: 800; line-height: 36px; color: var(--color-text-main); margin-bottom: 8px; }}
    .page-hero p {{ font-size: 15px; line-height: 24px; color: var(--color-text-secondary); }}
    .page-content {{ flex: 1; padding: 24px 16px 40px; }}
    .page-content h2 {{ font-size: 20px; font-weight: 700; margin-bottom: 12px; margin-top: 28px; color: var(--color-text-main); }}
    .page-content h2:first-child {{ margin-top: 0; }}
    .page-content h3 {{ font-size: 16px; font-weight: 700; margin-bottom: 8px; margin-top: 20px; color: var(--color-text-main); }}
    .page-content p {{ font-size: 14px; line-height: 22px; color: var(--color-text-secondary); margin-bottom: 14px; }}
    .page-content ul {{ list-style: disc; padding-left: 20px; margin-bottom: 14px; }}
    .page-content ul li {{ font-size: 14px; line-height: 24px; color: var(--color-text-secondary); }}
    .page-content a {{ color: var(--color-primary); text-decoration: underline; }}
    .page-content .card {{ background: var(--color-bg-neutral); border-radius: 12px; padding: 20px; margin-bottom: 16px; }}
    .page-content .card h3 {{ margin-top: 0; }}
    .page-content .card p:last-child {{ margin-bottom: 0; }}
    .page-content .btn {{ display: inline-block; background: var(--color-primary); color: #fff; font-family: var(--font); font-size: 14px; font-weight: 600; padding: 12px 24px; border-radius: 100px; text-decoration: none; margin-top: 8px; transition: opacity 0.15s; }}
    .page-content .btn:hover {{ opacity: 0.9; }}
    .page-content .stat-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 16px 0; }}
    .page-content .stat {{ text-align: center; background: var(--color-bg-neutral); border-radius: 12px; padding: 20px 12px; }}
    .page-content .stat .num {{ font-size: 28px; font-weight: 800; color: var(--color-primary); }}
    .page-content .stat .label {{ font-size: 12px; font-weight: 600; color: var(--color-text-secondary); margin-top: 4px; }}
    .page-content .faq-item {{ border-bottom: 1px solid var(--color-border); padding: 16px 0; }}
    .page-content .faq-q {{ font-size: 15px; font-weight: 600; color: var(--color-text-main); cursor: pointer; display: flex; justify-content: space-between; align-items: center; }}
    .page-content .faq-q::after {{ content: '+'; font-size: 20px; color: var(--color-text-subtle); }}
    .page-content .faq-a {{ display: none; font-size: 14px; line-height: 22px; color: var(--color-text-secondary); margin-top: 10px; }}
    .page-content .faq-item.open .faq-a {{ display: block; }}
    .page-content .faq-item.open .faq-q::after {{ content: '\\2212'; }}
    .page-content .contact-card {{ display: flex; gap: 14px; background: var(--color-bg-neutral); border-radius: 12px; padding: 16px; margin-bottom: 12px; align-items: center; text-decoration: none; color: inherit; transition: background 0.15s; }}
    .page-content .contact-card:hover {{ background: #edf0f3; }}
    .page-content .contact-card .ic {{ width: 44px; height: 44px; border-radius: 50%; background: var(--color-primary-weak); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
    .page-content .contact-card .ic svg {{ width: 22px; height: 22px; stroke: var(--color-primary); fill: none; stroke-width: 2; }}
    .page-content .contact-card .ct {{ flex: 1; }}
    .page-content .contact-card .ct strong {{ font-size: 14px; display: block; }}
    .page-content .contact-card .ct span {{ font-size: 13px; color: var(--color-text-subtle); }}
    .legal-text h2 {{ font-size: 18px; margin-top: 24px; }}
    .legal-text h3 {{ font-size: 15px; margin-top: 18px; }}
    .legal-text p, .legal-text li {{ font-size: 13px; line-height: 21px; }}
    .footer {{ background: #031419; color: white; padding: 32px 16px 40px; }}
    .footer-cols {{ display: flex; justify-content: space-between; margin-bottom: 32px; }}
    .footer-col h5 {{ font-size: 14px; font-weight: 700; margin-bottom: 10px; }}
    .footer-col ul {{ list-style: none; }}
    .footer-col ul li {{ font-size: 13px; line-height: 22px; margin-bottom: 4px; }}
    .footer-col ul li a {{ color: rgba(255,255,255,0.75); text-decoration: none; transition: color 0.15s; }}
    .footer-col ul li a:hover {{ color: white; }}
    .footer .legal {{ border-top: 1px solid rgba(255,255,255,0.15); padding-top: 16px; font-size: 12px; color: rgba(255,255,255,0.5); }}
    .footer .legal a {{ color: white; text-decoration: none; }}
  </style>
</head>
<body>
  <nav class="nav">
    <a href="home.html" class="nav-logo">fever</a>
    <a href="javascript:history.back()" class="nav-back">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
      Back
    </a>
  </nav>
  <div class="page-hero">
    <h1>{title}</h1>
    <p>{subtitle}</p>
  </div>
  <div class="page-content{extra_class}">
    {content}
  </div>
''' + FOOTER_HTML + '''
  {extra_js}
</body>
</html>'''

pages = {}

pages['press.html'] = dict(title='Press', subtitle='Fever in the news. Media resources and press releases.', extra_class='', extra_js='', content='''<h2>About Fever</h2>
    <p>Fever is the leading global live-entertainment discovery platform with a mission to democratize access to culture and entertainment. With a growing presence in over 100 cities, Fever has helped millions discover the best experiences in their city.</p>
    <div class="stat-grid">
      <div class="stat"><div class="num">100+</div><div class="label">Cities worldwide</div></div>
      <div class="stat"><div class="num">80M+</div><div class="label">Users</div></div>
      <div class="stat"><div class="num">150K+</div><div class="label">Experiences</div></div>
      <div class="stat"><div class="num">2014</div><div class="label">Founded</div></div>
    </div>
    <h2>Press Releases</h2>
    <div class="card"><h3>Fever expands Candlelight to 50 new cities</h3><p>January 2026 &mdash; The iconic classical music series by candlelight continues its global expansion.</p></div>
    <div class="card"><h3>Fever partners with major venues worldwide</h3><p>November 2025 &mdash; Fever announces strategic partnerships with leading cultural venues.</p></div>
    <div class="card"><h3>Fever reaches 80 million users</h3><p>September 2025 &mdash; The platform celebrates a milestone of 80 million registered users globally.</p></div>
    <h2>Media Contact</h2>
    <p>For press inquiries: <strong>press@feverup.com</strong></p>
    <a href="mailto:press@feverup.com" class="btn">Contact Press Team</a>''')

pages['careers.html'] = dict(title='Careers', subtitle='Join the team building the future of live entertainment.', extra_class='', extra_js='', content='''<h2>Why Fever?</h2>
    <p>We are a global team of passionate people building the technology that connects millions with the experiences they love.</p>
    <div class="stat-grid">
      <div class="stat"><div class="num">2,000+</div><div class="label">Team members</div></div>
      <div class="stat"><div class="num">40+</div><div class="label">Nationalities</div></div>
      <div class="stat"><div class="num">15</div><div class="label">Offices</div></div>
      <div class="stat"><div class="num">100+</div><div class="label">Open positions</div></div>
    </div>
    <h2>Our Values</h2>
    <div class="card"><h3>&#127775; Own it</h3><p>We take ownership and pride in everything we do.</p></div>
    <div class="card"><h3>&#128640; Move fast</h3><p>We ship quickly, iterate constantly, and never stop improving.</p></div>
    <div class="card"><h3>&#129309; Win together</h3><p>We collaborate across teams and celebrate collective success.</p></div>
    <div class="card"><h3>&#127919; Think big</h3><p>We dream boldly and set ambitious goals.</p></div>
    <h2>Open Positions</h2>
    <div class="card"><h3>Senior Frontend Engineer</h3><p>Madrid &middot; Engineering &middot; Full-time</p><a href="#" class="btn">Apply now</a></div>
    <div class="card"><h3>Product Designer</h3><p>Madrid &middot; Design &middot; Full-time</p><a href="#" class="btn">Apply now</a></div>
    <div class="card"><h3>Data Scientist</h3><p>New York &middot; Data &middot; Full-time</p><a href="#" class="btn">Apply now</a></div>
    <div class="card"><h3>City Manager</h3><p>London &middot; Operations &middot; Full-time</p><a href="#" class="btn">Apply now</a></div>''')

pages['fellowships.html'] = dict(title='Fellowships', subtitle='Early career programs to launch your journey in entertainment tech.', extra_class='', extra_js='', content='''<h2>Fever Fellowship Program</h2>
    <p>Our program is designed for recent graduates passionate about technology and entertainment. Fellows work on real projects alongside senior team members.</p>
    <h2>Program Details</h2>
    <div class="card"><h3>Duration</h3><p>6 months, full-time paid fellowship with possibility of conversion.</p></div>
    <div class="card"><h3>Areas</h3><p>Engineering, Product, Data, Marketing, Operations, and Business Development.</p></div>
    <div class="card"><h3>Locations</h3><p>Madrid, New York, London, Paris, and other offices worldwide.</p></div>
    <h2>What You Get</h2>
    <ul>
      <li>Hands-on experience with real products used by millions</li>
      <li>Mentorship from industry leaders</li>
      <li>Competitive compensation and benefits</li>
      <li>Access to all Fever experiences during your fellowship</li>
    </ul>
    <a href="careers.html" class="btn">Visit Careers</a>''')

pages['gift-cards.html'] = dict(title='Gift Cards', subtitle='Give the gift of unforgettable experiences.', extra_class='', extra_js='', content='''<h2>Fever Gift Cards</h2>
    <p>Fever Gift Cards let your loved ones choose from thousands of experiences &mdash; from Candlelight concerts to immersive exhibitions, food tours, and more.</p>
    <div class="card"><h3>&#127873; How it works</h3><p><strong>1.</strong> Choose your amount (from &euro;10 to &euro;500)<br><strong>2.</strong> Personalize it with a message<br><strong>3.</strong> Send instantly via email or print<br><strong>4.</strong> Recipient picks their favorite experience</p></div>
    <h2>Popular Gift Cards</h2>
    <div class="card"><h3>Candlelight Gift Card</h3><p>Live classical music by candlelight. Valid in 100+ cities.</p><p><strong>From &euro;40.00</strong></p></div>
    <div class="card"><h3>Fever Madrid Gift Card</h3><p>Redeemable for any experience in Madrid.</p><p><strong>From &euro;10.00</strong></p></div>
    <div class="card"><h3>Birthday Gift Card</h3><p>A specially designed card for experience lovers.</p><p><strong>From &euro;20.00</strong></p></div>
    <h2>Corporate Gift Cards</h2>
    <p>Volume discounts and custom branding for corporate orders.</p>
    <a href="corporate.html" class="btn">Corporate Solutions</a>''')

pages['help-center.html'] = dict(title='Help Center', subtitle='Find answers or contact our support team.', extra_class='', extra_js='<script>document.querySelectorAll(".faq-item").forEach(function(el){el.querySelector(".faq-q").addEventListener("click",function(){el.classList.toggle("open");});});</script>', content='''<h2>Frequently Asked Questions</h2>
    <div class="faq-item"><div class="faq-q">How do I purchase tickets?</div><div class="faq-a">Browse experiences on Fever, select your date and tickets, and complete purchase. You receive confirmation via email.</div></div>
    <div class="faq-item"><div class="faq-q">Can I cancel or get a refund?</div><div class="faq-a">Refund policies vary by experience. Generally, cancellations up to 48 hours before the event are eligible for a full refund.</div></div>
    <div class="faq-item"><div class="faq-q">Where do I find my tickets?</div><div class="faq-a">In the Fever app under "My Plans" and in your confirmation email. Show the QR code at the venue.</div></div>
    <div class="faq-item"><div class="faq-q">How do I change the date?</div><div class="faq-a">If date changes are available, modify in the app under "My Plans".</div></div>
    <div class="faq-item"><div class="faq-q">How do I redeem a gift card?</div><div class="faq-a">Enter your code at checkout or add it in app settings under "Gift Cards &amp; Credits".</div></div>
    <div class="faq-item"><div class="faq-q">Is my payment secure?</div><div class="faq-a">Yes. All payments use secure, PCI-compliant providers. We accept cards, Apple Pay, Google Pay, and PayPal.</div></div>
    <h2>Contact Support</h2>
    <a href="contact.html" class="contact-card"><div class="ic"><svg viewBox="0 0 24 24"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg></div><div class="ct"><strong>Live Chat</strong><span>Available 24/7</span></div></a>
    <a href="mailto:help@feverup.com" class="contact-card"><div class="ic"><svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></div><div class="ct"><strong>Email</strong><span>help@feverup.com</span></div></a>''')

pages['fever-zone.html'] = dict(title='Fever Zone', subtitle='Manage your events and reach millions.', extra_class='', extra_js='', content='''<h2>Your Event Dashboard</h2>
    <p>Fever Zone is the all-in-one platform for event organizers. Manage listings, track sales, access analytics, and grow your audience.</p>
    <h2>What You Can Do</h2>
    <div class="card"><h3>&#128202; Real-time Analytics</h3><p>Track ticket sales, revenue, and audience demographics with live dashboards.</p></div>
    <div class="card"><h3>&#127919; Audience Targeting</h3><p>Reach the right audience with AI-powered recommendations and marketing tools.</p></div>
    <div class="card"><h3>&#128176; Revenue Optimization</h3><p>Dynamic pricing, promo codes, and upselling tools.</p></div>
    <div class="card"><h3>&#128241; Seamless Check-in</h3><p>QR scanning, guest lists, and real-time capacity tracking.</p></div>
    <h2>Get Started</h2>
    <p>Already have an account? Log in. New organizer? Create your free account.</p>
    <a href="#" class="btn">Log in to Fever Zone</a>''')

pages['list-event.html'] = dict(title='List Your Event', subtitle='Reach millions of people looking for experiences.', extra_class='', extra_js='', content='''<h2>Why List on Fever?</h2>
    <div class="stat-grid">
      <div class="stat"><div class="num">80M+</div><div class="label">Active users</div></div>
      <div class="stat"><div class="num">100+</div><div class="label">Cities</div></div>
    </div>
    <h2>How It Works</h2>
    <div class="card"><h3>1. Submit your event</h3><p>Fill in details, upload images, set pricing, choose dates.</p></div>
    <div class="card"><h3>2. We review &amp; optimize</h3><p>Our team reviews and optimizes your listing for maximum visibility.</p></div>
    <div class="card"><h3>3. Start selling</h3><p>Your event goes live and reaches millions.</p></div>
    <h2>What You Get</h2>
    <ul>
      <li>Featured placement in the Fever app and website</li>
      <li>AI-powered audience matching</li>
      <li>Marketing support and promotional tools</li>
      <li>Detailed analytics and reporting</li>
      <li>Secure payment processing and fast payouts</li>
    </ul>
    <a href="#" class="btn">Submit your event</a>''')

pages['affiliate.html'] = dict(title='Affiliate Program', subtitle='Earn commissions by promoting the best experiences.', extra_class='', extra_js='', content='''<h2>Join the Fever Affiliate Program</h2>
    <p>Earn commissions every time someone books through your unique link.</p>
    <h2>How It Works</h2>
    <div class="card"><h3>1. Sign up</h3><p>Apply to become an affiliate. Approval in 24-48 hours.</p></div>
    <div class="card"><h3>2. Share your links</h3><p>Get unique tracking links for any Fever experience.</p></div>
    <div class="card"><h3>3. Earn commissions</h3><p>Earn on every sale. Monthly payouts.</p></div>
    <h2>Benefits</h2>
    <ul>
      <li>Competitive commission rates</li>
      <li>30-day cookie window</li>
      <li>Creative assets and banners</li>
      <li>Dedicated affiliate manager</li>
      <li>Real-time reporting dashboard</li>
    </ul>
    <a href="#" class="btn">Apply now</a>''')

pages['ambassadors.html'] = dict(title='Ambassadors', subtitle='Become a Fever ambassador and inspire your community.', extra_class='', extra_js='', content='''<h2>Fever Ambassador Program</h2>
    <p>Are you a content creator or community leader who loves sharing experiences? Get exclusive perks while inspiring your followers.</p>
    <h2>What You Get</h2>
    <div class="card"><h3>&#127881; Free experiences</h3><p>Complimentary tickets to the best experiences in your city.</p></div>
    <div class="card"><h3>&#128184; Earn commissions</h3><p>Share your code and earn on every sale.</p></div>
    <div class="card"><h3>&#11088; Exclusive access</h3><p>First to know about new experiences and VIP events.</p></div>
    <div class="card"><h3>&#128247; Content support</h3><p>Professional photos and behind-the-scenes content.</p></div>
    <h2>Requirements</h2>
    <ul>
      <li>Active social media presence (5K+ followers)</li>
      <li>Passion for live entertainment</li>
      <li>Based in a city where Fever operates</li>
    </ul>
    <a href="#" class="btn">Apply to be an Ambassador</a>''')

pages['contact.html'] = dict(title='Contact Us', subtitle="We're here to help. Reach out anytime, 24/7.", extra_class='', extra_js='', content='''<h2>Get in Touch</h2>
    <a href="#" class="contact-card"><div class="ic"><svg viewBox="0 0 24 24"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg></div><div class="ct"><strong>Live Chat</strong><span>Average response: 2 minutes</span></div></a>
    <a href="mailto:help@feverup.com" class="contact-card"><div class="ic"><svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></div><div class="ct"><strong>Email Support</strong><span>help@feverup.com</span></div></a>
    <a href="help-center.html" class="contact-card"><div class="ic"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg></div><div class="ct"><strong>Help Center</strong><span>Browse FAQs and guides</span></div></a>
    <h2>Office Locations</h2>
    <div class="card"><h3>&#127466;&#127480; Madrid (HQ)</h3><p>Calle de Alcal&aacute;, 28014 Madrid, Spain</p></div>
    <div class="card"><h3>&#127482;&#127480; New York</h3><p>1 World Trade Center, New York, NY 10007</p></div>
    <div class="card"><h3>&#127468;&#127463; London</h3><p>1 Poultry, London EC2R 8EJ, United Kingdom</p></div>
    <div class="card"><h3>&#127467;&#127479; Paris</h3><p>31 Rue du 4 Septembre, 75002 Paris, France</p></div>
    <h2>Press Inquiries</h2>
    <p><a href="mailto:press@feverup.com">press@feverup.com</a></p>''')

pages['faqs.html'] = dict(title='FAQs', subtitle='Quick answers to common questions.', extra_class='', extra_js='<script>document.querySelectorAll(".faq-item").forEach(function(el){el.querySelector(".faq-q").addEventListener("click",function(){el.classList.toggle("open");});});</script>', content='''<h2>Purchasing &amp; Booking</h2>
    <div class="faq-item"><div class="faq-q">How do I buy tickets?</div><div class="faq-a">Browse experiences, select your date and tickets, and complete purchase. Payment is processed securely.</div></div>
    <div class="faq-item"><div class="faq-q">What payment methods do you accept?</div><div class="faq-a">Visa, Mastercard, Amex, Apple Pay, Google Pay, and PayPal. Available methods may vary by region.</div></div>
    <div class="faq-item"><div class="faq-q">Can I buy for someone else?</div><div class="faq-a">Yes! Purchase and forward the confirmation email, or send a Fever Gift Card.</div></div>
    <h2>Cancellations &amp; Refunds</h2>
    <div class="faq-item"><div class="faq-q">Can I cancel my booking?</div><div class="faq-a">Most experiences allow free cancellation up to 48 hours before. Check the experience page for specific terms.</div></div>
    <div class="faq-item"><div class="faq-q">How long do refunds take?</div><div class="faq-a">5-10 business days to your original payment method.</div></div>
    <div class="faq-item"><div class="faq-q">What if the event is cancelled?</div><div class="faq-a">Full automatic refund. We notify you via email as soon as possible.</div></div>
    <h2>Account &amp; Tickets</h2>
    <div class="faq-item"><div class="faq-q">Where are my tickets?</div><div class="faq-a">In the app under "My Plans" and in your email. Show the QR code at the venue.</div></div>
    <div class="faq-item"><div class="faq-q">Can I change the date?</div><div class="faq-a">If allowed, modify in the app under "My Plans".</div></div>
    <div class="faq-item"><div class="faq-q">I forgot my password</div><div class="faq-a">Tap "Forgot password" on login. We send a reset link to your email.</div></div>
    <p style="margin-top:24px;">Still need help? <a href="contact.html">Contact support</a></p>''')

pages['terms.html'] = dict(title='Terms of Use', subtitle='Last updated: January 1, 2026', extra_class=' legal-text', extra_js='', content='''<h2>1. Acceptance of Terms</h2>
    <p>By accessing or using the Fever platform, you agree to be bound by these Terms of Use.</p>
    <h2>2. Description of Service</h2>
    <p>Fever provides a platform for discovering, purchasing, and attending live entertainment experiences. We act as an intermediary between organizers and attendees.</p>
    <h2>3. Account Registration</h2>
    <p>To purchase tickets, you must create an account. You are responsible for maintaining confidentiality of your credentials and for all activities under your account.</p>
    <h2>4. Purchases and Payments</h2>
    <p>All purchases are subject to availability. Prices include applicable taxes unless otherwise stated. Service fees may apply and will be displayed before confirmation.</p>
    <h2>5. Cancellations and Refunds</h2>
    <p>Cancellation and refund policies vary by experience. Generally, cancellations made more than 48 hours before the start time are eligible for a full refund.</p>
    <h2>6. User Conduct</h2>
    <p>You agree not to: use the platform for unlawful purposes; resell tickets without authorization; create multiple accounts to circumvent restrictions; interfere with platform operation.</p>
    <h2>7. Intellectual Property</h2>
    <p>All content on Fever is owned by or licensed to Fever and protected by intellectual property laws.</p>
    <h2>8. Limitation of Liability</h2>
    <p>Fever shall not be liable for indirect, incidental, or consequential damages. Our total liability shall not exceed the amount paid for the specific experience.</p>
    <h2>9. Changes to Terms</h2>
    <p>Fever may modify these terms at any time. Continued use constitutes acceptance.</p>
    <h2>10. Governing Law</h2>
    <p>These terms are governed by the laws of Spain. Disputes shall be resolved in the courts of Madrid.</p>
    <p style="margin-top:24px;">Questions? <a href="mailto:legal@feverup.com">legal@feverup.com</a></p>''')

pages['privacy.html'] = dict(title='Privacy Policy', subtitle='Last updated: January 1, 2026', extra_class=' legal-text', extra_js='', content='''<h2>1. Introduction</h2>
    <p>Fever Labs, Inc. respects your privacy and is committed to protecting your personal data.</p>
    <h2>2. Data We Collect</h2>
    <h3>Information you provide</h3>
    <ul><li>Account information (name, email, phone)</li><li>Payment information (via secure third-party providers)</li><li>Profile preferences and interests</li></ul>
    <h3>Automatically collected</h3>
    <ul><li>Device and browser information</li><li>IP address and approximate location</li><li>Usage data and cookies</li></ul>
    <h2>3. How We Use Your Data</h2>
    <ul><li>Process transactions and deliver tickets</li><li>Personalize your experience</li><li>Send relevant communications (with consent)</li><li>Improve our platform</li><li>Prevent fraud and ensure security</li></ul>
    <h2>4. Data Sharing</h2>
    <p>We share data only with: experience organizers, payment processors, service providers, and when required by law. We do not sell personal data.</p>
    <h2>5. Your Rights</h2>
    <p>Under GDPR, you have the right to: access, rectify, delete, restrict processing, data portability, and object. Contact <a href="mailto:privacy@feverup.com">privacy@feverup.com</a>.</p>
    <h2>6. Security</h2>
    <p>We implement industry-standard security including encryption, access controls, and regular audits.</p>
    <h2>7. Contact</h2>
    <p>Data Protection Officer: <a href="mailto:privacy@feverup.com">privacy@feverup.com</a></p>''')

pages['cookies.html'] = dict(title='Cookie Policy', subtitle='Last updated: January 1, 2026', extra_class=' legal-text', extra_js='', content='''<h2>What Are Cookies?</h2>
    <p>Cookies are small text files stored on your device when you visit a website. They help remember preferences and understand interactions.</p>
    <h2>Cookies We Use</h2>
    <h3>Essential Cookies</h3>
    <p>Required for core features: authentication, shopping cart, payment processing. Cannot be disabled.</p>
    <h3>Analytics Cookies</h3>
    <p>Help us understand visitor interactions. Aggregated and anonymized data via Google Analytics.</p>
    <h3>Personalization Cookies</h3>
    <p>Remember preferences (language, city, interests) and customize your experience.</p>
    <h3>Marketing Cookies</h3>
    <p>Deliver relevant ads and measure campaign effectiveness. May be set by third-party partners.</p>
    <h2>Managing Cookies</h2>
    <ul><li><strong>Chrome:</strong> Settings &rarr; Privacy &rarr; Cookies</li><li><strong>Safari:</strong> Preferences &rarr; Privacy</li><li><strong>Firefox:</strong> Settings &rarr; Privacy &amp; Security</li></ul>
    <p>Disabling certain cookies may affect functionality.</p>
    <p style="margin-top:24px;">Questions? <a href="mailto:privacy@feverup.com">privacy@feverup.com</a></p>''')

pages['private-events.html'] = dict(title='Private Events', subtitle='Curated experiences for your team, clients, or special occasion.', extra_class='', extra_js='', content='''<h2>Fever Private Events</h2>
    <p>From intimate team dinners to large-scale galas, we create bespoke live entertainment experiences tailored to your needs.</p>
    <h2>Our Offerings</h2>
    <div class="card"><h3>&#127926; Private Candlelight Concerts</h3><p>Exclusive classical music performances in stunning venues. Fully customizable.</p></div>
    <div class="card"><h3>&#127860; Culinary Experiences</h3><p>Private chef dinners, cocktail masterclasses, and food tours.</p></div>
    <div class="card"><h3>&#127912; Immersive Team Building</h3><p>Escape rooms, interactive theater, and creative workshops.</p></div>
    <div class="card"><h3>&#127878; Celebrations</h3><p>Birthdays, anniversaries, proposals, and milestone events.</p></div>
    <h2>Why Choose Fever?</h2>
    <ul><li>Dedicated event planner</li><li>Access to 500+ venues worldwide</li><li>End-to-end production</li><li>Custom branding and theming</li><li>Budgets starting from &euro;1,000</li></ul>
    <a href="contact.html" class="btn">Request a quote</a>''')

pages['corporate.html'] = dict(title='Corporate Benefits', subtitle='Boost employee wellness with the gift of experiences.', extra_class='', extra_js='', content='''<h2>Fever for Business</h2>
    <p>Give employees and clients access to thousands of experiences. Boost engagement, reward performance, and create memorable moments.</p>
    <h2>Solutions</h2>
    <div class="card"><h3>&#127873; Corporate Gift Cards</h3><p>Bulk gift cards with custom branding. Volume discounts available.</p></div>
    <div class="card"><h3>&#127775; Employee Benefits</h3><p>Integrate Fever into your benefits program with exclusive discounts.</p></div>
    <div class="card"><h3>&#128188; Client Entertainment</h3><p>Curated experience packages to build relationships.</p></div>
    <div class="stat-grid">
      <div class="stat"><div class="num">500+</div><div class="label">Corporate clients</div></div>
      <div class="stat"><div class="num">95%</div><div class="label">Satisfaction rate</div></div>
    </div>
    <a href="contact.html" class="btn">Get started</a>''')

pages['gift-vouchers.html'] = dict(title='Gift Vouchers', subtitle='Custom-branded experience vouchers for your business.', extra_class='', extra_js='', content='''<h2>Custom Gift Vouchers</h2>
    <p>Create branded gift vouchers for employee recognition, client appreciation, and promotions.</p>
    <h2>How It Works</h2>
    <div class="card"><h3>1. Choose your design</h3><p>Select from templates or upload your branding.</p></div>
    <div class="card"><h3>2. Set the value</h3><p>From &euro;10 to &euro;500. Volume discounts for 50+.</p></div>
    <div class="card"><h3>3. Distribute</h3><p>Send digitally or order physical cards with premium packaging.</p></div>
    <h2>Pricing</h2>
    <div class="card"><h3>Standard</h3><p>1-49 vouchers &middot; Face value &middot; Free digital delivery</p></div>
    <div class="card"><h3>Business</h3><p>50-499 vouchers &middot; 5% discount &middot; Custom branding</p></div>
    <div class="card"><h3>Enterprise</h3><p>500+ vouchers &middot; 10% discount &middot; Dedicated manager</p></div>
    <a href="contact.html" class="btn">Order vouchers</a>''')

for filename, data in pages.items():
    html = TEMPLATE.format(**data)
    with open(filename, 'w') as f:
        f.write(html)
    print(f'Created {filename}')

print(f'Done! Created {len(pages)} pages')
