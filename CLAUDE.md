# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Tổng quan

Đồ án môn Quản lý Thông tin / HQTCSDL — mô phỏng hệ thống đặt xe (Grab/Gojek).

Website là **presentation layer + SQL interaction layer**: kết nối trực tiếp SQL Server, thực thi SQL thật, hiển thị BEFORE/AFTER data để demo nghiệp vụ cho giảng viên.

> Trước khi generate bất kỳ feature nào, tham khảo file `basic-requirement-for-website-demo.jpg`.

---

## Tech Stack

| Layer | Công nghệ |
|---|---|
| Backend | Django (monolithic, Django Templates) |
| Database | SQL Server 2019 (Docker trên macOS) |
| DB Driver | pyodbc, mssql-django, ODBC Driver 18 |
| Frontend | Bootstrap 5 (tables, cards, navbar, forms) |

**KHÔNG dùng:** React, Next.js, REST API, DRF, GraphQL, microservices.

---

## Kết nối Database

**Django engine:** `mssql`

**Env vars:** `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`

**Connection options bắt buộc:** `'TrustServerCertificate': 'yes'`

Luôn dùng raw SQL — KHÔNG dùng ORM:

```python
with connection.cursor() as cursor:
    cursor.execute("EXEC sp_ten_procedure @param = %s", [value])
    # hoặc raw SELECT/UPDATE/INSERT
```

**Không tự generate Django ORM models hay authentication system trừ khi được yêu cầu.**

---

## Kiến trúc

```
Django Templates → Django Views → Raw SQL / EXEC SP → SQL Server
                                                        ↓ (auto)
                                                    Trigger fires
```

Business logic (SP, Trigger, Function, Cursor) **đã được viết sẵn trên SSMS và tồn tại trong SQL Server**. Django chỉ gọi chúng — không reimport logic vào Python.

```
project/
├── booking/        # app chính (views, urls)
├── config/         # settings, db config
├── templates/      # Django HTML templates
├── static/         # CSS, JS tĩnh
├── sql/            # bản sao .sql files để version control (schema, SP, trigger, function, cursor, security, sample data)
├── requirements.txt
├── .env.example
└── manage.py
```

**Thư mục `sql/`** chỉ để lưu bản copy các file `.sql` đã viết trên SSMS phục vụ version control và nộp đồ án — không phải nơi Django đọc/chạy SQL.

---

## Demo Flow (cốt lõi đồ án)

Mỗi tính năng demo (SP, Trigger, Function, Raw SQL) phải trình bày theo flow 5 bước:

| Bước | Nội dung | Yêu cầu |
|---|---|---|
| B1 | Mô tả nghiệp vụ | Text giải thích bài toán |
| B2 | Hiển thị SQL sẽ chạy | Code block SQL/SP/Trigger thật |
| B3 | Dữ liệu BEFORE | Load trực tiếp từ SQL Server |
| B4 | Nút Execute | Thực sự gọi SQL Server |
| B5 | Dữ liệu AFTER | Reload từ SQL Server sau khi execute |

**Ví dụ luồng thực tế:**

- Hiển thị ví tài xế = 100k (BEFORE, load từ DB)
- Bấm "Hoàn thành cuốc xe" → Django gọi `EXEC sp_complete_trip @trip_id=?`
- SQL Server tự kích hoạt Trigger → cập nhật ví tài xế
- Website reload → hiển thị ví = 120k (AFTER, load lại từ DB)

**Tuyệt đối KHÔNG:** hardcode data, mock JSON, fake data, simulate SQL execution.

---

## Các trang chính

- **Dashboard** — tổng quan dữ liệu từ DB
- **Drivers Page** — danh sách tài xế
- **Trips Page** — danh sách chuyến đi
- **Procedure Demo** — demo 5 SP theo flow B1→B5
- **Trigger Demo** — demo 5 Trigger theo flow B1→B5
- **Function / Cursor Demo** — tương tự

---

## UI & Coding Rules

- Bootstrap 5, academic-friendly, business-style — KHÔNG animation, fancy UI
- Simple, readable, explicit — clarity hơn cleverness
- Mọi SQL execution cần basic error handling, không crash khi query lỗi

---

## Quy trình phát triển (theo phase)

| Phase | Nội dung |
|---|---|
| 1 | Django setup, SQL Server connection, Bootstrap base layout |
| 2 | Dashboard, Drivers page, Trips page |
| 3 | Procedure demo, Trigger demo, BEFORE/AFTER visualization |
| 4 | Function/Cursor demo, UI cleanup, error handling |

**Generate từng phase — KHÔNG generate toàn bộ project một lần. Dừng sau mỗi phase và chờ instruction.**
