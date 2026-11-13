from pathlib import Path
from datetime import date
import re
import json

root = Path(__file__).resolve().parent
index = root / "web" / "index.html"

html = index.read_text(encoding="utf-8")

# Remove previous generated SEO block before rebuilding
html = re.sub(
    r'<!-- AYUSHMAN SEO START -->.*?<!-- AYUSHMAN SEO END -->',
    '',
    html,
    flags=re.S
)

seo = """
<!-- AYUSHMAN SEO START -->
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="googlebot" content="index,follow">
<meta name="description" content="Find Ayushman Bharat PM-JAY empanelled hospitals and government hospitals across India. Search hospitals by state and district.">
<meta name="keywords" content="Ayushman Bharat Hospital List, PMJAY Hospital List, Ayushman Card Hospital, Government Hospital India, आयुष्मान भारत अस्पताल सूची">

<meta property="og:title" content="Ayushman Hospital Directory | PM-JAY Hospital Finder">
<meta property="og:description" content="Find Ayushman Bharat empanelled and government hospitals across India.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://tv-u.github.io/Ayushman-Hospital-Book/">
<meta property="og:site_name" content="Ayushman Hospital Directory">

<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="Ayushman Hospital Directory">
<meta name="twitter:description" content="Search PM-JAY and government hospitals across India.">

<link rel="canonical" href="https://tv-u.github.io/Ayushman-Hospital-Book/">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Ayushman Hospital Directory",
  "url": "https://tv-u.github.io/Ayushman-Hospital-Book/",
  "description": "Ayushman Bharat PM-JAY and government hospital directory in India"
}
</script>
<!-- AYUSHMAN SEO END -->
"""

if re.search(r"<head(?:\\s[^>]*)?>", html, re.I):
    html = re.sub(
        r"(<head(?:\\s[^>]*)?>)",
        lambda m: m.group(1) + "\\n" + seo,
        html,
        count=1,
        flags=re.I
    )
else:
    raise SystemExit("ERROR: HTML head tag missing")

index.write_text(html, encoding="utf-8")

print("SEO metadata successfully updated.")

# Sitemap
today = date.today().isoformat()
sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://tv-u.github.io/Ayushman-Hospital-Book/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
"""

(root / "web" / "sitemap.xml").write_text(
    sitemap, encoding="utf-8"
)

robots = """User-agent: *
Allow: /

Sitemap: https://tv-u.github.io/Ayushman-Hospital-Book/sitemap.xml
"""

(root / "web" / "robots.txt").write_text(
    robots, encoding="utf-8"
)

# Remove old broken generated script if present
print("Sitemap and robots.txt generated.")
