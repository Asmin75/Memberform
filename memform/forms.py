from django import forms
from django.contrib.admin import widgets
from .models import Member

class MForm(forms.ModelForm):

    class Meta:

        model = Member
        fields =('email_address', 'title', 'first_name', 'middle_name',
                    'last_name', 'date_of_birth', 'gender', 'program_participated',
                    'program_start_year', 'program_start_year', 'program_end_year',
                    'current_designation', 'current_organization', 'business_address', 'residence_address',
                    'personal_email', 'office_email', 'office_phone', 'mobile_phone', 'photo', 'social_media_address',
                    )

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'datetimepicker'})
        }

