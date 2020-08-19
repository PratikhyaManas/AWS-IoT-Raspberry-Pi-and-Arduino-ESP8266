#!/usr/bin/python
# importing libraries
import paho.mqtt.client as paho
import ssl
from time import sleep
from random import uniform
 
connflag = False
 
def on_connect(client, userdata, flags, rc):                # func for making connection
    global connflag
    print("Connected to AWS")
    connflag = True
    #if connection is successful, rc value will be 0
    print("Connection returned result: " + str(rc) )
    #print(flags)
 
def on_message(client, userdata, msg):                      # Func for Sending msg
    print(msg.topic+" "+str(msg.payload))
 
#def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))
 
mqttc = paho.Client()    
#create an mqtt client object
#attach call back function
mqttc.on_connect = on_connect
#attach on_connect function written in the
#mqtt class, (which will be invoked whenever
#mqtt client gets connected with the broker)
#is attached with the on_connect function
#written by you.


mqttc.on_message = on_message                               # assign on_message func
#attach on_message function written inside
#mqtt class (which will be invoked whenever
#mqtt client gets a message) with the on_message
#function written by you

#### Change following parameters #### 
awshost = "a252np1o22gleq-ats.iot.us-east-1.amazonaws.com"      # Endpoint
awsport = 8883                                              # Port no.   
clientId = "IoT_Test"                                     # Thing_Name
thingName = "IoT_Test"                                    # Thing_Name
caPath = "AmazonRootCA1.pem.crt" #Amazon's certificate from Third party                                     # Root_CA_Certificate_Name
certPath = "14cccc7820-certificate.pem.crt"   # <Thing_Name>.cert.pem.crt. Thing's certificate from Amazon
keyPath = "14cccc7820-private.pem.key"        # <Thing_Name>.private.key Thing's private key from Amazon
 
mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters
 
mqttc.connect(awshost, awsport, keepalive=60)               # connect to aws server
 
mqttc.loop_start()                                          # Start the loop
 
while 1:
    sleep(5)
    if connflag == True:
        tempreading = uniform(20.0,25.0)                        # Generating Temperature Readings
        message = '{"temperature":'+str(tempreading)+'}'
        mqttc.publish("temperatureTopic", message, 1)        # topic: temperature # Publishing Temperature values
        print("msg sent: temperature " + "%.2f" % tempreading ) # Print sent temperature msg on console
    else:
        print("waiting for connection...") 