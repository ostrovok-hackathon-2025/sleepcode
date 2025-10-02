import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from django.contrib.auth.models import User
from app.hotels.models import Hotel
from app.reviews.models import Review

print("Seeding database...")

# Users
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin123")
alice, _ = User.objects.get_or_create(username="alice", defaults={"password":"alice"})
bob, _ = User.objects.get_or_create(username="bob", defaults={"password":"bob"})
charlie, _ = User.objects.get_or_create(username="charlie", defaults={"password":"charlie"})

# Hotels
moscow, _ = Hotel.objects.get_or_create(name="Отель Москва", city="Москва")
paris, _ = Hotel.objects.get_or_create(name="Hotel Paris", city="Париж")
istanbul, _ = Hotel.objects.get_or_create(name="Istanbul Stay", city="Стамбул")

# Reviews
Review.objects.get_or_create(hotel=moscow, user=bob, text="Очень удобно!", recommended=True)
Review.objects.get_or_create(hotel=istanbul, user=charlie, text="Красивый вид!", recommended=True)
print("Done seeding.")
