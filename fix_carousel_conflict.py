import os

pubspec_path = 'pubspec.yaml'
if os.path.exists(pubspec_path):
    with open(pubspec_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # carousel_slider का पुराना वर्जन 4.1.1 हटाकर नया या सेफ वर्जन सेट कर रहे हैं
    if 'carousel_slider: ^4.1.1' in content:
        content = content.replace('carousel_slider: ^4.1.1', 'carousel_slider: ^5.0.0')
        print("✅ pubspec.yaml में carousel_slider का वर्जन अपडेट कर दिया गया है!")
    elif 'carousel_slider:' in content:
        print("ℹ️ carousel_slider पहले से मौजूद है।")
        
    with open(pubspec_path, 'w', encoding='utf-8') as f:
        f.write(content)
else:
    print("❌ pubspec.yaml नहीं मिली!")

# यदि प्रोजेक्ट के किसी Dart कोड में CarouselController का नेमस्पेस कॉन्फ्लिक्ट है, तो उसे एज पर शोहाइड (show/hide) इम्पोर्ट से ठीक करें
# निर्देशिका स्कैन करके ठीक करना
for root, dirs, files in os.walk('lib'):
    for file in files:
        if file.endswith('.dart'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                code = f.read()
            if 'carousel_slider' in code and 'show CarouselController' not in code:
                # इम्पोर्ट को रीडायरेक्ट कर रहे हैं ताकि नाम का टकराव न हो
                new_code = code.replace("import 'package:carousel_slider/carousel_slider.dart';", "import 'package:carousel_slider/carousel_slider.dart' hide CarouselController;\nimport 'package:carousel_slider/carousel_slider.dart' as cs show CarouselController;")
                if new_code != code:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_code)
                    print(f"✅ Fixed import conflict in: {filepath}")

