import subprocess
import os
import urllib.request

REPO_DIR = r"C:\Users\Administrator\.gemini\antigravity\scratch\phuquocbds"
GIT_EXE = r"C:\Users\Administrator\AppData\Local\Programs\Git\cmd\git.exe"

print("--- 1. GIT STATUS ---")
res = subprocess.run([GIT_EXE, "status", "-s"], cwd=REPO_DIR, capture_output=True, text=True)
print(res.stdout)

print("--- 2. GIT ADD ---")
subprocess.run([GIT_EXE, "add", "-A"], cwd=REPO_DIR, check=True)

print("--- 3. GIT COMMIT ---")
res = subprocess.run([GIT_EXE, "commit", "-m", "feat(seo): Xuat ban bai viet Bang gia dat Tai dinh cu KP10 va KP5 Duong Dong 07:00 16/11"], cwd=REPO_DIR, capture_output=True, text=True)
print(res.stdout)

print("--- 4. GIT PUSH ---")
res = subprocess.run([GIT_EXE, "push", "origin", "main"], cwd=REPO_DIR, capture_output=True, text=True)
print(res.stdout)
print(res.stderr)

print("--- 5. DEPLOY TO SURGE CDN ---")
env = os.environ.copy()
env["PATH"] = r"C:\Users\Administrator\AppData\Local\Programs\Nodejs\node-v20.18.0-win-x64;" + env.get("PATH", "")
env["SURGE_LOGIN"] = "phuquocbds4878@fldubai.com"
env["SURGE_TOKEN"] = "2ba1fad35a72227eb6fe2dae2afdac00"

npx_cmd = r"C:\Users\Administrator\AppData\Local\Programs\Nodejs\node-v20.18.0-win-x64\npx.cmd"
res = subprocess.run([npx_cmd, "surge", REPO_DIR, "phuquocbds.surge.sh"], env=env, capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("Stderr:", res.stderr)

print("--- 6. VERIFY LIVE SURGE CDN ---")
article_url = "https://phuquocbds.surge.sh/bai-viet/bang-gia-dat-tai-dinh-cu-khu-pho-10-va-khu-pho-5-duong-dong-phu-quoc.html"
try:
    req = urllib.request.Request(article_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        print(f"URL: {article_url} -> Status: {resp.status} OK!")
except Exception as e:
    print(f"Error checking live URL: {e}")
