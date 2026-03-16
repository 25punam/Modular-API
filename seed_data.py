# seed_data.py
import os
import django

# Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "modular_api.settings")
django.setup()

from vendor.models import Vendor
from product.models import Product
from course.models import Course
from certification.models import Certification
from vendor_product_mapping.models import VendorProductMapping
from product_course_mapping.models import ProductCourseMapping
from course_certification_mapping.models import CourseCertificationMapping

def run():
    print("Seeding data...")

    # --- Vendors ---
    vendors = [
        {"name": "Amazon", "code": "V001", "description": "Cloud services"},
        {"name": "Microsoft", "code": "V002", "description": "Software and cloud"},
        {"name": "Google", "code": "V003", "description": "Search and cloud services"},
    ]
    vendor_objs = []
    for v in vendors:
        obj, created = Vendor.objects.get_or_create(code=v["code"], defaults=v)
        vendor_objs.append(obj)

    # --- Products ---
    products = [
        {"name": "AWS EC2", "code": "P001", "description": "Cloud compute service"},
        {"name": "Azure VM", "code": "P002", "description": "Microsoft virtual machines"},
        {"name": "Google Compute Engine", "code": "P003", "description": "Google cloud compute"},
    ]
    product_objs = []
    for p in products:
        obj, created = Product.objects.get_or_create(code=p["code"], defaults=p)
        product_objs.append(obj)

    # --- Courses ---
    courses = [
        {"name": "AWS Basics", "code": "C001", "description": "Introduction to AWS"},
        {"name": "Azure Fundamentals", "code": "C002", "description": "Microsoft Azure intro"},
        {"name": "Google Cloud Intro", "code": "C003", "description": "Intro to GCP"},
    ]
    course_objs = []
    for c in courses:
        obj, created = Course.objects.get_or_create(code=c["code"], defaults=c)
        course_objs.append(obj)

    # --- Certifications ---
    certifications = [
        {"name": "AWS Certified Solutions Architect", "code": "CERT001", "description": "AWS Cert"},
        {"name": "Azure Fundamentals Cert", "code": "CERT002", "description": "Azure Cert"},
        {"name": "Google Cloud Associate", "code": "CERT003", "description": "GCP Cert"},
    ]
    cert_objs = []
    for cert in certifications:
        obj, created = Certification.objects.get_or_create(code=cert["code"], defaults=cert)
        cert_objs.append(obj)

    # --- Vendor-Product Mappings ---
    mappings = [
        {"vendor": vendor_objs[0], "product": product_objs[0], "primary_mapping": True},
        {"vendor": vendor_objs[1], "product": product_objs[1], "primary_mapping": True},
        {"vendor": vendor_objs[2], "product": product_objs[2], "primary_mapping": True},
    ]
    for m in mappings:
        VendorProductMapping.objects.get_or_create(
            vendor=m["vendor"],
            product=m["product"],
            defaults={"primary_mapping": m["primary_mapping"], "is_active": True}
        )

    # --- Product-Course Mappings ---
    prod_course_mappings = [
        {"product": product_objs[0], "course": course_objs[0], "primary_mapping": True},
        {"product": product_objs[1], "course": course_objs[1], "primary_mapping": True},
        {"product": product_objs[2], "course": course_objs[2], "primary_mapping": True},
    ]
    for pcm in prod_course_mappings:
        ProductCourseMapping.objects.get_or_create(
            product=pcm["product"],
            course=pcm["course"],
            defaults={"primary_mapping": pcm["primary_mapping"], "is_active": True}
        )

    # --- Course-Certification Mappings ---
    course_cert_mappings = [
        {"course": course_objs[0], "certification": cert_objs[0], "primary_mapping": True},
        {"course": course_objs[1], "certification": cert_objs[1], "primary_mapping": True},
        {"course": course_objs[2], "certification": cert_objs[2], "primary_mapping": True},
    ]
    for ccm in course_cert_mappings:
        CourseCertificationMapping.objects.get_or_create(
            course=ccm["course"],
            certification=ccm["certification"],
            defaults={"primary_mapping": ccm["primary_mapping"], "is_active": True}
        )

    print("Seeding completed!")

if __name__ == "__main__":
    run()