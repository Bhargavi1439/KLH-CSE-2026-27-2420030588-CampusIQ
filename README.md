# **Campus IQ – Intelligent Resource Management for Smart Campuses**

 ## **Team Members**

2420030093	E. Mahathi 

2420030043	P. Pranathi

2420030588	Ch. Bhargavi Devi

2420090077	D. Krishna Chaitanya

### **Supervisor**

Dr G.Lavanya

### **Abstract**

Campus IQ – Intelligent Resource Management for Smart Campuses is a smart campus management system developed to improve the way educational institutions manage and utilize their available resources. A college campus consists of many resources such as classrooms, laboratories, computers, equipment, electricity, library facilities, and other infrastructure. Managing these resources manually can be difficult when there are many students, faculty members, departments, and activities taking place simultaneously. This can lead to problems such as unused classrooms, overcrowded laboratories, inefficient equipment usage, unnecessary energy consumption, and difficulty in tracking resource availability. Campus IQ aims to address these problems by combining Artificial Intelligence (AI), databases, and data analysis. The system collects information related to resource availability, occupancy, usage time, equipment usage, and energy consumption. This information can be collected using existing campus systems, or manual inputs. The collected data is stored in a database, where it can be organized and processed for further analysis. AI and data analysis can help identify resources that are frequently used, underused, or overused. Based on these patterns, Campus IQ can provide useful recommendations to administrators. For example, if a classroom remains unused during specific hours, the system can suggest assigning it to another class or activity. If one laboratory is overcrowded while another is available, the system can recommend a better allocation of students. The system can also monitor energy usage and identify unusual or unnecessary consumption. Campus IQ includes an administrator dashboard that provides information about resource availability, occupancy, usage statistics, energy consumption, alerts, reports, and AI-based recommendations. This dashboard helps administrators monitor campus resources from a single platform and reduces the need for manual checking. By using real-time or regularly updated data, administrators can make better decisions about resource allocation and campus operations. The main goal of Campus IQ is to reduce resource wastage, improve resource utilization, save energy and costs, and reduce manual work. The system can benefit students, faculty, and administrators by making campus resources easier to monitor and manage. In the future, the system can be extended with real-time IoT monitoring, automatic classroom allocation, predictive maintenance of equipment, smart energy control, mobile applications, and AI-based campus assistants. Overall, Campus IQ provides a practical approach to creating a smarter, more efficient, organized, and sustainable campus environment by using technology to make better use of the resources that are already available.

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
