import os
import shutil

base = r'C:\Users\krish\.gemini\antigravity-ide\scratch\CampusIQ-AI\backend'
src_dir = os.path.join(base, 'transport-service')
dst_dir = os.path.join(base, 'event-service')

if os.path.exists(dst_dir):
    shutil.rmtree(dst_dir)
shutil.copytree(src_dir, dst_dir)

# Remove target directory
shutil.rmtree(os.path.join(dst_dir, 'target'), ignore_errors=True)

# Rename package transport -> event
old_pkg = os.path.join(dst_dir, 'src', 'main', 'java', 'com', 'campusiq', 'transport')
new_pkg = os.path.join(dst_dir, 'src', 'main', 'java', 'com', 'campusiq', 'event')
os.rename(old_pkg, new_pkg)

# Replace text in java files
for root, dirs, files in os.walk(new_pkg):
    for f in files:
        if f.endswith('.java'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            content = content.replace('com.campusiq.transport', 'com.campusiq.event')
            content = content.replace('TransportServiceApplication', 'EventServiceApplication')
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

# Rename Application class
os.rename(os.path.join(new_pkg, 'TransportServiceApplication.java'), os.path.join(new_pkg, 'EventServiceApplication.java'))

# Edit pom.xml
pom_path = os.path.join(dst_dir, 'pom.xml')
with open(pom_path, 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace('<artifactId>transport-service</artifactId>', '<artifactId>event-service</artifactId>')
content = content.replace('<name>CampusIQ Transport Service</name>', '<name>CampusIQ Event Service</name>')
content = content.replace('<description>Transport Service for CampusIQ</description>', '<description>Event Service for CampusIQ</description>')
with open(pom_path, 'w', encoding='utf-8') as file:
    file.write(content)

# Edit application.yml
yml_path = os.path.join(dst_dir, 'src', 'main', 'resources', 'application.yml')
with open(yml_path, 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace('port: ', 'port: ')
content = content.replace('name: transport-service', 'name: event-service')
content = content.replace('default_schema: transport_schema', 'default_schema: event_schema')
with open(yml_path, 'w', encoding='utf-8') as file:
    file.write(content)

# Edit parent pom.xml
parent_pom = os.path.join(base, 'pom.xml')
with open(parent_pom, 'r', encoding='utf-8') as file:
    content = file.read()
if '<module>event-service</module>' not in content:
    content = content.replace('<module>transport-service</module>', '<module>transport-service</module>\n        <module>event-service</module>')
    with open(parent_pom, 'w', encoding='utf-8') as file:
        file.write(content)
