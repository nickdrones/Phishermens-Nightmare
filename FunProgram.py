import requests
import os
import random
import string
import json
import time

def makeFakeCCNum():
    firstSet=str(random.randint(1000,9999))
    secondSet=str(random.randint(1000,9999))
    thirdSet=str(random.randint(1000,9999))
    fourthSet=str(random.randint(1000,9999))
    fifthSet=str(random.randint(1000,9999))
    return "{} {} {} {} {}".format(firstSet,secondSet,thirdSet,fourthSet,fifthSet)

def makeFakeCCexp():
    month=str(random.randint(10,12))
    year=str(random.randint(21,28))
    return "{}/{}".format(month,year)

def makeFakeCCcvv():
    return str(random.randint(100,999))

def makeFakePinNum():
    return str(random.randint(1000,9999))

def makeFakeDOB():
    month=str(random.randint(1,12))
    day=str(random.randint(1,28))
    year=str(random.randint(1970,2002))
    return "{}/{}/{}".format(month,day,year)

def makeFakeSSN():
    firstOne=str(random.randint(100,999))
    secondOne=str(random.randint(10,99))
    thirdOne=str(random.randint(1000,9999))
    return "{}-{}-{}".format(firstOne,secondOne,thirdOne)


requests.adapters.DEFAULT_RETRIES=10

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url='scam url here'
headers = {'User-Agent': 'Mozilla/5.0 (Win64 x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36'}

names = json.loads(open('names.json').read())
lastNames=json.loads(open('surnames.json').read())
emailAddresses=["gmail.com","yahoo.com","sjcd.edu","outlook.com", "youtube.com", "nasa.gov", "enron.com", "vxinnovations.com", "fbi.gov", "doj.gov", "cia.gov", "nsa.gov", "protonmail.com", "protonmail.ch","thecw.com","aol.com", "att.net", "comcast.net", "facebook.com", "gmail.com", "gmx.com", "googlemail.com","google.com", "hotmail.com", "hotmail.co.uk", "mac.com", "me.com", "mail.com", "msn.com","live.com", "sbcglobal.net", "verizon.net", "yahoo.com", "yahoo.co.uk","btinternet.com", "virginmedia.com", "blueyonder.co.uk", "freeserve.co.uk", "live.co.uk","ntlworld.com", "o2.co.uk", "orange.net", "sky.com", "talktalk.co.uk", "tiscali.co.uk","virgin.net", "wanadoo.co.uk", "bt.com","yahoo.ca", "hotmail.ca", "bell.net", "shaw.ca", "sympatico.ca", "rogers.com"]


while (1==1):
    try:
        for i in range(len(lastNames)):
            randomName=random.randint(0,len(names)-1) #Random First Name
            randomLastName=random.randint(0,len(lastNames)-1) #Random Last Name

            extraLength=random.randint(1,5)
            name_extra = ''.join(random.choice(string.digits) for i in range(extraLength))
            chosenAddress=str(random.choice(emailAddresses))

            username = names[randomName].lower() + name_extra + "@" + chosenAddress #Randomly generated email
            passwordLength=random.randint(8,15)
            password = ''.join(random.choice(chars) for i in range(passwordLength)) #Randomly generated password

            CreditCardNumber=makeFakeCCNum()
            CreditCardExpDate=makeFakeCCexp()
            CreditCardCVV=makeFakeCCcvv()
            CreditCardPin=makeFakePinNum()
            FakeDOB=makeFakeDOB()
            FakeSSN=makeFakeSSN()

            requests.post(url, allow_redirects=False, data={
                'cc': CreditCardNumber,
                'exp': CreditCardExpDate,
                'cvv':CreditCardCVV,
                'pin':CreditCardPin,
                'dob':FakeDOB,
                'mname': randomName,
                'sc': FakeSSN,
            },headers=headers)
            print 'sending packet:%s, %s, %s,%s,%s,%s,%s' % (CreditCardNumber,CreditCardExpDate, CreditCardCVV, CreditCardPin, FakeDOB, randomName, FakeSSN) #edit to only show data points being sent
    except:
        print "Error, restarting...\n" #If page times out (common through VPN), wait 5 seconds and restart
    time.sleep(5)