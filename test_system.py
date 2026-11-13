import sqlite3
import json

def test_db():
    print("   -> डेटाबेस बना रहे हैं...")
    conn = sqlite3.connect('ayushman_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS hospitals (
        id TEXT PRIMARY KEY, name TEXT, address TEXT, state TEXT, district TEXT, raw_data TEXT)''')
    
    print("   -> डमी (Test) डेटा डाल रहे हैं...")
    cursor.execute("INSERT OR REPLACE INTO hospitals (id, name, address, state, district, raw_data) VALUES (?, ?, ?, ?, ?, ?)",
                   ("test_1", "Ayushman Test Hospital", "Jind, Haryana", "Haryana", "Jind", "{}"))
    conn.commit()
    
    print("   -> डेटा वापस पढ़ कर चेक कर रहे हैं...")
    cursor.execute("SELECT name, state FROM hospitals WHERE id='test_1'")
    row = cursor.fetchone()
    conn.close()
    
    if row:
        print(f"   ✅ टेस्ट सफल! डेटाबेस में डेटा सेव है: {row[0]} ({row[1]})")
    else:
        print("   ❌ टेस्ट फेल! डेटा सेव नहीं हुआ।")

if __name__ == "__main__":
    test_db()
