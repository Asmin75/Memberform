from django.contrib import admin
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'title', 'first_name', 'middle_name',
                    'last_name', 'date_of_birth', 'gender', 'program_participated',
                    'program_start_year', 'program_start_year', 'program_end_year',
                    'current_designation', 'current_organization', 'business_address', 'residence_address',
                    'personal_email', 'office_email', 'office_phone', 'mobile_phone', 'photo', 'social_media_address',
                    )
    search_fields = ('email_address', 'title', 'first_name', 'middle_name',
                    'last_name', 'date_of_birth', 'gender', 'program_participated',
                    'program_start_year', 'program_start_year', 'program_end_year',
                    'current_designation', 'current_organization', 'business_address', 'residence_address',
                    'personal_email', 'office_email', 'office_phone', 'mobile_phone', 'photo', 'social_media_address',
                    )
admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
admin.site.register(Member,MemberAdmin)
# Register your models here.
