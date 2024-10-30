from django.db import models

# Create your models here.
from django.db import models


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ("Food", "Food"),
        ("Transport", "Transport"),
        ("Entertainment", "Entertainment"),
        ("Utilities", "Utilities"),
        ("Groceries", "Groceries"),  # For supermarket or grocery shopping
        ("Dining Out", "Dining Out"),  # For restaurants and cafes
        ("Shopping", "Shopping"),  # For retail shopping
        ("Health", "Health"),  # For medical expenses or health-related purchases
        ("Travel", "Travel"),  # For travel-related expenses (flights, hotels)
        ("Education", "Education"),  # For tuition, books, and other educational costs
        ("Home", "Home"),  # For home improvement or supplies
        ("Gifts", "Gifts"),  # For presents or special occasions
        (
            "Subscriptions",
            "Subscriptions",
        ),  # For monthly or yearly subscriptions (Netflix, etc.)
        ("Insurance", "Insurance"),  # For health, vehicle, or property insurance
        ("Investments", "Investments"),  # For investments in stocks, bonds, etc.
        ("Pet Care", "Pet Care"),  # For expenses related to pets (food, vet visits)
        ("Personal Care", "Personal Care"),  # For grooming, cosmetics, etc.
        ("Clothing", "Clothing"),  # For clothing and accessories
        ("Fitness", "Fitness"),  # For gym memberships, classes, or sports activities
        (
            "Technology",
            "Technology",
        ),  # For gadgets, software, or tech-related purchases
        ("Miscellaneous", "Miscellaneous"),  # For any other expenses not covered above
    ]
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"
