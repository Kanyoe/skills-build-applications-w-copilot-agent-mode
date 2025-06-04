try:
    from bson import ObjectId
    print("bson.ObjectId imported successfully.")
except Exception as e:
    print("Error importing bson.ObjectId:", e)

try:
    from django.core.management.base import BaseCommand
    print("django.core.management.base imported successfully.")
except Exception as e:
    print("Error importing django.core.management.base:", e)
