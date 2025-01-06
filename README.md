🍽️ Restaurant Management System
📌 Overview
The Restaurant Management System is a web application built with Django to help restaurants manage their operations efficiently. It provides a manager dashboard for overseeing orders and menu items and a staff dashboard for placing and tracking orders.

🛠 Features

✅ User authentication (Login, Logout, Signup)
✅ Role-based access control (Managers & Staff)
✅ Order management (Create, Update, Cancel Orders)
✅ Menu management (Managers can add menu items)
✅ Receipt generation for completed orders


🏗️ Technologies Used
Backend: Django (Python)
Frontend: Bootstrap, HTML, CSS
Database: SQLite (Can be switched to PostgreSQL)
Authentication: Django's built-in user system
Deployment: Optional (e.g., Heroku, Render)
🚀 Installation & Setup
🔹 Step 1: Clone the Repository
sh
Copy code
git clone https://github.com/ImanimK/Restaurant-Management-System.git
cd restaurant_management
🔹 Step 2: Set Up a Virtual Environment
sh
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
🔹 Step 3: Install Dependencies
sh
Copy code
pip install -r requirements.txt
🔹 Step 4: Apply Migrations
sh
Copy code
python manage.py migrate
🔹 Step 5: Create a Superuser
sh
Copy code
python manage.py createsuperuser
🔹 Step 6: Run the Development Server
sh
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

📜 Project Structure
csharp
Copy code
restaurant_management/
│── restaurant/                 # Django app
│   ├── templates/              # HTML Templates
│   ├── static/                 # CSS, JavaScript, Images
│   ├── models.py               # Database Models
│   ├── views.py                # View Functions
│   ├── forms.py                # Django Forms
│   ├── urls.py                 # URL Routing
│── static/                      # Static Assets
│── db.sqlite3                    # Database
│── manage.py                     # Django Management Script
│── requirements.txt               # Dependencies
│── README.md                      # Project Documentation
🛠️ Usage Guide
Manager:

Log in as a manager
Manage menu items
View and update order status
Staff:

Log in as staff
Place orders
View receipts


📌 Future Enhancements
🔹 Mobile responsiveness
🔹 Table booking system
🔹 Advanced reporting and analytics

👨‍💻 Contributors
[Imani Kingsley] - Lead Developer

