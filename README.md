# Phishermen's Nightmare

I saw a YouTube video where a programmer received a phishing attempt in his email and proceeded to create a Python program to flood the scammer's database with fake personal data. I liked the idea and copied it but I noticed he never updated the code and there were some improvements that could be made. I decided to make those improvements are occasionally add new functions whenever I see the need.


## Original Project

The original project video is on the **Engineer Man** YouTube Channel and is a good demonstration of the process of writing the code and finding the exact URL that the post request needs to use. I recommend watching this video and follow his method for finding the URL. My code was heavily based off of his code linked in the description of the video.
Original video: https://www.youtube.com/watch?v=UtNYzv8gLbs

## Modifications

The original project was good but it had a few flaws. All the emails were a first name and a single digit followed by "@yahoo.com". Additionally, all the passwords were 8 characters long. A smart person could probably run a command in their database to find all entries from yahoo with 8-character passwords. I modified the code to be a bit smarter.
* Passwords are now anywhere between 8 and 15 characters in length, randomly generated for each entry
* Email addresses now have between 1 and 5 numbers trailing the name and before the "@"
* The code now selects from a decent list of possible email domains and selects a new one for each generated entry
## Additions

Some phishing sites ask for more then just a username and password, some ask for credit card details, maiden names, or even social security numbers! I created a few simple functions to generate some of these common bits of info and will add more as I see the demand. Each of the functions needs to parameters when it is called and it simply returns a string with the data. The functions I have so far create:
* Credit Card Numbers (currently just random numbers but I hope to incorporate the algorithm such that cards numbers are the correct pattern)
* Credit Card CVV and PIN numbers (literally just returning either 3 or 4 random digits)
* Credit Card Expiration Dates (just returns the a string with a month/year in 2-digit number form)
* Date of Birth (returns a string with the 2-digit day and month and a 4-digit year in MM/DD/YYYY format)
* More to come soon!

## Final Remarks
This code is written in Python 2.7.16 and you need to have the "requests" module installed in order for this code to work
