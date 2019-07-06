# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC4814f794e6e19e083fc3dda63b3746cb'
auth_token = '87b9303c354e284f6a7641bd2d3992b8'
client = Client(account_sid, auth_token)
i = 0;
while 1: 
    message = client.messages.create(
                     body="تم اختراقك بنجاح ... ههههههه",
                     from_='+15182031326',
				     # to='+201090802147'
                     # to='+201204993792'
                     to='+201022363439'
                 )
	  
		 
    if i > 100: 
     break
    print(message.sid)
    i += 1