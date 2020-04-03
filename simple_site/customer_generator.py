'''
Used to Generate Fake Customer Data
'''
import os
from faker import Faker
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_site.settings')
django.setup()

from my_app.models import Customer

# Fake population script

FAKE = Faker()

def popluate(_n=5):
    '''
    Function used to create random users and store in the db
    '''
    for entry in range(_n):
        print(entry)

        #create Fake Data for that entry
        f_name = FAKE.first_name()
        l_name = FAKE.last_name()
        address = FAKE.address()
        email = FAKE.email()
        cc_number = FAKE.credit_card_number()

        #Create the new user
        user = Customer.objects.get_or_create(first_name=f_name, last_name=l_name, email=email, address=address, cc_number=cc_number)[0]
        print(user)

if __name__ == '__main__':
    print('popluating scripts')
    popluate(20)
    print('populating complete')
