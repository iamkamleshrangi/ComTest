from pymongo import MongoClient
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "company.settings")
django.setup()
from roc.models import Company, Charge, Director

#Settings MongoDB
conn = MongoClient('127.0.0.1', 27017)
db = conn['roc_data']

def processRoc(cin):
    cin = "U72900TG2008PTC060114"

    col1 = "roc_director_details"
    col2 = "roc_director_disqualifieds" #[x]
    col3 = "roc_defaulters_companies" #[x]
    col4 = "roc_defaulters_directors"
    col5 = "roc_defaulters_secretaries"
    col6 = "roc" #[x]
    #================Defaulters Companies===========
    defaulters_company = db['roc_defaulters_companies'].find_one({'cin_number': cin})
    company_default = 'False'
    if defaulters_company:
        company_default = 'True'
    #===============Director Disqualified===========
    director_disqualified = db['roc_director_disqualifieds'].find({'cin_number': cin})
    for director in director_disqualified:
        print(director)
        print('')
    #=================Company Data==================
    company = db['roc'].find_one({'cin_number': cin})
    #Extract Data
    cin_number = company.get('cin_number','')
    company_name = company.get('company_name','')

    city = company.get('roc_code','').replace('RoC-','')
    registration_number = company.get('registration_number','')

    company_category = company.get('company_category','')
    company_subcategory = company.get('company_subcategory','')

    company_class = company.get('company_class','')
    incorporation_date = company.get('incorporation_date','')

    authorised_capital = company.get('authorised_capital','')
    paid_capital = company.get('paid_capital','')

    registered_address = company.get('registered_address','')
    listed_type = company.get('listed_type','')

    company_status = company.get('company_status','')
    members = company.get('members','')

    #Charges
    charges = company.get('charges','')
    for charge in charges:
        sno = charge.get('sno', '')
        srn = charge.get('srn','')
        charge_id = charge.get('charge_id','')
        bank_name = charge.get('charge_holder_name','')
        amount = charge.get('amount','')
        address = charge.get('address','')

        creation_date = charge.get('creation_date','')
        modification_date = charge.get('modification_date','')
        break

    #To it later
    signatories = company.get('signatory','')
    for signatory in signatories:
        din_pan = signatory['pan']
        director_name = signatory['name']
        director_address = signatory['address']
        designation = signatory['designation']
        appointment = signatory['appointment']
        dsc_registered = signatory['dsc_registered']
        #break


def getCin():
    con = db['roc']
    for record in con.find({},{'cin_number':1}):
        cin = record['cin_number']
        processRoc(cin)
        break

getCin()
