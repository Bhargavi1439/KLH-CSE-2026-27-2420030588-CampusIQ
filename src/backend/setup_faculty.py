import os
import shutil

base = r'C:\Users\krish\.gemini\antigravity-ide\scratch\CampusIQ-AI\backend'
src_dir = os.path.join(base, 'student-service')
dst_dir = os.path.join(base, 'faculty-service')

if os.path.exists(dst_dir):
    shutil.rmtree(dst_dir)
shutil.copytree(src_dir, dst_dir)

# Remove target directory
shutil.rmtree(os.path.join(dst_dir, 'target'), ignore_errors=True)

# Rename package student -> faculty
old_pkg = os.path.join(dst_dir, 'src', 'main', 'java', 'com', 'campusiq', 'student')
new_pkg = os.path.join(dst_dir, 'src', 'main', 'java', 'com', 'campusiq', 'faculty')
os.rename(old_pkg, new_pkg)

# Replace text in java files
for root, dirs, files in os.walk(new_pkg):
    for f in files:
        if f.endswith('.java'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            content = content.replace('com.campusiq.student', 'com.campusiq.faculty')
            content = content.replace('StudentServiceApplication', 'FacultyServiceApplication')
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

# Rename Application class
os.rename(os.path.join(new_pkg, 'StudentServiceApplication.java'), os.path.join(new_pkg, 'FacultyServiceApplication.java'))

# Edit pom.xml
pom_path = os.path.join(dst_dir, 'pom.xml')
with open(pom_path, 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace('<artifactId>student-service</artifactId>', '<artifactId>faculty-service</artifactId>')
content = content.replace('<name>CampusIQ Student Service</name>', '<name>CampusIQ Faculty Service</name>')
content = content.replace('<description>Student Service for CampusIQ</description>', '<description>Faculty Service for CampusIQ</description>')
with open(pom_path, 'w', encoding='utf-8') as file:
    file.write(content)

# Edit application.yml
yml_path = os.path.join(dst_dir, 'src', 'main', 'resources', 'application.yml')
with open(yml_path, 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace('port: ', 'port: ')
content = content.replace('name: student-service', 'name: faculty-service')
content = content.replace('default_schema: student_schema', 'default_schema: faculty_schema')
with open(yml_path, 'w', encoding='utf-8') as file:
    file.write(content)

# Edit parent pom.xml
parent_pom = os.path.join(base, 'pom.xml')
with open(parent_pom, 'r', encoding='utf-8') as file:
    content = file.read()
if '<module>faculty-service</module>' not in content:
    content = content.replace('<module>student-service</module>', '<module>student-service</module>\n        <module>faculty-service</module>')
    with open(parent_pom, 'w', encoding='utf-8') as file:
        file.write(content)
