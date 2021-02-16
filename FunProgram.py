import requests
import os
import random
import string
import json
import time

#################################################
#    Generator Functions
#################################################

def makeFakeCCNum(): #Function that generates a fake credit card number in the form "#### #### #### #### ####"
    firstSet=str(random.randint(1000,9999))
    secondSet=str(random.randint(1000,9999))
    thirdSet=str(random.randint(1000,9999))
    fourthSet=str(random.randint(1000,9999))
    fifthSet=str(random.randint(1000,9999))
    return "{} {} {} {} {}".format(firstSet,secondSet,thirdSet,fourthSet,fifthSet)

def makeFakeCCexp(): #Function that generates a fake credit card exp date in the form "MM/YY"
    month=str(random.randint(10,12))
    year=str(random.randint(21,28))
    return "{}/{}".format(month,year)

def makeFakeCCcvv(): #Function that returns a three digit random number to be used as the CVV of the fake credit card
    return str(random.randint(100,999))

def makeFakePinNum(): #Function that returns a 4 digit random number to be used as the PIN number for the credit card (some sites ask for this)
    return str(random.randint(1000,9999))

def makeFakeDOB(): #Function that creates a random date of birth in the form "MM/DD/YYYY"
    month=str(random.randint(1,12))
    day=str(random.randint(1,28))
    year=str(random.randint(1970,2002))
    return "{}/{}/{}".format(month,day,year)

def makeFakeSSN(): #Function that creates a fake Social Security Number in the form "###-##-####"
    firstOne=str(random.randint(100,999))
    secondOne=str(random.randint(10,99))
    thirdOne=str(random.randint(1000,9999))
    return "{}-{}-{}".format(firstOne,secondOne,thirdOne)

def makeFakePhoneNum(): #Function that creates a fake phone number in the form "(+1)###-###-####"
    firstOne=str(random.randint(100,999))
    secondOne=str(random.randint(109,999))
    thirdOne=str(random.randint(1000,9999))
    return "(+1){}-{}-{}".format(firstOne,secondOne,thirdOne)


chars = string.ascii_letters + string.digits + '!@#$%^&*()' #Create a list of all possible characters for password generator to use
random.seed = (os.urandom(1024)) #Seed the random number generator

url='scam url here' #This is where you will copy/paste the link you found from the video demonstration

#Browser user agent header, eventually I'll make a function that selects from a list of possible headers to further obfuscate
headers = {'User-Agent': 'Mozilla/5.0 (Win64 x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36'} 

names = json.loads(open('names.json').read()) #Open the names.json file containing first names and create a list containing the entries
lastNames=json.loads(open('surnames.json').read()) #Open the surnames.json file containing last names and create a list containing the entries
emailAddresses=json.loads(open('emailDomains.json').read()) #Open the emailDomains.json file containing email domains and create a list containing the entries

while (1==1): #Run this forever
    try:  #Try/Catch to allow for error recovery like page timeouts
        randomName=random.randint(0,len(names)-1) #Select a random first name from the list
        randomLastName=random.randint(0,len(lastNames)-1) #Select a random last name from the list

        extraLength=random.randint(1,5)
        name_extra = ''.join(random.choice(string.digits) for i in range(extraLength)) #Create a string of 1-5 random characters to add onto front of name, useful for creating usernames and email addresses

        chosenAddress=str(random.choice(emailAddresses)) #Select a random email domain from the list

        #Randomly generated email which consists of "(randomly selected first name in lowercase) (1-5 random characters) @ (randomly selected email domain)"
        username = names[randomName].lower() + name_extra + "@" + chosenAddress

        passwordLength=random.randint(8,15)
        password = ''.join(random.choice(chars) for i in range(passwordLength)) #Create a randomly generated 8-15 digit password using the list of characters from earlier

        CreditCardNumber=makeFakeCCNum()   #Examples of calling each of the generator functions from the beginning of the code
        CreditCardExpDate=makeFakeCCexp()
        CreditCardCVV=makeFakeCCcvv()
        CreditCardPin=makeFakePinNum()
        FakeDOB=makeFakeDOB()
        FakeSSN=makeFakeSSN()

        requests.post(url, allow_redirects=False, data={  #Use the requests library to send the data in json format using an HTTP POST command, the names of each field will vary and you will need to use the video tutorial to find the ones for your case
            'cc': CreditCardNumber,
            'exp': CreditCardExpDate,
            'cvv':CreditCardCVV,
            'pin':CreditCardPin,
            'dob':FakeDOB,
            'mname': randomName,
            'sc': FakeSSN,
        },headers=headers)
        print 'sending packet:%s, %s, %s,%s,%s,%s,%s' % (CreditCardNumber,CreditCardExpDate, CreditCardCVV, CreditCardPin, FakeDOB, randomName, FakeSSN) #Mainly for debugging, just a statement to show what data points are being sent at the moment
    except:
        print "Error, restarting...\n" #If page times out (common through VPN), wait 5 seconds and restart
        time.sleep(5)