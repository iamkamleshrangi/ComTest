from django.db import models

class Charge(models.Model):
    srn = models.CharField(max_length=30)
    charge_id = models.CharField(max_length=30)
    name = models.CharField(max_length=100, blank=False)
    dated = models.DateField(null=True)
    amount = models.IntegerField(null=True)
    address = models.TextField()

    #Dates
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.name

class Director(models.Model):
    din_dpin_pan = models.CharField(max_length=30)
    name = models.CharField(max_length=100, blank=False)
    address = models.TextField(blank=True)
    roc_code = models.CharField(max_length=30, blank=True)
    roc_name = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    vaild_from = models.DateField(null=True)
    vaild_to = models.DateField(null=True)

    #Dates
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.name

class Company(models.Model):
    #Codes
    CLASS_CHOICES = [('Private', 'Private'), ('Public', 'Public'), ('OPC', 'Private(One Person Company)')]
    LISTED_CHOICES = [('Unlisted','Unlisted'),('Listed','Listed')]
    DEFAULTER_CHOICES = [('True', 'YES'), ('False', 'NO')]

    #ROC Mapping
    cin_number = models.CharField(max_length=30, primary_key=True)
    company_name = models.CharField(max_length=100, blank=False)

    roc_code = models.CharField(max_length=30, blank=True)
    registration_number = models.CharField(max_length=30, blank=True)

    company_category = models.CharField(max_length=80, blank=True)
    company_subcategory = models.CharField(max_length=80, blank=True)

    company_class = models.CharField(max_length=8, choices=CLASS_CHOICES, blank=False)

    listed_type = models.CharField(max_length=8, choices=LISTED_CHOICES, blank=True)
    members = models.IntegerField(null=True)

    company_status = models.CharField(max_length=30, blank=True)

    authorised_capital = models.IntegerField(null=True)
    paid_capital = models.IntegerField(null=True)

    incorporation_date = models.DateField(null=True)
    registered_address = models.TextField()

    company_default = models.CharField(max_length=6, choices=DEFAULTER_CHOICES, default='False', blank=False)

    #Dates
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    #Relationships
    directors = models.ForeignKey(Director, null=True)
    charges = models.ForeignKey(Charge, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.cin_number
