#Midterm Assignment
#Oct. 17 2020

import re
import urllib.request
import json

api = 'https://api.exchangerate-api.com/v4/latest/'
###################################################################################################
def valid_countryCode(code):
    regexp = re.compile(r'^[a-zA-Z]{3}$')
    if not regexp.search(code):
        print("Invalid currency code {}".format(code))
        return False
#####################################################################################################
def page_exists(page):
    try:
        print(page)
        urllib.request.urlopen(page)
        return True
    except:
        return False
#######################################################################################################
def converter(FROM, TO, amount):
    if(page_exists(api+FROM)):
        page = urllib.request.urlopen(api+FROM) #open correct website after checking if it exists
        content = page.read().decode("utf-8") #keep in mind the byte string needs to be decoded; read and save whatevers on webpage
        data = json.loads(content) #take entire URL page in json format and store it in a variable; data has type dictionary with inner dictionaries
        if not data:
            return "Country code(s) doesn't exist"
        rates = data["rates"][0] #possibly don't need the [0]#Midterm Assignment
#Oct. 17 2020

import re
import urllib.request
import json
import sys

api = 'https://api.exchangerate-api.com/v4/latest/'
###################################################################################################
def valid_countryCode(code):
    regexp = re.compile(r'^[A-Z]{3}$')
    if not regexp.search(code):
        print("Invalid currency code {}".format(code))
        return False
#####################################################################################################
def page_exists(page):
	try:
		urllib.request.urlopen(page)
		return True
	except:
		return False
#######################################################################################################
def conversion(rate, amount):
  return (rate * amount)
#######################################################################################################
def converter(FROM, TO, amount):
    if(page_exists(api+FROM)):
        page = urllib.request.urlopen(api+FROM) #open correct website after checking if it exists
        content = page.read().decode("utf-8") #keep in mind the byte string needs to be decoded; read and save whatevers on webpage
        data = json.loads(content) #take entire URL page in json format and store it in a variable; data has type dictionary with inner dictionaries
        if not data:
            return "Country code(s) doesn't exist"
        #check to see if country code exists
        if TO in data["rates"]:
          rates = data["rates"][TO]
        else:
          return "Country code(s) doesn't exist"
        if not rates:
            return "Country code(s) doesn't exist"
    else:
        return "ERROR: Invalid API endpoint"
  
    converted = conversion(rates, amount)
    return "{} in {} = {} in {}".format(amount, FROM, converted, TO)
####################################################################################################
def main():
  go = True
  while go == True:
      amount = input("Enter amount to be converted (q to quit):    ")
    
      if amount.lower() == 'q':
          print("See you next time!")
          go = False
          break
      else:
          regexp = re.compile(r'^[0-9]+(\.[0-9]{1,2})?$')
          if not regexp.search(amount):
            print("Invalid input {}".format(amount))
            continue
      amount = float(amount) #make str a float value for later on math function

       #use upper function to handle lowercase letters
      FROM = input("Enter FROM currency 3 letter code:    ").upper()
      valid1 = valid_countryCode(FROM.upper())    #use validation function here
      if valid1 == False:
        continue
      #use upper function to handle lowercase letters
      TO = input("Enter TO currency 3 letter code: ").upper()
    
      valid2 = valid_countryCode(TO)    #use validation function here
      if valid2 == False:
        continue
      print(converter(FROM, TO, amount))
#######################################################################################      
if __name__ == '__main__':
  main()
        if not rates:
            return "Country code(s) doesn't exist"
    else:
        print("ERROR: Invalid API endpoint")
        return "Country code(s) doesn't exist"
    exchangeRate = rates[TO]
    print(exchangeRate)
    converted = amount * exchangeRate
    print(converted)
    return "{} in {} = {} in {}".format(amount, FROM, converted, TO)
####################################################################################################
go = True
while go == True:
    amount = input("Enter amount to be converted (q to quit):    ")
    
    if amount.lower() == 'q':
        print("See you next time!")
        go = False
        break
    else:
        regexp = re.compile(r'^[0-9]+(\.[0-9]{1,2})?$')
        if not regexp.search(amount):
             print("Invalid input {}".format(amount))
             continue

    FROM = input("Enter FROM currency 3 letter code:    ")
    valid1 = valid_countryCode(FROM.upper())    #use validation function here
    if valid1 == False:
        continue
    TO = input("Enter TO currency 3 letter code: ")
    valid2 = valid_countryCode(TO.upper())    #use validation function here
    if valid2 == False:
        continue
    print(converter(FROM, TO, amount))
#######################################################################################      
