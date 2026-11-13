import os

# Adsterra Smartlinks data from provided source[span_0](start_span)[span_0](end_span)
ads = [
    {"name": "Smartlink_1", "id": "28634833", "url": "https://asiafilm.org/4/c2b46070b44982014166acafd6074c3d"},
    {"name": "Smartlink_2", "id": "28731465", "url": "https://asiafilm.org/4/3711015d24018cf89ccb362976c4a2e0"},
    {"name": "Smartlink_3", "id": "30967579", "url": "https://asiafilm.org/4/dc01c1237bd130c5ef9bcfef4f0928ed"}
]

index_path = 'templates/index.html'

if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # विज्ञापन बैनर/बटन्स का HTML कोड तैयार करना
    ads_html = """
    <!-- Active Adsterra Smartlinks Section -->
    <div class="max-w-7xl mx-auto px-4 my-8">
        <div class="bg-gradient-to-r from-amber-500 to-orange-600 rounded-2xl p-6 text-white shadow-lg text-center">
            <h3 class="text-xl font-bold mb-3">🔥 विशेष स्वास्थ्य सेवाएँ और ऑफर्स</h3>
            <p class="text-amber-100 text-sm mb-4">नीचे दिए गए स्पॉन्सर लिंक्स पर क्लिक करके अधिक जानकारी प्राप्त करें:</p>
            <div class="flex flex-wrap justify-center gap-4">
    """
    
    for ad in ads:
        ads_html += f'<a href="{ad["url"]}" target="_blank" class="bg-white text-orange-600 hover:bg-amber-50 px-5 py-2.5 rounded-xl font-bold text-sm shadow transition transform hover:-translate-y-0.5">📢 {ad["name"]} ऑफर देखें</a>\n'

    ads_html += """
            </div>
        </div>
    </div>
    <!-- End Adsterra Section -->
    """

    # अगर पहले से एड्स नहीं जुड़े हैं, तो फुटर या मुख्य भाग के ऊपर जोड़ दें
    if "Active Adsterra Smartlinks Section" not in html:
        if '<footer' in html:
            html = html.replace('<footer', ads_html + '\n<footer')
        else:
            html += ads_html
            
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print("✅ Adsterra के तीनों Smartlinks (Smartlink_1, 2, 3) सफलता पूर्वक वेबसाइट पर एक्टिव कर दिए गए हैं!")
    else:
        print("ℹ️ विज्ञापन पहले से ही वेबसाइट पर एक्टिव हैं।")
else:
    print("❌ templates/index.html फाइल नहीं मिली!")

