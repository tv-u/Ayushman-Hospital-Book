from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3, json, os, requests

app = Flask(__name__)
DB_FILE = 'ayushman_data.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hospitals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hospital_name TEXT,
            state TEXT,
            district TEXT,
            city TEXT,
            pincode TEXT,
            address TEXT,
            hospital_type TEXT,
            specialties TEXT,
            pm_jay TEXT,
            raw_data TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Stats
    total_hospitals = cursor.execute("SELECT COUNT(*) FROM hospitals").fetchone()[0]
    states = cursor.execute("SELECT COUNT(DISTINCT state) FROM hospitals").fetchone()[0]
    districts = cursor.execute("SELECT COUNT(DISTINCT district) FROM hospitals").fetchone()[0]
    
    # Search & Filters query parameters
    q = request.args.get('q', '')
    state_filter = request.args.get('state', '')
    type_filter = request.args.get('type', '')
    
    query = "SELECT id, hospital_name, state, district, hospital_type, specialties, pm_jay FROM hospitals WHERE 1=1"
    params = []
    
    if q:
        query += " AND (hospital_name LIKE ? OR city LIKE ? OR district LIKE ?)"
        params.extend([f'%{q}%', f'%{q}%', f'%{q}%'])
    if state_filter:
        query += " AND state = ?"
        params.append(state_filter)
    if type_filter:
        query += " AND hospital_type = ?"
        params.append(type_filter)
        
    query += " LIMIT 50"
    cursor.execute(query, params)
    hospitals = cursor.fetchall()
    
    # Get distinct states for filter dropdown
    cursor.execute("SELECT DISTINCT state FROM hospitals WHERE state IS NOT NULL ORDER BY state")
    states_list = [row[0] for row in cursor.fetchall()]
    
    conn.close()
    return render_template('index.html', 
                           total=total_hospitals, 
                           states_count=states, 
                           districts_count=districts,
                           hospitals=hospitals,
                           states_list=states_list,
                           query=q)

@app.route('/sync-data')
def sync_data():
    API_KEY = "579b464db66ec23bdd0000015f84c036c77b46f64db25870fb252d5f"
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        RESOURCE_ID = config.get('RESOURCE_ID', '3b01bcb8-0b14-4abf-b4f2-c1bfd3f4ba69')
    except:
        RESOURCE_ID = '3b01bcb8-0b14-4abf-b4f2-c1bfd3f4ba69'
        
    url = f"https://api.data.gov.in/resource/{RESOURCE_ID}?api-key={API_KEY}&format=json&limit=500"
    try:
        res = requests.get(url, timeout=30)
        data = res.json()
        records = data.get('records', [])
        
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        count = 0
        for rec in records:
            name = rec.get('hospital_name') or rec.get('name') or 'N/A'
            state = rec.get('state') or rec.get('state_name') or 'N/A'
            district = rec.get('district') or rec.get('district_name') or 'N/A'
            city = rec.get('city') or 'N/A'
            pincode = str(rec.get('pincode') or rec.get('pin') or '')
            address = rec.get('address') or 'N/A'
            h_type = rec.get('hospital_type') or 'General'
            specialties = rec.get('specialities') or rec.get('specialty') or 'Multi-Specialty'
            pm_jay = rec.get('pmjay_empanelled') or rec.get('empanelment_status') or 'Yes'
            
            cursor.execute('''
                INSERT INTO hospitals (hospital_name, state, district, city, pincode, address, hospital_type, specialties, pm_jay, raw_data)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, state, district, city, pincode, address, h_type, specialties, pm_jay, json.dumps(rec)))
            count += 1
            
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "synced_records": count})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    print("🚀 Ayushman Portal Master Server Running on http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
