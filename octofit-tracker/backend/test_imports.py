try:
    from bson import ObjectId
    print("bson module imported successfully.")
except ImportError as e:
    print(f"Error importing bson: {e}")

try:
    from django.core.management.base import BaseCommand
    print("django.core.management.base imported successfully.")
except ImportError as e:
    print(f"Error importing django.core.management.base: {e}")
