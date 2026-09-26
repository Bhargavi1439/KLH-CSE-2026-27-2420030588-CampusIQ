import os
import shutil

base = r'C:\Users\krish\.gemini\antigravity-ide\scratch\CampusIQ-AI\backend\dashboard-service'
source_base = r'C:\Users\krish\.gemini\antigravity-ide\scratch\CampusIQ-AI\backend\auth-service'

if not os.path.exists(base):
    shutil.copytree(source_base, base)

src = os.path.join(base, 'src', 'main', 'java', 'com', 'campusiq', 'dashboard')
old_src = os.path.join(base, 'src', 'main', 'java', 'com', 'campusiq', 'auth')

if os.path.exists(old_src):
    os.rename(old_src, src)

# Delete unnecessary auth stuff
for d in ['controller', 'dto', 'service', 'util']:
    shutil.rmtree(os.path.join(src, d), ignore_errors=True)

# Create missing directories
for d in ['controller', 'service', 'dto']:
    os.makedirs(os.path.join(src, d), exist_ok=True)

# Keep security
for root, dirs, files in os.walk(src):
    for f in files:
        if f.endswith('.java'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            content = content.replace('com.campusiq.auth', 'com.campusiq.dashboard')
            content = content.replace('AuthServiceApplication', 'DashboardServiceApplication')
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

# Rename main class file if necessary
main_old = os.path.join(src, 'AuthServiceApplication.java')
if os.path.exists(main_old):
    os.rename(main_old, os.path.join(src, 'DashboardServiceApplication.java'))

with open(os.path.join(base, 'pom.xml'), 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace('<artifactId>auth-service</artifactId>', '<artifactId>dashboard-service</artifactId>')
content = content.replace('<name>CampusIQ Auth Service</name>', '<name>CampusIQ Dashboard Service</name>')
content = content.replace('<description>Authentication and Security Service for CampusIQ</description>', '<description>Dashboard Service for CampusIQ</description>')
with open(os.path.join(base, 'pom.xml'), 'w', encoding='utf-8') as file:
    file.write(content)

print("Dashboard service setup complete.")
