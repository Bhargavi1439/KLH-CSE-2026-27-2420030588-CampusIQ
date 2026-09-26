import os

base = r'C:\Users\krish\.gemini\antigravity-ide\scratch\CampusIQ-AI\backend\student-service'
yml_path = os.path.join(base, 'src', 'main', 'resources', 'application.yml')
with open(yml_path, 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace('port: 8081', 'port: 8082')
content = content.replace('default_schema: auth_schema', 'default_schema: student_schema')
with open(yml_path, 'w', encoding='utf-8') as file:
    file.write(content)

parent_pom = r'C:\Users\krish\.gemini\antigravity-ide\scratch\CampusIQ-AI\backend\pom.xml'
with open(parent_pom, 'r', encoding='utf-8') as file:
    content = file.read()
if '<module>student-service</module>' not in content:
    content = content.replace('<module>auth-service</module>', '<module>auth-service</module>\n        <module>student-service</module>')
    with open(parent_pom, 'w', encoding='utf-8') as file:
        file.write(content)
