# AWS-IoT-Raspberry_Pi & Arduino-8266
 
# PROBLEM STATEMENT:
This program will publish test mqtt messages using the AWS IOT hub

# STEPS:

1. Sign in to AWS Amazon > Services > AWS IoT > Settings > copy Endpoint
    This is your awshost
 
2. Change following things in the below program:
    a. awshost   (from step 1)
    b. clientId  (Thing_Name)
    c. thingName (Thing_Name)
    d. caPath    (root-CA_certificate_Name)
    e. certPath  (<Thing_Name>.cert.pem)
    f. keyPath   (<Thing_Name>.private.key)
 
3. Keep all the files in folder where all aws key files are kept. 
4. Run publisher_dynamodb.py script


