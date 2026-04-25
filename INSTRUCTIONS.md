# Healthcare Backend API - Setup & Run Instructions

## 📋 Project Overview
A Django REST API for healthcare management with:
- User authentication (JWT)
- Patient management
- Doctor management
- Patient-Doctor assignments
- PostgreSQL database
- Environment variables for sensitive data

---

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Setup Database
```bash
psql -U postgres
CREATE USER healthcare_user WITH PASSWORD 'harsh';
CREATE DATABASE healthcare_db OWNER healthcare_user;
GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO healthcare_user;
\q
```

### Step 3: Run Server
```bash
py manage.py migrate
py manage.py runserver
```

**Server running at:** `http://127.0.0.1:8000/`

---

## 📝 Testing with Postman

### 1. Register User
**URL:** `POST http://127.0.0.1:8000/api/auth/register/`

**Body (JSON):**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}
```

**Expected Response:**
```json
{"message": "User registered successfully"}
```

---

### 2. Login User (Get JWT Token)
**URL:** `POST http://127.0.0.1:8000/api/auth/login/`

**Body (JSON):**
```json
{
  "username": "john@example.com",
  "password": "password123"
}
```

**Expected Response:**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**⚠️ IMPORTANT:** Copy the `access` token - you'll need it for all other requests!

---

### 3. Create Patient (Authenticated)
**URL:** `POST http://127.0.0.1:8000/api/patients/`

**Headers:**
- Key: `Authorization`
- Value: `Bearer YOUR_ACCESS_TOKEN` (replace YOUR_ACCESS_TOKEN)

**Body (JSON):**
```json
{
  "name": "Jane Smith",
  "email": "jane@example.com",
  "phone": "9876543210",
  "date_of_birth": "1995-05-20",
  "address": "456 Oak Street, City",
  "medical_history": "Diabetes, Hypertension"
}
```

**Expected Response:** Patient object with ID

---

### 4. Get All Patients
**URL:** `GET http://127.0.0.1:8000/api/patients/`

**Headers:**
- Key: `Authorization`
- Value: `Bearer YOUR_ACCESS_TOKEN`

**Expected Response:** List of patients created by logged-in user

---

### 5. Get Patient Details
**URL:** `GET http://127.0.0.1:8000/api/patients/1/`

**Headers:**
- Key: `Authorization`
- Value: `Bearer YOUR_ACCESS_TOKEN`

**Expected Response:** Single patient details

---

### 6. Update Patient
**URL:** `PUT http://127.0.0.1:8000/api/patients/1/`

**Headers:**
- Key: `Authorization`
- Value: `Bearer YOUR_ACCESS_TOKEN`

**Body (JSON):**
```json
{
  "medical_history": "Updated medical history"
}
```

---

### 7. Delete Patient
**URL:** `DELETE http://127.0.0.1:8000/api/patients/1/`

**Headers:**
- Key: `Authorization`
- Value: `Bearer YOUR_ACCESS_TOKEN`

---

### 8. Create Doctor
**URL:** `POST http://127.0.0.1:8000/api/doctors/`

**Headers:**
- Key: `Authorization`
- Value: `Bearer YOUR_ACCESS_TOKEN`

**Body (JSON):**
```json
{
  "name": "Dr. Smith",
  "email": "dr.smith@hospital.com",
  "phone": "9876543210",
  "specialization": "Cardiologist",
  "license_number": "DOC123456"
}
```

---

### 9. Get All Doctors
**URL:** `GET http://127.0.0.1:8000/api/doctors/`

**Headers:**
- Key: `Authorization`
- Value: `Bearer YOUR_ACCESS_TOKEN`

---

### 10. Assign Doctor to Patient (Create Mapping)
**URL:** `POST http://127.0.0.1:8000/api/mappings/`

**Headers:**
- Key: `Authorization`
- Value: `Bearer YOUR_ACCESS_TOKEN`

**Body (JSON):**
```json
{
  "patient": 1,
  "doctor": 1
}
```

---

### 11. Get All Mappings
**URL:** `GET http://127.0.0.1:8000/api/mappings/`

**Headers:**
- Key: `Authorization`
- Value: `Bearer YOUR_ACCESS_TOKEN`

---

### 12. Get Doctors for Specific Patient
**URL:** `GET http://127.0.0.1:8000/api/mappings/patient/1/`

**Headers:**
- Key: `Authorization`
- Value: `Bearer YOUR_ACCESS_TOKEN`

---

### 13. Delete Mapping
**URL:** `DELETE http://127.0.0.1:8000/api/mappings/1/`

**Headers:**
- Key: `Authorization`
- Value: `Bearer YOUR_ACCESS_TOKEN`

---

## 🔑 Environment Variables (.env)

The `.env` file contains:
```
SECRET_KEY=django-insecure-your-secret-key-here-change-in-production
DEBUG=True
DB_ENGINE=django.db.backends.postgresql
DB_NAME=healthcare_db
DB_USER=healthcare_user
DB_PASSWORD=harsh
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=127.0.0.1,localhost
```

---

## 📁 Project Structure

```
healthcare_backend/
├── api/
│   ├── migrations/
│   ├── models.py          (Patient, Doctor, PatientDoctorMapping)
│   ├── views.py           (API views)
│   ├── serializers.py     (Serializers)
│   ├── urls.py            (API endpoints)
│   └── admin.py
├── healthcare_backend/
│   ├── settings.py        (Django settings)
│   ├── urls.py            (Main URLs)
│   └── wsgi.py
├── .env                   (Environment variables)
├── .gitignore
├── manage.py
├── requirements.txt       (Dependencies)
├── db.sqlite3            (SQLite DB - optional)
└── README.md
```

---

## 🛠️ Troubleshooting

**Error: "No such file or directory" (psql)**
- PostgreSQL not installed or not in PATH
- Install from: https://www.postgresql.org/download/windows/

**Error: "database does not exist"**
- Create the database first using psql commands above

**Error: "No active account found with the given credentials"**
- Email/password mismatch
- Register first, then login with same credentials

**Error: "Permission denied" on migrations**
- Make sure .env file is in the correct location
- Verify DB credentials match

---

## ✅ Verification Checklist

- [ ] PostgreSQL installed and running
- [ ] `requirements.txt` installed
- [ ] Database created
- [ ] Migrations applied (`py manage.py migrate`)
- [ ] Server running (`py manage.py runserver`)
- [ ] Can register user
- [ ] Can login and get token
- [ ] Can create patients
- [ ] Can create doctors
- [ ] Can create mappings

---

## 📚 API Endpoints Summary

| Method | Endpoint | Authentication | Description |
|--------|----------|-----------------|-------------|
| POST | /api/auth/register/ | No | Register new user |
| POST | /api/auth/login/ | No | Login & get JWT |
| POST | /api/patients/ | Yes | Create patient |
| GET | /api/patients/ | Yes | List user's patients |
| GET | /api/patients/<id>/ | Yes | Get patient details |
| PUT | /api/patients/<id>/ | Yes | Update patient |
| DELETE | /api/patients/<id>/ | Yes | Delete patient |
| POST | /api/doctors/ | Yes | Create doctor |
| GET | /api/doctors/ | Yes | List all doctors |
| GET | /api/doctors/<id>/ | Yes | Get doctor details |
| PUT | /api/doctors/<id>/ | Yes | Update doctor |
| DELETE | /api/doctors/<id>/ | Yes | Delete doctor |
| POST | /api/mappings/ | Yes | Assign doctor to patient |
| GET | /api/mappings/ | Yes | List all mappings |
| GET | /api/mappings/patient/<id>/ | Yes | Get doctors for patient |
| DELETE | /api/mappings/<id>/ | Yes | Remove mapping |

---

## 🔐 Authentication

All endpoints (except register/login) require JWT token in headers:
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

The token is obtained from the `/api/auth/login/` endpoint.

---

## 📞 Support
If you encounter any issues:
1. Check PostgreSQL is running
2. Verify database credentials in `.env`
3. Ensure Python 3.12+ is installed
4. Check `requirements.txt` is fully installed

Happy Testing! 🚀
