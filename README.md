
# 📱 QR Code Generator

A simple and modern QR Code Generator web application built using Python and Django. It allows users to generate QR codes from text, URLs, and other data through a clean and user-friendly interface.

## 🚀 Features

- Generate QR codes from text and URLs
- Simple and user-friendly interface
- Modern styling with CSS
- Fast QR code generation
- Download generated QR codes (if enabled in the application)
- Responsive web interface

## 🛠️ Technologies Used

- Python
- Django
- HTML5
- CSS3
- QR Code Library
- SQLite

## 📋 Requirements

- Python
- pip

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/prathamesh302008-ux/QR-code-generater.git
```

### 2. Open the Project Folder

```bash
cd QR-code-generater
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```cmd
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

### 8. Open in Your Browser

Visit:

http://127.0.0.1:8000/

## 📁 Project Structure

```text
QR-code-generater/
├── config/
│   ├── settings.py
│   └── urls.py
├── generator/
│   ├── templates/
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── templates/
├── static/
│   └── css/
│       └── style.css
├── manage.py
├── requirements.txt
└── README.md
```

## 🎯 Project Purpose

This project was developed to practice Python and Django web development, QR code generation, and frontend design.

## 👨‍💻 Author

**Prathamesh Patil**

GitHub: [@prathamesh302008-ux](https://github.com/prathamesh302008-ux)

## 📄 License

This project is intended for educational and learning purposes.
