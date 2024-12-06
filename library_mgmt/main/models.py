from django.db import models


class Membership(models.Model):
    MEMBERSHIP_CHOICES = [
        ('6_months', 'Six Months'),
        ('1_year', 'One Year'),
        ('2_years', 'Two Years'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_address = models.TextField()
    adhaar_card_no = models.CharField(max_length=12)
    start_date = models.DateField()
    end_date = models.DateField()
    membership_type = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES, default='6_months')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.membership_type}"


class Media(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('book', 'Book'),
        ('movie', 'Movie'),
    ]
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, default='book')
    name = models.CharField(max_length=255)
    date_of_procurement = models.DateField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.name} ({self.media_type})"

class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('new', 'New User'),
        ('existing', 'Existing User'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    ADMIN_CHOICES = [
        ('yes', 'Admin'),
        ('no', 'User'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='new')
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    admin_status = models.CharField(max_length=10, choices=ADMIN_CHOICES, default='no')

    def __str__(self):
        return f"{self.name} - {self.status} - {'Admin' if self.admin_status == 'yes' else 'User'}"
