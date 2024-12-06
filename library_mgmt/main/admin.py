from django.contrib import admin
from .models import Membership, Media, UserProfile

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'membership_type', 'start_date', 'end_date')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'media_type', 'quantity', 'date_of_procurement')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_type', 'status', 'admin_status')
