# 🛒 E-Commerce Management System

A full-featured E-Commerce Management System built with **Python** and **Django**. This project includes product management, user authentication, shopping cart, order processing, and an admin dashboard.


---

## ✨ Features

- 🔐 **User Authentication** — Register, Login, Logout with session management
- 📦 **Product Management** — Add, update, delete products with categories
- 🛒 **Shopping Cart** — Add/remove items, update quantities
- 📋 **Order Management** — Place orders, view order history
- 🖥️ **Admin Dashboard** — Manage products, users, and orders via Django Admin
- 📱 **Responsive Design** — Works on desktop and mobile

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python 3.x | Backend language |
| Django | Web framework |
| SQLite | Database (default) |
| HTML/CSS | Frontend templates |
| Bootstrap | UI styling |
| Vercel | Deployment |

---

## 🚀 Getting Started (Local Setup)

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Khuzama-arshad/E-commerce-management-system.git
   cd E-commerce-management-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (Admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open in browser**
   ```
   http://127.0.0.1:8000/
   ```
   Admin panel: `http://127.0.0.1:8000/admin/`

---

## 📁 Project Structure

```
E-commerce-management-system/
│
├── management_system/        # Main Django project folder
│   ├── settings.py           # Project settings
│   ├── urls.py               # URL routing
│   └── wsgi.py               # WSGI config
│
├── requirements.txt          # Python dependencies
├── manage.py                 # Django management script
└── README.md
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 👩‍💻 Author

**Khuzama Arshad**
- GitHub: [@Khuzama-arshad](https://github.com/Khuzama-arshad)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
