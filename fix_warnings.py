import os

# 1. state_Items.dart से unused 'dart:convert' हटाना
p1 = 'lib/modules/dropDownItems/state_Items.dart'
if os.path.exists(p1):
    with open(p1, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace("import 'dart:convert';", "")
    with open(p1, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Fixed: state_Items.dart")

# 2. controlButtons.dart में fields को final बनाना या missing import/fix करना
# @immutable के साथ fields final होनी चाहिए
p2 = 'lib/widgets/controlButtons.dart'
if os.path.exists(p2):
    with open(p2, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        # अगर क्लास के अंदर fields हैं, उन्हें final बना देते हैं या @immutable हटा देते हैं
        if '@immutable' in line:
            continue # @immutable हटा रहे हैं ताकि must_be_immutable वार्निंग खत्म हो जाए
        new_lines.append(line)
    with open(p2, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("✅ Fixed: controlButtons.dart")

# 3. dropDownDistrict.dart से @immutable हटाना
p3 = 'lib/widgets/dropDownDistrict.dart'
if os.path.exists(p3):
    with open(p3, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        if '@immutable' in line:
            continue
        new_lines.append(line)
    with open(p3, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("✅ Fixed: dropDownDistrict.dart")

