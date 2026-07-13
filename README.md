# 🚀 QR Code Generator & Scanner

<p align="center">
  A Full-Stack Django web application for generating, scanning, and managing QR Codes.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Django-Framework-darkgreen?style=for-the-badge&logo=django">
  <img src="https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap">
  <img src="https://img.shields.io/badge/PostgreSQL-Neon-blue?style=for-the-badge&logo=postgresql">
  <img src="https://img.shields.io/badge/Vercel-Deployed-black?style=for-the-badge&logo=vercel">
</p>

---

## 📖 About The Project

QR Code Generator & Scanner is a **Full-Stack Web Application** built using **Python** and **Django**.

The application allows users to create QR codes instantly, scan existing QR codes, and manage their profiles through a clean and responsive interface. It integrates a cloud-hosted **Neon PostgreSQL** database and is deployed on **Vercel**, providing a production-ready environment.

This project was developed to strengthen my understanding of:

- Full-Stack Web Development
- Django Framework
- Authentication System
- Database Integration
- QR Code Processing
- Cloud Deployment
- Responsive UI Design

---

# ✨ Features

- 🔐 User Registration & Login
- 👤 User Profile Management
- 📱 Generate QR Codes
- 🔍 Scan & Decode QR Codes
- 💾 Secure Database Storage
- ☁️ Neon PostgreSQL Database
- 🚀 Live Deployment on Vercel
- 📱 Fully Responsive Design

---

# 🛠 Tech Stack

### Backend
- Python
- Django

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 5

### Database
- Neon PostgreSQL

### Deployment
- Vercel

---

# 📦 Python Libraries

- Django
- qrcode
- Pillow
- pyzbar
- NumPy

---

# 📁 Project Structure

```text
django_qr_code/
│
├── django_qr/
│   ├── migrations/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── forms.py
│   ├── models.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── media/
│
├── templates/
│   ├── base.html
│   ├── generate_qr_code.html
│   ├── login.html
│   ├── profile.html
│   ├── qr_result.html
│   └── signup.html
│
├── .gitignore
├── db.sqlite3
├── manage.py
├── requirements.txt
├── vercel.json
└── README.md
```

---

# ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/abdullah-tahir-asif/django_qr_code.git
```

### Navigate into the project

```bash
cd django_qr_code
```

### Create a Virtual Environment

#### Windows

```bash
python -m venv env
env\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv env
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Database Migrations

```bash
python manage.py migrate
```

### Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit

```
http://127.0.0.1:8000/
```

---

# 🚀 Deployment

This project is deployed on **Vercel** using:

- Vercel Hosting
- Neon PostgreSQL Database

---

# 📸 Screenshots

> Add screenshots of your application here.

Example:

```
screenshots/
    home.png
    login.png
    profile.png
    generate.png
```

Then display them like this:

```md
## Home Page

![Home](screenshots/home.png)

## Generate QR

![Generate](screenshots/generate.png)
```

---

# 🎯 Future Improvements

- 📂 QR History
- ❤️ Favorite QR Codes
- 📤 Download QR in Multiple Formats
- 🌙 Dark Mode
- 📊 User Dashboard
- 📱 Progressive Web App (PWA)

---

# 🤝 Contributing

Contributions are always welcome.

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 👨‍💻 Author

### Abdullah Tahir

GitHub:
https://github.com/abdullah-tahir-asif

LinkedIn:
(Add your LinkedIn URL here)

---

# ⭐ Show Your Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates me to build more open-source applications.

---

## 📄 License

This project is licensed under the MIT License.
