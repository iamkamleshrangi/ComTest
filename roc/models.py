from django.db import models

class Company(models.Model):
    #Codes 
    CLASS_CHOICES = [('Private', 'Private'), ('Public', 'Public'), ('OPC', 'Private(One Person Company)')]
    LISTED_CHOICES = [('Unlisted','Unlisted'),('Listed','Listed')]

    #ROC Mapping
    cin_number = models.CharField(max_length=30, blank=False)
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

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.cin_number
