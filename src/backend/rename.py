import os

base = r'C:\Users\krish\.gemini\antigravity-ide\scratch\CampusIQ-AI\backend\notification-service\src\main\java\com\campusiq\notification'

model_dir = os.path.join(base, 'model')
repo_dir = os.path.join(base, 'repository')
controller_dir = os.path.join(base, 'controller')

# rename model
os.rename(os.path.join(model_dir, 'MaintenanceRequest.java'), os.path.join(model_dir, 'Notification.java'))

# rename repo
os.rename(os.path.join(repo_dir, 'MaintenanceRequestRepository.java'), os.path.join(repo_dir, 'NotificationRepository.java'))

# rename controller
os.rename(os.path.join(controller_dir, 'InfrastructureController.java'), os.path.join(controller_dir, 'NotificationController.java'))
