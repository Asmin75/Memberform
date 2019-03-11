from django.db import models
from multiselectfield import MultiSelectField

TITLE_CHOICES = (
    ('Mr', 'Mr.'),
    ('Ms', 'Ms.'),
    ('Dr', 'Dr.'),
    ('Prof', 'Prof.'),
)
GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female'),
   ('N', 'Prefer not to say'),
)
PARTICIPATE_CHOICES = (
    ('American Council of Young Political Leaders (ACYPL)', 'American Council of Young Political Leaders (ACYPL)'),
    ('American English E-Teacher Program', 'American English E-Teacher Program'),
    ('BRIDGE (BRIDGE)', 'BRIDGE (Building Respect through Internet Dialogue and Global Education)'),
    ('Citizen Exchanges', 'Citizen Exchanges'),
    ('Community Solutions Program', 'Community Solutions Program'),
    ('Cultural Programs', 'Cultural Programs'),
    ('English Access Microscholarship Program', 'English Access Microscholarship Program'),
    ('ELFPFEW', 'English Language Fellow Program Foreign Educators Workshop'),
    ('Farmer Youth Program (4-H Foundation)', 'Farmer Youth Program (4-H Foundation)'),
    ('Foreign Press Center Reporting Tour (non-ECA)', 'Foreign Press Center Reporting Tour (non-ECA)'),
    ('Fortune 500: Women Leaders', 'Fortune 500: Women Leaders'),
    ('Fulbright American Studies Institute', 'Fulbright American Studies Institute'),
    ('Fulbright Conflict Resolution Program', 'Fulbright Conflict Resolution Program'),
    ('Fulbright Foreign Student Program', 'Fulbright Foreign Student Program'),
    ('Fulbright Foreign Teacher Exchange Program', 'Fulbright Foreign Teacher Exchange Program'),
    ('Fulbright International Science and Technology Award', 'Fulbright International Science and Technology Award'),
    ('Fulbright New Century Visiting Scholars Program', 'Fulbright New Century Visiting Scholars Program'),
    ('Fulbright Programs (other)', 'Fulbright Programs (other)'),
    ('Fulbright Scholar-in-Residence Program', 'Fulbright Scholar-in-Residence Program'),
    ('Fulbright Seminar Programs (Foreign)', 'Fulbright Seminar Programs (Foreign)'),
    ('Fulbright Visiting Scholar Program', 'Fulbright Visiting Scholar Program'),
    ('Global Undergraduate Exchange Program (UGRAD)', 'Global Undergraduate Exchange Program (UGRAD)'),
    ('Graduate Fellowships', 'Graduate Fellowships'),
    ('Hubert Humphrey Fellowship Program', 'Hubert Humphrey Fellowship Program'),
    ('IVLP', 'International Visitor Leadership Program (IVLP or IVP as referred previously)'),
    ('IVLP (IVLP)/ Voluntary Visitors', 'International Visitor Leadership Program (IVLP)/ Voluntary Visitors'),
    ('International Writing Program (IWP)', 'International Writing Program (IWP)'),
    ('J-1 Au pair (non-ECA)', 'J-1 Au pair (non-ECA)'),
    ('J-1 Intern (non-ECA)', 'J-1 Intern (non-ECA)'),
    ('J-1 Physician (non-ECA)', 'J-1 Physician (non-ECA)'),
    ('J-1 Specialist (non-ECA)', 'J-1 Specialist (non-ECA)'),
    ('J-1 Trainee (non-ECA)', 'J-1 Trainee (non-ECA)'),
    ('Legislative Fellows Program (LFP)', 'Legislative Fellows Program (LFP)'),
    ('(NESA UGRAD)', 'Near East and South Asia Undergraduate Exchange Program (NESA UGRAD)'),
    ('Ngawang Choephel Fellows Program', 'Ngawang Choephel Fellows Program'),
    ('(PLUS)', 'Partnerships for Learning Undergraduate Studies Program (PLUS)'),
    ('Professional Exchanges and Training', 'Professional Exchanges and Training'),
    ('Professional Fellows Program (PFP)', 'Professional Fellows Program (PFP)'),
    ('Sports Exchanges', 'Sports Exchanges'),
    ('Study of the U.S. Institutes (any other SUSI)', 'Study of the U.S. Institutes (any other SUSI)'),
    ('Study of the U.S. Institutes for Scholars (SUSI)', 'Study of the U.S. Institutes for Scholars (SUSI)'),
    ('(SUSI)', 'Study of the U.S. Institutes for Student Leaders (SUSI)'),
    ('(SUSI)', 'Study of the U.S. Summer Institute for Secondary Educators Program (SUSI)'),
    ('Teaching Excellence & Achievement Program (TEA)', 'Teaching Excellence & Achievement Program (TEA)'),
    ('Tibetan Scholarship Program (TSP)', 'Tibetan Scholarship Program (TSP)'),
    ('Traditional Public-Private Partnership (TPPP)', 'Traditional Public-Private Partnership (TPPP)'),
    ('USBT (EducationUSA Advisors)', 'USBT (EducationUSA Advisors)'),
    ('Youth Exchange Programs (any other)', 'Youth Exchange Programs (any other)'),
    ('Youth Leadership Program (YLP)', 'Youth Leadership Program (YLP)'),
    ('Other', 'other'),
)


class Member(models.Model):
    email_address = models.EmailField(max_length=100)
    title = models.CharField(max_length=6, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=80)
    middle_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    date_of_birth = models.DateField(max_length=10)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    program_participated = MultiSelectField(choices=PARTICIPATE_CHOICES)
    program_start_year = models.DateField(max_length=10)
    program_end_year = models.DateField(max_length=10)
    current_designation = models.CharField(max_length=100)
    current_organization = models.CharField(max_length=100)
    business_address = models.CharField(max_length=20)
    residence_address = models.CharField(max_length=20)
    personal_email = models.EmailField(max_length=100)
    office_email = models.EmailField(max_length=100, null=True)
    office_phone = models.CharField(max_length=100, null=True)
    residence_phone = models.CharField(max_length=100, null=True)
    mobile_phone = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="Photo")
    social_media_address = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name