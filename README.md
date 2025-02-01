# FAQ Backend - Django API

## 📌 Introduction
This is a Django-based FAQ management system that supports multilingual translations and provides a REST API for managing FAQs efficiently. It includes:
- WYSIWYG editor integration (django-ckeditor)
- Multi-language translation using Google Translate API
- Caching mechanism using Redis
- Django admin panel for managing FAQs
- Unit tests for API and model validation

---

## 🚀 Features
- **FAQ Model**: Stores questions, answers, and translations.
- **WYSIWYG Editor**: Rich text formatting for FAQ answers.
- **REST API**: Retrieve, create, update, and delete FAQs.
- **Caching**: Speeds up translations using Redis.
- **Multi-language Support**: Supports Hindi, Bengali, and more.
- **Admin Panel**: Manage FAQs from Django admin.
- **Unit Testing**: Ensures API correctness and reliability.

---

## ⚙️ Installation

### Prerequisites
- Python 3.8+
- Django 4+
- Redis (for caching)
- Virtual environment (recommended)

### Step 1: Clone the Repository
```sh
git clone https://github.com/jayantgoyal1502/faq-backend.git
cd faq-backend
```

### Step 2: Create and Activate Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 4: Apply Migrations
```sh
python manage.py migrate
```

### Step 5: Run Development Server
```sh
python manage.py runserver
```

### Step 6: Start Redis Server (For Caching)
```sh
redis-server
```

---

## 📌 API Endpoints

### **1. Get All FAQs (Default: English)**
```sh
GET /api/faqs/
```
Example Response:
```json
[
    {
        "id": 1,
        "question": "What is Django?",
        "answer": "Django is a Python framework for web development."
    }
]
```

### **2. Get FAQs in Specific Language**
```sh
GET /api/faqs/?lang=hi
```
Example Response (Hindi):
```json
[
    {
        "id": 1,
        "question": "Django क्या है?",
        "answer": "Django एक Python फ्रेमवर्क है।"
    }
]
```

### **3. Create a New FAQ**
```sh
POST /api/faqs/
```
Request Body:
```json
{
    "question": "What is Redis?",
    "answer": "Redis is an in-memory database.",
    "language": "en"
}
```

### **4. Update an FAQ**
```sh
PUT /api/faqs/{id}/
```
Request Body:
```json
{
    "question": "What is Redis?",
    "answer": "Redis is a fast in-memory key-value store."
}
```

### **5. Delete an FAQ**
```sh
DELETE /api/faqs/{id}/
```

---

## 🧪 Running Tests
To run unit tests, use:
```sh
pytest
```

---

## 🔥 Caching
This project uses **Redis** for caching translations and FAQ retrieval. Ensure Redis is running before testing.

---

## 🛠️ Admin Panel
Access the Django admin panel at:
```
http://127.0.0.1:8000/admin/
```
To create a superuser:
```sh
python manage.py createsuperuser
```

---

## 📜 Git Commit Message Guidelines
Follow conventional commit messages:
- `feat: Add multilingual FAQ model`
- `fix: Improve translation caching`
- `docs: Update README with API examples`
- `test: Add unit tests for FAQ API`

---

## 👥 Contribution Guidelines
1. Fork the repository.
2. Clone the forked repo:
   ```sh
   git clone https://github.com/your-username/faq-backend.git
   ```
3. Create a new branch:
   ```sh
   git checkout -b feature-branch
   ```
4. Make your changes and commit:
   ```sh
   git commit -m "feat: Add new API endpoint"
   ```
5. Push changes:
   ```sh
   git push origin feature-branch
   ```
6. Open a pull request.

---

## 📌 Deployment (Docker Optional)
To run the project with Docker:
```sh
docker-compose up --build
```

---

✅ **Now you're ready to use the FAQ Backend API! 🚀**
