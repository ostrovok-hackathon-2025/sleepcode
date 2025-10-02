from django.shortcuts import render
from app.hotels.models import Hotel
from app.reviews.models import Review

def hotel_list(request):
    friends_only = request.GET.get("friends") == "1"
    hotels = Hotel.objects.all()
    data = []
    for h in hotels:
        reviews = Review.objects.filter(hotel=h)
        friends_reviews = [r for r in reviews if r.recommended]
        if friends_only and not friends_reviews:
            continue
        data.append({
            "name": h.name,
            "city": h.city,
            "reviews": friends_reviews,
        })
    return render(request, "index.html", {"hotels": data, "friends_only": friends_only})
