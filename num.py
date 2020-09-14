# get phone number details
# github.com/rashtion 

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import phonemetadata
import time 

# enter phone number here  :

phoneNumber = phonenumbers.parse("PHONE_NUMBER_HERE")

time.sleep(0.3)
print(geocoder.description_for_number(phoneNumber, 'en'))
time.sleep(0.3)
print(carrier.name_for_number(phoneNumber, 'en'))
time.sleep(0.3)
print(phonemetadata.NumberFormat(phoneNumber, 'en'))

time.sleep(3)
print("Thanks for using") 
