import os

def disable_amqp(app_path, app_name):
    with open(app_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'exclude = {org.springframework.boot.autoconfigure.amqp.RabbitAutoConfiguration.class}' not in content:
        content = content.replace('@SpringBootApplication', '@SpringBootApplication(exclude = {org.springframework.boot.autoconfigure.amqp.RabbitAutoConfiguration.class})')
        with open(app_path, 'w', encoding='utf-8') as f:
            f.write(content)

base = r'C:\Users\krish\.gemini\antigravity-ide\scratch\CampusIQ-AI\backend'
disable_amqp(os.path.join(base, 'event-service', 'src', 'main', 'java', 'com', 'campusiq', 'event', 'EventServiceApplication.java'), 'EventServiceApplication')
disable_amqp(os.path.join(base, 'notification-service', 'src', 'main', 'java', 'com', 'campusiq', 'notification', 'NotificationServiceApplication.java'), 'NotificationServiceApplication')

