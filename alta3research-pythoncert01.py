#!/usr/bin/python3

"""
This is a basic python program for retrieving your weekly horoscope

Uses:
* API request
* Uses pandas to create dataframe and export to different file format (json,csv,excel)
* Loop until providing the right input
* uses crayon library if the the user input  invalid value (red) and valid value (green)
* make case-insensitive

-rvardeleon| Python3 Basic

"""

# use for API calls
import requests
# use to change the text color
import crayons
# use to import file to different format
import pandas as pd
# use to check the current OS type
from os import system, name


WEEKLUCK = "http://horoscope-api.herokuapp.com/horoscope/week/"


# Contain Header  and Validate the user enter the right value 
def SUNSIGN():
    print('\n\n' + 'Your Weekly Horoscope' + '\n\n')

    # String as inout
    SIGN = str(input("Please enter your zodiac sign--> "))

    # Make  case-insensitive key
    SIGN = SIGN.lower()

    # Loop if the input is in valid
    while SIGN  not in ["aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagittarius","capricorn","aquarius","pisces"]:

        # Print  text red if input is invalid 
        print(crayons.red("Entered invalid zodiac sign, Please try again" + "\n\n"))

        # open a file and provide the right choices
        f = open('horoscopesigns.data', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()

        SIGN = str(input("Please pick your Zodiac valid  sign: "))
        SIGN = SIGN.lower()
        clearscreen() # clear the screen
        print('\n\n' + 'Your Weekly Horoscope' + '\n\n')
        
    clearscreen() # clear the screen
    print(crayons.green("\n\n" + "Your Zodiac Sign is:  {}".format(SIGN)))
    return SIGN


# define Screen  clear function
def clearscreen():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


def main():

     # grab the Zodiac sign input
     SIGN = SUNSIGN()

     # make API lookup
     r = requests.get(WEEKLUCK + SIGN)

     # test the response eq 200 
     if r.status_code != 200:
        print(r.status_code)
        print(r.json())
        exit()
     
     # Ouput the API request to a JSON file
     data = r.text
     f = open("WEEKLUCK.json","w")
     f.write(data)
     f.close()



     # get the JSON API response
     r = r.json()

     # open file to write the output data (Creates a new file if it does not exist or truncates the file if it exist)s
     with open("WEEKLUCK.data", "w") as f:

        # Three blank lines
        print("\n\n\n")

        # write out Zodiac sign , Zodiac - blue color text
        f.write(crayons.blue("Zodiac: ", bold=True) + r.get("sunsign") + "\n\n")

        # write out week ,  Week - blue color text
        f.write(crayons.blue("Week: ", bold=True) + r.get("week") + "\n\n")
    
        # write out Horoscope Your Horoscope - blue color text
        f.write(crayons.blue("Your Horoscope: ", bold=True) + r.get("horoscope") + "\n\n")

        # add blank lines
        f.write("\n\n")
     
     # Open the output file
     f = open('WEEKLUCK.data', 'r')

     # read the contents
     file_contents = f.read()

     # Display to terminal
     print (file_contents)
     f.close()

     # export file to different format using pandas
     # define name of json file
     json_file = 'WEEKLUCK.json'

     # create a dataframe oject, only cantains key value pairs (type=series)
     data_json = pd.read_json(json_file, typ='series')

     # import JSON to CSV file
     data_json.to_csv("WEEKLUCK.csv")

     # import JSON to Excel file
     data_json.to_excel('WEEKLUCK.xlsx')

if __name__ == "__main__":
    main()
