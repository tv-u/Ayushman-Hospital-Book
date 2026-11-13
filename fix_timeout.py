import re

with open('sync_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# timeout को बढ़ाकर 120 सेकंड कर रहे हैं ताकि एरर न आए
new_content = re.sub(r'timeout\s*=\s*\d+', 'timeout=120', content)
if 'timeout=' not in new_content:
    new_content = new_content.replace('requests.get(', 'requests.get(timeout=120, ')

with open('sync_data.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ टाइमआउट 120 सेकंड सेट कर दिया गया है!")
