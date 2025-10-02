from django.db import models
from django.contrib.auth.models import User
from app.hotels.models import Hotel

class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    recommended = models.BooleanField(default=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.hotel.name}"
