# Modular Entity and Mapping System API

## Project Overview
A modular Django REST Framework backend for managing **Vendors, Products, Courses, Certifications**, and their mappings.  
All APIs are implemented using **APIView**, with **drf-yasg** for Swagger and ReDoc documentation.

---

## Apps

# Modular API: Vendors, Products, Courses, Certifications & Mappings

This project is a modular Django REST Framework backend for managing Vendors, Products, Courses, Certifications, and their mappings. All APIs use **APIView only** (no ViewSets, routers, GenericAPIView, or mixins). API documentation is provided via drf-yasg (Swagger & ReDoc).

---

## Project Structure

```
modular_api/
│
├── vendor/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── product/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── course/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── certification/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── vendor_product_mapping/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── product_course_mapping/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── course_certification_mapping/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── modular_api/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py
```

---

## Setup Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/25punam/Modular-API.git
   cd modular_api
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install django djangorestframework drf-yasg
   ```
4. **Add to `INSTALLED_APPS` in `settings.py`:**
   ```python
   'rest_framework',
   'drf_yasg',
   'vendor',
   'product',
   'course',
   'certification',
   'vendor_product_mapping',
   'product_course_mapping',
   'course_certification_mapping',
   ```
5. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```
7. **Run the server:**
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### Master APIs

| Method | Endpoint                | Description         |
|--------|-------------------------|---------------------|
| GET    | /api/vendors/           | List vendors        |
| POST   | /api/vendors/           | Create vendor       |
| GET    | /api/vendors/<id>/      | Retrieve vendor     |
| PUT    | /api/vendors/<id>/      | Update vendor       |
| PATCH  | /api/vendors/<id>/      | Partial update      |
| DELETE | /api/vendors/<id>/      | Delete vendor       |

Similar endpoints exist for products, courses, and certifications.

### Mapping APIs

| Method | Endpoint                              | Description                  |
|--------|---------------------------------------|------------------------------|
| GET    | /api/vendor-product-mappings/         | List vendor-product mappings |
| POST   | /api/vendor-product-mappings/         | Create mapping               |
| GET    | /api/vendor-product-mappings/<id>/    | Retrieve mapping             |
| PUT    | /api/vendor-product-mappings/<id>/    | Update mapping               |
| PATCH  | /api/vendor-product-mappings/<id>/    | Partial update mapping       |
| DELETE | /api/vendor-product-mappings/<id>/    | Delete mapping               |

Similar endpoints exist for product-course and course-certification mappings.

---

## API Documentation

- **Swagger:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **ReDoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

All APIs include:
- Request body schema
- Response schema
- Query parameters for filtering
- Success and error response examples

---

## Filtering

Use query params for filtering in list APIs:

- `/api/products/?vendor_id=1`
- `/api/courses/?product_id=2`
- `/api/certifications/?course_id=3`

---

## Validation

- Unique code for master entities
- Prevent duplicate mappings
- Only one primary mapping per parent
- Required fields

---

## Admin

All models are registered for admin management.

---

## Example API Usage

Create a vendor:
```bash
curl -X POST http://localhost:8000/api/vendors/ \
     -H "Content-Type: application/json" \
     -d '{"name": "Vendor1", "code": "V001", "description": "Test vendor"}'
```

Retrieve all products:
```bash
curl http://localhost:8000/api/products/
```

Create a vendor-product mapping:
```bash
curl -X POST http://localhost:8000/api/vendor-product-mappings/ \
     -H "Content-Type: application/json" \
     -d '{"vendor": 1, "product": 2, "primary_mapping": true}'
```

---

## Migration Steps

```bash
python manage.py makemigrations
python manage.py migrate
```

## Runserver Steps

```bash
python manage.py runserver
```

---

## Seed Data

- Add your own fixtures or use Django admin to create initial data.

---

## License

MIT