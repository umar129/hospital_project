# Hospital Management System - Setup & Usage Guide

## Setup Instructions

### 1. Install Django REST Framework
```bash
pip install djangorestframework
```

### 2. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Admin User (if needed)
```bash
python manage.py createsuperuser
```

### 4. Run Development Server
```bash
python manage.py runserver
```

---

## API Endpoints

### List & Create Patients
- **GET** `/patients/api/patients/` - Get all patients
- **POST** `/patients/api/patients/` - Create a new patient

**POST Request Example:**
```json
{
  "name": "John Doe",
  "age": 30,
  "mobile": "1234567890",
  "email": "john@example.com",
  "address": "123 Main St",
  "doctor_id": 1
}
```

### Get, Update, Delete Patient
- **GET** `/patients/api/patients/{id}/` - Get patient by ID
- **PUT** `/patients/api/patients/{id}/` - Update patient
- **DELETE** `/patients/api/patients/{id}/` - Delete patient

### List & Create Doctors
- **GET** `/doctors/api/doctors/` - Get all doctors
- **POST** `/doctors/api/doctors/` - Create a new doctor

**POST Request Example:**
```json
{
  "name": "Dr. Ahmed Khan",
  "department_id": 1,
  "salary": 150000
}
```

### Get, Update, Delete Doctor
- **GET** `/doctors/api/doctors/{id}/` - Get doctor by ID
- **PUT** `/doctors/api/doctors/{id}/` - Update doctor
- **DELETE** `/doctors/api/doctors/{id}/` - Delete doctor

---

## Web Interface URLs

### Patient Management
- **Home** - `/patients/` - View all patients
- **Create Patient** - `/patients/create/` - Add new patient
- **View Patient** - `/patients/{id}/detail/` - View patient details
- **Edit Patient** - `/patients/{id}/update/` - Update patient information
- **Delete Patient** - `/patients/{id}/delete/` - Delete patient

### Doctor & Department Management
- **View Doctors** - `/doctors/` - View all doctors and manage them
- **Create Doctor** - `/doctors/create/` - Add new doctor
- **View Doctor** - `/doctors/{id}/detail/` - View doctor details
- **Edit Doctor** - `/doctors/{id}/update/` - Update doctor information
- **Delete Doctor** - `/doctors/{id}/delete/` - Delete doctor

### Admin Panel
- **Admin Panel** - `/admin/` - Django admin interface with Patients, Doctors, and Departments management

---

## Model Structure

### Patients Model
- `id` - Auto-generated primary key
- `name` - Patient's full name (CharField)
- `age` - Patient's age (IntegerField)
- `address` - Patient's address (TextField)
- `mobile` - Mobile number, 10 digits (CharField)
- `email` - Email address (CharField)
- `doctor` - ForeignKey to Doctor (optional)

### Doctors Model
- `id` - Auto-generated primary key
- `name` - Doctor's name (CharField)
- `department` - ForeignKey to Departments
- `joining_date` - Joining date (DateTimeField)
- `salary` - Monthly salary (IntegerField)

### Departments Model
- `id` - Auto-generated primary key
- `dep_name` - Department name (CharField with fixed choices)
  - Cardiology
  - Neurology
  - Orthopedics
  - Pediatrics
  - Dermatology
  - General

---

## Validation Rules

### Patient Data Validation
✅ **Age**: Must be between 1-150  
✅ **Mobile**: Must be exactly 10 digits  
✅ **Email**: Must be valid email format  
✅ **Name**: Required, max 64 characters  
✅ **Doctor**: Optional, can be assigned/updated anytime  

---

## Django Admin Features

### Patients Admin
- Search by name, email, or mobile
- Filter by age and assigned doctor
- Sort by ID (latest first)
- Quick edit and delete functionality

### Doctors Admin
- Search by doctor name
- Filter by department and joining date
- View salary information
- Easy assignment to patients

### Departments Admin
- View all available departments
- Manage department list

---

## HTML Templates

### Patient List (`patient_list.html`)
- Displays all patients in a table format
- Shows total patient count
- Quick actions: View, Edit, Delete
- Links to doctor management

### Patient Form (`patient_form.html`)
- Form to create new patient or edit existing
- Input validation on frontend
- Error messages display
- Doctor assignment dropdown

### Patient Detail (`patient_detail.html`)
- Shows complete patient information
- Displays assigned doctor details
- Edit and delete options
- Links to patient list

### Patient Delete Confirmation (`patient_confirm_delete.html`)
- Confirmation dialog before deletion
- Shows patient details
- Safety warning message

### Doctor & Department List (`doctor_list.html`)
- Shows all doctors with their departments
- Department cards with color coding
- Doctor cards with joining date and salary
- Total count of doctors
- Link back to patients

### Doctor Management Templates (`doctor_form.html`, `doctor_detail.html`, `doctor_confirm_delete.html`)
- Create and update doctors with full details
- View individual doctor information
- Safe deletion with confirmation
- Department assignment interface

---

## Features

✨ **Complete CRUD Operations**
- Create, Read, Update, Delete patients and doctors via web or API

✨ **REST API**
- Full API endpoints for patients and doctors
- JSON request/response format
- Easy integration with external systems

✨ **Data Validation**
- Server-side validation using Django serializers
- Patient: Email, phone (10 digits), age (1-150)
- Doctor: Name (min 3 chars), salary (> 0)

✨ **Doctor Assignment**
- Assign doctors to patients
- View doctor information on patient detail page
- Manage doctors independently

✨ **Beautiful UI**
- Responsive design
- Gradient backgrounds
- Color-coded buttons and cards
- Clean and intuitive interface

✨ **Admin Panel**
- Full Django admin integration
- Search and filter capabilities
- Customized field display

---

## Example API Usage with cURL

### Create a Patient
```bash
curl -X POST http://localhost:8000/patients/api/patients/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith",
    "age": 28,
    "mobile": "9876543210",
    "email": "jane@example.com",
    "address": "456 Oak Ave",
    "doctor_id": 1
  }'
```

### Get All Patients
```bash
curl http://localhost:8000/patients/api/patients/
```

### Get Single Patient
```bash
curl http://localhost:8000/patients/api/patients/1/
```

### Update a Patient
```bash
curl -X PUT http://localhost:8000/patients/api/patients/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith Updated",
    "age": 29,
    "mobile": "9876543210",
    "email": "jane.updated@example.com",
    "address": "789 Pine Rd",
    "doctor_id": 2
  }'
```

### Delete a Patient
```bash
curl -X DELETE http://localhost:8000/patients/api/patients/1/
```

### Create a Doctor
```bash
curl -X POST http://localhost:8000/doctors/api/doctors/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Dr. Ahmed Khan",
    "department_id": 1,
    "salary": 150000
  }'
```

### Get All Doctors
```bash
curl http://localhost:8000/doctors/api/doctors/
```

### Get Single Doctor
```bash
curl http://localhost:8000/doctors/api/doctors/1/
```

### Update a Doctor
```bash
curl -X PUT http://localhost:8000/doctors/api/doctors/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Dr. Ahmed Khan Updated",
    "department_id": 2,
    "salary": 160000
  }'
```

### Delete a Doctor
```bash
curl -X DELETE http://localhost:8000/doctors/api/doctors/1/
```

---

## Troubleshooting

**Q: Templates not found?**  
A: Make sure `APP_DIRS` is True in settings.py and templates are in the correct directory structure.

**Q: API returns 404?**  
A: Ensure urls.py is properly configured and included in the main project urls.

**Q: SyntaxError with migrations?**  
A: Run `python manage.py makemigrations` before `python manage.py migrate`.

**Q: Doctor not showing up in dropdown?**  
A: Make sure doctors are created in the admin panel first.

---

## Notes

- All dates are stored in UTC
- Mobile numbers must be exactly 10 digits
- Email validation is performed both client-side and server-side
- Doctor field is optional; patients can exist without a doctor assignment
