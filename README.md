# ✈️ Flight Routes System (Django)

## 📌 Overview
This project is a Django-based Flight Routes System that allows users to manage airport routes and perform graph-based operations like finding Nth node, longest route, and shortest path.

---

## 🚀 Features

### 🔹 Airport Management (CRUD)
- Add Airport
- View Airport List
- Edit Airport
- Delete Airport

### 🔹 Route Management
- Add Airport Routes (Parent, Child, Position, Duration)

### 🔹 Functionalities

1. **Find Nth Node**
   - Traverse Left/Right from a starting airport
   - Returns the Nth node

2. **Longest Route**
   - Displays route with maximum duration

3. **Shortest Path**
   - Uses Dijkstra Algorithm
   - Finds shortest distance between two airports

---

## 🛠️ Tech Stack
- Python
- Django
- SQLite
- HTML, CSS
- SweetAlert (UI Alerts)

---

## ⚙️ Installation

```bash
git clone https://github.com/sadhik-ali/Flight-Routes-System.git
cd Flight-Routes-System
````

### Create Virtual Environment

```bash
python -m venv env
source env/bin/activate   # Windows: env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

---

## 🌐 URLs

| Feature       | URL         |
| ------------- | ----------- |
| Home          | /           |
| Add Route     | /add-route/ |
| Nth Node      | /nth-node/  |
| Longest Route | /longest/   |
| Shortest Path | /shortest/  |
| Airports      | /airports/  |

---

## 🧪 Sample Data

Airports:

* DXB, MAA, DEL, BLR

Routes:

* DXB → MAA (3000)
* DXB → DEL (2500)
* MAA → BLR (350)

---

## 📌 Author

Sadhik Ali
Python Django Developer

````

