# 🍽️ Restaurant Management System

## 📌 Project Overview
The **Restaurant Management System** is a web application built using Django that allows restaurant managers and staff to efficiently handle orders, manage menu items, and generate receipts.

## 👥 Team
- **Developer:** [Your Name]
- **Contributors:** [If applicable]

## 🏗️ Architecture & Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Bootstrap)
- **Database:** SQLite (Default Django DB)
- **Authentication:** Django's built-in authentication system

## 🔧 Features

### 🔹 **Manager Features**
- ✅ Add and update menu items
- ✅ View all orders
- ✅ Update order status (Pending, In Progress, Completed, Cancelled)
- ✅ Generate receipts for completed orders

### 🔹 **Staff Features**
- ✅ Place new orders
- ✅ View orders they have created
- ✅ Print receipts for completed orders

## 🚀 Installation & Setup

### 📥 Clone the Repository
```sh
git clone https://github.com/yourusername/restaurant-management.git
cd restaurant-management
```

### 🛠️ Install Dependencies
```sh
pip install -r requirements.txt
```

### 🔑 Run Migrations & Create Superuser
```sh
python manage.py migrate
python manage.py createsuperuser  # Follow the prompts
```

### ▶️ Start the Server
```sh
python manage.py runserver
```
Open `http://127.0.0.1:8000/` in your browser.

## 🎯 Development Report

### ✅ **Successes**
- Successfully built an authentication system for managers and staff.
- Implemented an intuitive dashboard for easy navigation.
- Orders and menu items are stored and retrieved efficiently.

### ⚠️ **Challenges**
- Initial issues with URL configurations and template rendering.
- Ensuring role-based access control for managers and staff.

### 🔄 **Areas for Improvement**
- Implement API endpoints for mobile app integration.
- Enhance the UI for a more modern experience.

## 🎓 Lessons Learned & Next Steps
- Improved understanding of Django models and views.
- Better handling of user authentication and permissions.
- Future improvements: **Add reports & analytics**, **expand to multiple restaurant branches**.

## 📜 License
This project is licensed under the MIT License.

---

🚀 **Developed with Django & ❤️ by [Your Name]**
