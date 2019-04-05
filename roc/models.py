from django.db import models

class Charge(models.Model):
    srn = models.CharField(max_length=30)
    charge_id = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=100, blank=False)
    dated = models.DateField(null=True)
    amount = models.IntegerField(null=True)
    cin_number = models.CharField(max_length=30, blank=False, null=True)
    creation_date = models.DateField(null=True)
    modification_date = models.DateField(null=True)
    address = models.TextField()

    #Dates created and updated
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    CHOICES = [('True', 'YES'), ('False', 'NO')]

    din_pan = models.CharField(max_length=30,blank=False)
    name = models.CharField(max_length=100, blank=False)
    father_lastname = models.CharField(max_length=50, blank=True)
    cin_number = models.CharField(max_length=30, blank=False, null=True)
    address = models.TextField(blank=True)
    roc_code = models.CharField(max_length=30, blank=True)
    roc_name = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    designation = models.CharField(max_length=30, blank=True)
    appointment_date = models.DateField(null=True)
    dsc_registered = models.CharField(max_length=6, choices=CHOICES, blank=True)
    dsc_expiry_date = models.DateField(null=True)

    #Validity Date
    date_of_birth = models.DateField(null=True)
    vaild_from = models.DateField(null=True)
    vaild_to = models.DateField(null=True)

    #Defaulting Years
    director_default = models.CharField(max_length=6, choices=CHOICES,blank=True)
    defaulting_years =  models.CharField(max_length=100, blank=True)

    #addresses
    address = models.TextField(blank=True)

    #Dates
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    #AutoFill DataBase
    CLASS_CHOICES = [('Private', 'Private'), ('Public', 'Public'), ('OPC', 'Private(One Person Company)')]
    LISTED_CHOICES = [('Unlisted','Unlisted'),('Listed','Listed')]
    DEFAUL_CHOICES = [('True', 'YES'), ('False', 'NO')]

    #ROC Mapping
    cin_number = models.CharField(max_length=30, primary_key=True)
    company_name = models.CharField(max_length=100, blank=False)

    #Current Status
    company_status = models.CharField(max_length=30, blank=True)

    registration_number = models.CharField(max_length=30, blank=True)
    roc_code = models.CharField(max_length=30, blank=True)

    #Classes
    company_class = models.CharField(max_length=8, choices=CLASS_CHOICES, blank=False)
    listed_type = models.CharField(max_length=8, choices=LISTED_CHOICES, blank=True)
    company_category = models.CharField(max_length=80, blank=True)
    company_subcategory = models.CharField(max_length=80, blank=True)

    #Other Info
    members = models.IntegerField(null=True)
    stock = models.CharField(max_length=30, blank=True)
    email_id = models.EmailField(max_length=100,blank=True, unique= False)

    #Capital Related
    authorised_capital = models.IntegerField(null=True)
    paid_capital = models.IntegerField(null=True)

    #Company Addresses
    registered_address = models.TextField()
    other_address = models.TextField(blank=True)

    company_default = models.CharField(max_length=6, choices=DEFAUL_CHOICES, default='False', blank=False)

    #Dates
    annual_general_meeting = models.DateField(null=True)
    balancesheet_date = models.DateField(null=True)
    incorporation_date = models.DateField(null=True)

    #Dates Update and Create
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    #Relationships
    directors = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    charges = models.ForeignKey(Charge, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.cin_number
