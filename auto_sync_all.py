import requests, json, sqlite3, os, time

API_KEY = "579b464db66ec23bdd0000015f84c036c77b46f64db25870fb252d5f"
with open('config.json', 'r') as f:
    config = json.load(f)
RESOURCE_ID = config.get('RESOURCE_ID')

conn = sqlite3.connect('ayushman_data.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS hospitals (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT)''')
conn.commit()

print("🚀 data.gov.in से सारा डेटा सिंक हो रहा है...")
offset = 0
limit = 1000
total_saved = 0

while True:
    url = f"https://api.data.gov.in/resource/{RESOURCE_ID}?api-key={API_KEY}&format=json&offset={offset}&limit={limit}"
    try:
        res = requests.get(url, timeout=60)
        data = res.json()
        records = data.get('records', [])
        
        if not records:
            break
            
        for rec in records:
            cursor.execute("INSERT INTO hospitals (data) VALUES (?)", (json.dumps(rec),))
        conn.commit()
        
        total_saved += len(records)
        print(f"📥 कुल {total_saved} रिकॉर्ड सिंक हो चुके हैं...")
        
        if len(records) < limit:
            break
        offset += limit
        time.sleep(1)
    except Exception as e:
        print(f"⚠️ एरर: {e}, फिर कोशिश कर रहे हैं...")
        time.sleep(5)

conn.close()
print(f"🎉 शानदार! कुल {total_saved} रिकॉर्ड सफलतापूर्वक सिंक हो गए हैं!")
