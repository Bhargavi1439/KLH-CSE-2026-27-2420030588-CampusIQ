# **Campus IQ – Intelligent Resource Management for Smart Campuses**

 ## **Team Members**

2420030093	E. Mahathi 

2420030043	P. Pranathi

2420030588	Ch. Bhargavi Devi

2420090077	D. Krishna Chaitanya

### **Supervisor**

Dr G.Lavanya

### **Abstract**

CampusIQ is an adaptive software system designed to intelligently manage and optimize resources in smart campus environments. The system adapts to changing 
campus requirements, resource availability, user needs, and usage patterns through continuous monitoring and feedback. It supports dynamic allocation of 
classrooms, laboratories, equipment, faculty schedules, and other campus resources while identifying conflicts and improving utilization. The system follows 
adaptive software engineering principles, enabling iterative development, continuous improvement, and flexible response to changing requirements. By combining 
automation, data analysis, and adaptive decision-making, CampusIQ reduces resource wastage, improves operational efficiency, and provides a scalable solution 
for managing the evolving needs of modern educational institutions.

### **Setup Instructions**

**Clone the repository**

bash

git clone https://github.com/Bhargavi1439/KLH-CSE-2026-27-2420030588-CampusIQ.git

cd campus-iq

**Install dependencies**

Ensure Python 3.9+ is installed.

Install required packages:

bash

pip install -r requirements.txt

**Database setup**

Configure PostgreSQL/MySQL.

Update config/db_config.json with credentials.

Run migrations:

bash

python manage.py migrate

**Environment variables**

Create a .env file:

**Code**

SECRET_KEY=your_secret_key

DEBUG=True

DB_HOST=localhost

DB_USER=your_user

DB_PASSWORD=your_password

### **Execution Instructions**

**Start backend server**

bash

python manage.py runserver

**Launch frontend**

bash

cd frontend

npm install

npm start

### **Current Phase Status**

Phase 1: Requirement Analysis - Completed

Phase 2: System Design - In Progress

Phase 3: Prototype Development - In Progress

Phase 4: Testing & Validation - Pending

Phase 5: Deployment & Monitoring - Pending
