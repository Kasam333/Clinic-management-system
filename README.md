# Clinic Management System

<img width="946" alt="Screenshot 2025-01-26 235602" src="https://github.com/user-attachments/assets/9962fc90-33fe-4cbe-b5d5-be0ad17e4556" />

This is a **Django-based Clinic Management System** designed to streamline clinic operations. The project includes essential features such as user authentication, patient management, data visualization, and more. It uses **PostgreSQL** as the database and combines **HTML, CSS, and JavaScript** for a responsive and interactive frontend.

---

## 🚀 Features

### 🔐 **User Authentication**
- **Login** and **Register** functionality for doctors.
- **Reset Password** feature for enhanced security.
- **Logout** to ensure session security.

### 🩺 **Doctor Dashboard**
- A centralized interface for doctors to quickly access essential functionalities.

### 📝 **Quick Add Patient**
- Simplified form for adding new patients with minimal steps.

### 🗂️ **Manage Patients**
- **CRUD Operations**:
  - Add new patient records.
  - Update existing patient information.
  - Delete patient records.
  - Search for specific patients using filters.

### 📊 **Data Analytics**
- **Total Patients Analysis**:
  - Displays the total number of patients over time using **AJAXChart**.
- **Total Collection Chart**:
  - Visualizes the clinic's revenue over a selected time period.

### 💻 **Responsive UI**
- Intuitive user interface built with **HTML**, **CSS**, and **JavaScript**.

### 💾 **Database**
- Uses **PostgreSQL** to store patient data, user credentials, and analytics data.

---

## 🛠️ Technologies Used

### Backend
- **Python**
- **Django Framework**
- **PostgreSQL Database**

### Frontend
- **HTML5**
- **CSS3**
- **JavaScript**

### Libraries and Tools
- **AJAXChart**: For real-time chart rendering.
- **Django Authentication System**: For secure user management.
- **Bootstrap**: For responsive and modern UI design.

---
# 📸 Screenshots

## Index Page
<div align="center">
  <img src="https://github.com/user-attachments/assets/a617a5d8-25bf-4c5a-906f-1ed3ca820b77" alt="Index Page" width="400" />
</div>

---

## Login Page
<div align="center">
  <img src="https://github.com/user-attachments/assets/010f3a3a-5206-4fa6-a83e-f2464093c9ed" alt="Login Page 1" width="400" />
  <img src="https://github.com/user-attachments/assets/c1d55b05-e5d1-4daf-9140-18c322acff0b" alt="Login Page 2" width="400" />
</div>

---

## Dashboard
<div align="center">
  <img src="https://github.com/user-attachments/assets/677a0eda-594b-4bf7-8e1f-3528e9f53f59" alt="Dashboard" width="400" />
</div>

---

## Quick Add Patient
<div align="center">
  <img src="https://github.com/user-attachments/assets/26fd6d30-924c-4b28-9196-21f119a8c282" alt="Quick Add Patient" width="450" />
</div>

---

## Patient Management
<div align="center">
  <img src="https://github.com/user-attachments/assets/c864fc2f-1819-4398-9602-44428534eacf" alt="Patient Management 1" width="450" />
  <img src="https://github.com/user-attachments/assets/954cd9d5-14bb-40a0-ad74-e87e3a28155c" alt="Patient Management 2" width="450" />
  <img src="https://github.com/user-attachments/assets/f6eb4a75-d955-4502-9112-97acad380865" alt="Patient Management 3" width="450" />
  <img src="https://github.com/user-attachments/assets/1e871bef-869a-4c71-9c72-066cac491ad2" alt="Patient Management 4" width="450" />
</div>

---

## Data Analysis Charts - Total Patients
<div align="center">
  <img src="https://github.com/user-attachments/assets/3bf95a12-9492-463f-aaf8-f516ebf7298a" alt="Total Patients 1" width="500" />
  <img src="https://github.com/user-attachments/assets/8ec807d8-bc43-4ea8-a816-24b8177cc563" alt="Total Patients 2" width="500" />
  <img src="https://github.com/user-attachments/assets/15d45a07-8685-4bee-9dbd-25b8f5d515a5" alt="Total Patients 3" width="500" />
</div>

---

## Data Analysis Charts - Total Amount Collection
<div align="center">
  <img src="https://github.com/user-attachments/assets/404927f7-b400-4cb8-95e3-6a0314218155" alt="Total Amount Collection" width="500" />
</div>

---

## Reset Password
<div align="center">
  <img src="https://github.com/user-attachments/assets/bef629b6-c414-4b08-a3bb-5b2aa6eb89cc" alt="Reset Password" width="500" />
</div>


## 🛠️ Installation

### Prerequisites
- Python (>=3.8)
- PostgreSQL
- pip (Python package manager)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/clinic-management-system.git
   cd clinic-management-system
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**:
   - Update the `DATABASES` settings in `settings.py` with your PostgreSQL credentials.

5. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/`.

---

## 🌟 Future Enhancements
- Add appointment scheduling feature.
- Enable multi-language support.
- Add patient billing and invoice generation.
- Implement email and SMS notifications.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact
For any questions or feedback, feel free to contact:
- **Name**: Your Name
- **Email**: your.email@example.com
- **GitHub**: [Your GitHub Profile](https://github.com/yourusername)

