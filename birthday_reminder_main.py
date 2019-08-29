import requests
import json
import datetime
from names import Friends_List
import time


URL = 'http://www.way2sms.com/api/v1/sendCampaign'

x = datetime.datetime.now()
today = x.strftime("%d/%m")
Todays_birthday = [" "]


#prepare for message
def get_message(name):
    name = Todays_birthday[-1]
    message = "Wishing you a day filled with happiness and a year filled with joy. Happy birthday! " + name.title()
    return message


#Check availabilty of birthday
def check_birthday(today):
    for i in range(len(Friends_List)):
        if today in Friends_List[i][1]:
            Todays_birthday.append(Friends_List[i][0])
            return Friends_List[i][1]
        else:
            return None

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

name = Todays_birthday[-1]
message = get_message(name)

#send text message
def send_sms(message):
    if check_birthday(today) == None:
        print("No birthday found at " + today)
        return 0
    else:
        # get responses
        response = sendPostRequest(URL, apiKey, secretKey, 'stage', phoneNo, 'WAYSMS', message )
        # print response if you want
        print (response.text)

send_sms(message)
