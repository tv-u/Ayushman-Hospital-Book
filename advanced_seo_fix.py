import os

index_path = 'templates/index.html'

if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Advanced SEO Head Tags, Multilingual Support, Schema Markup & Zero-Competition Keywords
    seo_tags = """
    <!-- ========================================== -->
    <!-- ADVANCED MULTILINGUAL SEO & SCHEMA FIX     -->
    <!-- ========================================== -->
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
    <meta name="googlebot" content="index, follow">
    <meta name="bingbot" content="index, follow">
    
    <!-- Multilingual Alternate Links -->
    <link rel="alternate" hreflang="hi" href="https://tv-u.github.io/Ayushman-Hospital-Book/">
    <link rel="alternate" hreflang="en" href="https://tv-u.github.io/Ayushman-Hospital-Book/">
    <link rel="alternate" hreflang="bn" href="https://tv-u.github.io/Ayushman-Hospital-Book/">
    <link rel="alternate" hreflang="te" href="https://tv-u.github.io/Ayushman-Hospital-Book/">
    <link rel="alternate" hreflang="mr" href="https://tv-u.github.io/Ayushman-Hospital-Book/">
    <link rel="alternate" hreflang="ta" href="https://tv-u.github.io/Ayushman-Hospital-Book/">
    <link rel="alternate" hreflang="gu" href="https://tv-u.github.io/Ayushman-Hospital-Book/">
    <link rel="alternate" hreflang="x-default" href="https://tv-u.github.io/Ayushman-Hospital-Book/">

    <!-- Long-Tail & Zero-Competition Keywords -->
    <meta name="keywords" content="Ayushman Hospital List 2026, PM JAY empanelled hospitals near me, free government treatment hospital finder, आयुष्मान भारत अस्पताल सूची, सरकारी फ्री इलाज अस्पताल, Ayushman card hospital list PDF download, zero competition hospital directory India, state wise PMJAY hospital search">
    
    <!-- Open Graph / Social Media Meta Tags -->
    <meta property="og:title" content="Ayushman Hospital Directory & PM-JAY Finder 2026">
    <meta property="og:description" content="Find verified PM-JAY empanelled and government hospitals across all states and districts in India instantly.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://tv-u.github.io/Ayushman-Hospital-Book/">
    
    <!-- Schema.org Structured Data for Google Rich Results -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "MedicalWebPage",
      "name": "Ayushman Hospital Portal",
      "description": "Comprehensive directory of PM-JAY and government hospitals in India with automated daily sync.",
      "breadcrumb": "Home > Hospital Directory > Search",
      "audience": {
        "@type": "MedicalAudience",
        "audienceType": "Patient"
      },
      "significantLink": "https://tv-u.github.io/Ayushman-Hospital-Book/"
    }
    </script>
    <!-- ========================================== -->
    """

    # Add SEO tags inside <head> if not already present
    if "ADVANCED MULTILINGUAL SEO" not in html:
        if '<head>' in html:
            html = html.replace('<head>', '<head>\n' + seo_tags)
        else:
            html = seo_tags + html

        with open(index_path, 'w', encoding='text/plain', encoding_override='utf-8') as f:
            f.write(html)
        
        # Proper write using standard utf-8
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print("✅ Advanced SEO, Multilingual Meta, Schema Markup और Long-tail Keywords सफलतापूर्वक जोड़ दिए गए हैं!")
    else:
        print("ℹ️ Advanced SEO टैग्स पहले से मौजूद हैं।")

