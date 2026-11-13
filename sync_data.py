import requests, sqlite3, json, os, sys, time

with open("config.json", "r") as f:
    config = json.load(f)

API_KEY = "579b464db66ec23bdd0000015f84c036c77b46f64db25870fb252d5f"  # आपकी API Key
RESOURCE_ID = config["RESOURCE_ID"]

def sync_data():
    print("\n🔄 डेटा सिंक शुरू हो रहा है...")
    conn = sqlite3.connect('ayushman_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS hospitals (
        id TEXT PRIMARY KEY, name TEXT, address TEXT, state TEXT, district TEXT, raw_data TEXT)''')
    
    offset = 0
    limit = 100  # API की अधिकतम लिमिट
    total_fetched = 0
    
    while True:
        url = f"https://api.data.gov.in/resource/{RESOURCE_ID}?api-key={API_KEY}&format=json&offset={offset}&limit={limit}"
        try:
            response = requests.get(url, timeout=120)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            print(f"❌ नेटवर्क एरर: {e}")
            break
            
        records = data.get('records', [])
        total = int(data.get('total', 0))
        
        if not records:
            break
            
        for row in records:
            hosp_id = str(row.get('hospital_id', row.get('name', '') + row.get('address', '')))
            cursor.execute("SELECT id FROM hospitals WHERE id = ?", (hosp_id,))
            exists = cursor.fetchone()
            
            if exists:
                cursor.execute('''UPDATE hospitals SET name=?, address=?, state=?, district=?, raw_data=? WHERE id=?''',
                               (row.get('name'), row.get('address'), row.get('state'), row.get('district'), json.dumps(row), hosp_id))
            else:
                cursor.execute('''INSERT INTO hospitals (id, name, address, state, district, raw_data) VALUES (?, ?, ?, ?, ?, ?)''',
                               (hosp_id, row.get('name'), row.get('address'), row.get('state'), row.get('district'), json.dumps(row)))
        
        total_fetched += len(records)
        offset += limit
        print(f"   -> {total_fetched} / {total} रिकॉर्ड सिंक हुए...")
        
        if offset >= total:
            break
        
    conn.commit()
    conn.close()
    print(f"✅ सिंक पूरा! कुल {total_fetched} रिकॉर्ड प्रोसेस हुए।")

if __name__ == "__main__":
    sync_data()
