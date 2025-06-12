import random

def pinpicker(number):
    pin = ""
    for i in range(number):
      pin +=  str(random.randint(0,9))
    
    return pin



myping = pinpicker(4)

print(myping)

