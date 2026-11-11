import sqlite3, shutil, os

base = r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'
for prof in ['Default', 'Profile 3', 'Profile 4', 'Profile 5']:
    src = os.path.join(base, prof, 'History')
    if os.path.exists(src):
        dst = os.path.join(r'C:\Users\Administrator\.gemini\antigravity\scratch\phuquocbds', f'hist_{prof.replace(" ", "_")}')
        try:
            shutil.copyfile(src, dst)
            conn = sqlite3.connect(dst)
            c = conn.cursor()
            rows = c.execute("SELECT url, title FROM urls WHERE url LIKE '%cloudflare%' ORDER BY last_visit_time DESC LIMIT 10").fetchall()
            if rows:
                print(f'=== {prof} ===')
                for r in rows:
                    print(r[0], r[1])
            conn.close()
            os.remove(dst)
        except Exception as e:
            print(f'Error in {prof}: {e}')
