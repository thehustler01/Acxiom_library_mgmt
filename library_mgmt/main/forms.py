from django import forms
from .models import Membership, Media, UserProfile


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['first_name', 'last_name', 'contact_name', 'contact_address', 'adhaar_card_no', 'start_date', 'end_date', 'membership_type']
        widgets = {
            'membership_type': forms.RadioSelect,
        }


class UpdateMembershipForm(forms.Form):
    MEMBERSHIP_CHOICES = [
        ('6_months', 'Six Months'),
        ('1_year', 'One Year'),
        ('2_years', 'Two Years'),
    ]
    MEMBERSHIP_REMOVE_CHOICES = [
        ('extend', 'Extend'),
        ('cancel', 'Cancel'),
    ]
    membership_number = forms.IntegerField(label="Membership Number")
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    membership_extn = forms.ChoiceField(choices=MEMBERSHIP_CHOICES, widget=forms.RadioSelect, initial='6_months')
    membership_remove = forms.ChoiceField(choices=MEMBERSHIP_REMOVE_CHOICES, widget=forms.RadioSelect, initial='extend')


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['media_type', 'name', 'date_of_procurement', 'quantity']
        widgets = {
            'media_type': forms.RadioSelect,
        }


class UpdateMediaForm(forms.Form):
    MEDIA_TYPE_CHOICES = [
        ('book', 'Book'),
        ('movie', 'Movie'),
    ]
    media_type = forms.ChoiceField(choices=MEDIA_TYPE_CHOICES, widget=forms.RadioSelect, initial='book')
    name = forms.CharField(max_length=255)
    serial_no = forms.IntegerField(label="Serial No")
    status = forms.ChoiceField(choices=[('available', 'Available'), ('borrowed', 'Borrowed')])
    date_of_procurement = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    quantity = forms.IntegerField()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user_type', 'name', 'status', 'admin_status']
        widgets = {
            'user_type': forms.RadioSelect,
            'status': forms.CheckboxInput,
            'admin_status': forms.CheckboxInput,
        }
