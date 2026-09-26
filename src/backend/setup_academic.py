import os
import shutil

base = r'C:\Users\krish\.gemini\antigravity-ide\scratch\CampusIQ-AI\backend'
src_dir = os.path.join(base, 'faculty-service')
dst_dir = os.path.join(base, 'academic-service')

if os.path.exists(dst_dir):
    shutil.rmtree(dst_dir)
shutil.copytree(src_dir, dst_dir)

# Remove target directory
shutil.rmtree(os.path.join(dst_dir, 'target'), ignore_errors=True)

# Rename package faculty -> academic
old_pkg = os.path.join(dst_dir, 'src', 'main', 'java', 'com', 'campusiq', 'faculty')
new_pkg = os.path.join(dst_dir, 'src', 'main', 'java', 'com', 'campusiq', 'academic')
os.rename(old_pkg, new_pkg)

# Replace text in java files
for root, dirs, files in os.walk(new_pkg):
    for f in files:
        if f.endswith('.java'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            content = content.replace('com.campusiq.faculty', 'com.campusiq.academic')
            content = content.replace('FacultyServiceApplication', 'AcademicServiceApplication')
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

# Rename Application class
os.rename(os.path.join(new_pkg, 'FacultyServiceApplication.java'), os.path.join(new_pkg, 'AcademicServiceApplication.java'))

# Edit pom.xml
pom_path = os.path.join(dst_dir, 'pom.xml')
with open(pom_path, 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace('<artifactId>faculty-service</artifactId>', '<artifactId>academic-service</artifactId>')
content = content.replace('<name>CampusIQ Faculty Service</name>', '<name>CampusIQ Academic Service</name>')
content = content.replace('<description>Faculty Service for CampusIQ</description>', '<description>Academic Service for CampusIQ</description>')
with open(pom_path, 'w', encoding='utf-8') as file:
    file.write(content)

# Edit application.yml
yml_path = os.path.join(dst_dir, 'src', 'main', 'resources', 'application.yml')
with open(yml_path, 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace('port: ', 'port: ')
content = content.replace('name: faculty-service', 'name: academic-service')
content = content.replace('default_schema: faculty_schema', 'default_schema: academic_schema')
with open(yml_path, 'w', encoding='utf-8') as file:
    file.write(content)

# Edit parent pom.xml
parent_pom = os.path.join(base, 'pom.xml')
with open(parent_pom, 'r', encoding='utf-8') as file:
    content = file.read()
if '<module>academic-service</module>' not in content:
    content = content.replace('<module>faculty-service</module>', '<module>faculty-service</module>\n        <module>academic-service</module>')
    with open(parent_pom, 'w', encoding='utf-8') as file:
        file.write(content)
