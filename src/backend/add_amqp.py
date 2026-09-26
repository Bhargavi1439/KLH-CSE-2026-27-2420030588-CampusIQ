import os

def add_amqp(pom_path):
    with open(pom_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'spring-boot-starter-amqp' not in content:
        dep = '''        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-amqp</artifactId>
        </dependency>
    </dependencies>'''
        content = content.replace('</dependencies>', dep)
        with open(pom_path, 'w', encoding='utf-8') as f:
            f.write(content)

base = r'C:\Users\krish\.gemini\antigravity-ide\scratch\CampusIQ-AI\backend'
add_amqp(os.path.join(base, 'event-service', 'pom.xml'))
add_amqp(os.path.join(base, 'notification-service', 'pom.xml'))
