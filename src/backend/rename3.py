import os

base = r'C:\Users\krish\.gemini\antigravity-ide\scratch\CampusIQ-AI\backend\notification-service\src\main\java\com\campusiq\notification'

entity_dir = os.path.join(base, 'entity')
repo_dir = os.path.join(base, 'repository')
controller_dir = os.path.join(base, 'controller')

# rename entity
os.rename(os.path.join(entity_dir, 'Infrastructure.java'), os.path.join(entity_dir, 'Notification.java'))

# rename repo
os.rename(os.path.join(repo_dir, 'InfrastructureRepository.java'), os.path.join(repo_dir, 'NotificationRepository.java'))

# rename controller
os.rename(os.path.join(controller_dir, 'InfrastructureController.java'), os.path.join(controller_dir, 'NotificationController.java'))

# Replace text in java files
for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.java'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            content = content.replace('Infrastructure', 'Notification')
            content = content.replace('infrastructure', 'notification')
            content = content.replace('/notifications/requests', '/notifications')
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

