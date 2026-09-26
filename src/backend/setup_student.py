import os
import shutil

base = r'C:\Users\krish\.gemini\antigravity-ide\scratch\CampusIQ-AI\backend\student-service'
src = os.path.join(base, 'src', 'main', 'java', 'com', 'campusiq', 'student')

# Delete unnecessary auth stuff
for d in ['controller', 'dto', 'service']:
    shutil.rmtree(os.path.join(src, d), ignore_errors=True)

# Keep security, entity, repository
# Rename things in security
for root, dirs, files in os.walk(src):
    for f in files:
        if f.endswith('.java'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            content = content.replace('com.campusiq.auth', 'com.campusiq.student')
            content = content.replace('AuthServiceApplication', 'StudentServiceApplication')
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

with open(os.path.join(base, 'pom.xml'), 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace('<artifactId>auth-service</artifactId>', '<artifactId>student-service</artifactId>')
content = content.replace('<name>CampusIQ Auth Service</name>', '<name>CampusIQ Student Service</name>')
content = content.replace('<description>Authentication and Security Service for CampusIQ</description>', '<description>Student Service for CampusIQ</description>')
with open(os.path.join(base, 'pom.xml'), 'w', encoding='utf-8') as file:
    file.write(content)
