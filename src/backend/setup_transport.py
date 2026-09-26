import os
import shutil

base = r'C:\Users\krish\.gemini\antigravity-ide\scratch\CampusIQ-AI\backend'
src_dir = os.path.join(base, 'resource-service')
dst_dir = os.path.join(base, 'transport-service')

if os.path.exists(dst_dir):
    shutil.rmtree(dst_dir)
shutil.copytree(src_dir, dst_dir)

# Remove target directory
shutil.rmtree(os.path.join(dst_dir, 'target'), ignore_errors=True)

# Rename package resource -> transport
old_pkg = os.path.join(dst_dir, 'src', 'main', 'java', 'com', 'campusiq', 'resource')
new_pkg = os.path.join(dst_dir, 'src', 'main', 'java', 'com', 'campusiq', 'transport')
os.rename(old_pkg, new_pkg)

# Replace text in java files
for root, dirs, files in os.walk(new_pkg):
    for f in files:
        if f.endswith('.java'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            content = content.replace('com.campusiq.resource', 'com.campusiq.transport')
            content = content.replace('ResourceServiceApplication', 'TransportServiceApplication')
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

# Rename Application class
os.rename(os.path.join(new_pkg, 'ResourceServiceApplication.java'), os.path.join(new_pkg, 'TransportServiceApplication.java'))

# Edit pom.xml
pom_path = os.path.join(dst_dir, 'pom.xml')
with open(pom_path, 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace('<artifactId>resource-service</artifactId>', '<artifactId>transport-service</artifactId>')
content = content.replace('<name>CampusIQ Resource Service</name>', '<name>CampusIQ Transport Service</name>')
content = content.replace('<description>Resource Service for CampusIQ</description>', '<description>Transport Service for CampusIQ</description>')
with open(pom_path, 'w', encoding='utf-8') as file:
    file.write(content)

# Edit application.yml
yml_path = os.path.join(dst_dir, 'src', 'main', 'resources', 'application.yml')
with open(yml_path, 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace('port: ', 'port: ')
content = content.replace('name: resource-service', 'name: transport-service')
content = content.replace('default_schema: resource_schema', 'default_schema: transport_schema')
with open(yml_path, 'w', encoding='utf-8') as file:
    file.write(content)

# Edit parent pom.xml
parent_pom = os.path.join(base, 'pom.xml')
with open(parent_pom, 'r', encoding='utf-8') as file:
    content = file.read()
if '<module>transport-service</module>' not in content:
    content = content.replace('<module>resource-service</module>', '<module>resource-service</module>\n        <module>transport-service</module>')
    with open(parent_pom, 'w', encoding='utf-8') as file:
        file.write(content)
