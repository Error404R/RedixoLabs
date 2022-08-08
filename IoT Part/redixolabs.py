import connections
from boltiot import Sms, Bolt
import json, time

minimum_limit = 300
maximum_limit = 600  


mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)


while True: 
    print ("Reading sensor value")
    response = mybolt.analogRead('A0') 
    data = json.loads(response) 
    print("Sensor value is: " + str(data['value']))
    try: 
        sensor_value = int(data['value']) 
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms("The Current temperature sensor value is " +str(sensor_value))
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is :" + str(response.status))
            print("----------------------------------------------------------------")
            print("Intensity Value: ",sensor_value)
            
            print("Dear Prince, Your fieled No: 1 humidity is low")
            print("Turning on electric motor No: 01..............")
            response=mybolt.digitalWrite('0','HIGH')
            print(response)

            print("Sending SMS alert on your mobile number that elctric motor is turned on ")
            print("---------------------------------------------------------------")
            response = sms.send_sms("Dear RedixoLabs Team, Turning on Your electric motor No : 01 . Humidity of field No: 01 is " +str(sensor_value))
            print("Response received from Twilio API is: " + str(response))
            print("Alert has sent successfully")
            print("--------------------------------------------------------------------")

    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(10)
