# Information Management Project — Group 5 (2025-2026)

A ride-hailing system demo (inspired by Grab/Gojek) that showcases SQL Server business logic through Stored Procedures, Triggers, Functions, and Cursors via a Django web interface.

---

## Tech Stack

| Component | Technology |
|---|---|
| Backend | Django 6.0.5 |
| Database | Azure SQL Database (Microsoft SQL Azure 12.0) |
| DB Driver | pyodbc 5.3.0, mssql-django 1.7.1, ODBC Driver 18 |
| Frontend | Bootstrap 5 (Django Templates) |
| Python | 3.14.x |

---

## Prerequisites

- Python 3.10+
- [Microsoft ODBC Driver 18 for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)

**Install ODBC Driver on macOS:**
```bash
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew install msodbcsql18
```

**Install ODBC Driver on Ubuntu/Debian:**
```bash
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
```

---

## Project Structure

```
doan_qltt_2026_nhom5/
├── booking/            # Main app (views, urls)
├── config/             # Django settings, db config
├── templates/          # HTML templates (Django + Bootstrap 5)
├── static/             # Static CSS, JS
├── sql/                # SQL source files (schema, SP, triggers, functions, cursors, sample data)
├── venv/               # Python virtual environment
├── .env                # Environment variables — DO NOT commit or share publicly
├── .env.example        # Configuration template (no real credentials)
├── requirements.txt
└── manage.py
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone <repo-url>
cd doan_qltt_2026_nhom5
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Open `.env` and fill in the Azure SQL credentials — contact the team lead to obtain them:

```env
DB_NAME=<database name>
DB_USER=<username>
DB_PASSWORD=<password>
DB_HOST=<server>.database.windows.net
DB_PORT=1433

SECRET_KEY=<django secret key>
DEBUG=True
```

> `.env` is listed in `.gitignore` and must never be committed to the repository.

### 5. Run the development server

```bash
python manage.py migrate
python manage.py runserver
```

Open: **http://127.0.0.1:8000**

---

## Daily Usage (after initial setup)

```bash
source venv/bin/activate
python manage.py runserver
```

Open: **http://127.0.0.1:8000**

> No additional services need to be started — Azure SQL is always available on the cloud.

---

## Architecture

```
Browser
    ↓
Django Templates (HTML + Bootstrap 5)
    ↓
Django Views (Python — raw SQL, no ORM)
    ↓
Azure SQL Database
    ↓ (automatically)
Triggers / Functions / Cursors
```

All business logic (SPs, Triggers, Functions, Cursors) lives inside Azure SQL Database. Django only calls them and displays the results.

---

## Database

The database is hosted on **Azure SQL Database** with the following objects:

| Type | Count |
|---|---|
| Tables | 15 |
| Views | 7 |
| Stored Procedures | 7 |
| Functions | 4 |

SQL source files are stored in the `sql/` directory for version control and project submission.

---

## Demo Flow

Each feature is demonstrated in 5 steps:

| Step | Description |
|---|---|
| S1 | Business requirement explanation |
| S2 | Display the SQL / SP / Trigger to be executed |
| S3 | **BEFORE** data — loaded from Azure SQL |
| S4 | Execute button — makes a real call to Azure SQL |
| S5 | **AFTER** data — reloaded from Azure SQL |

---

## Troubleshooting

**ODBC Driver not found:**
```
django.db.utils.InterfaceError: ('IM002', ...)
```
→ Install ODBC Driver 18 as described in the Prerequisites section.

**Azure SQL connection error (timeout / firewall):**
```
django.db.utils.OperationalError: ('HYT00', ...)
```
→ Your IP address has not been whitelisted in the Azure Portal firewall rules. Contact the team lead to get access.

**Port 8000 already in use:**
```bash
python manage.py runserver 8080
# Open http://127.0.0.1:8080
```

---

## Group 5 — Information Management, UIT 2025-2026
