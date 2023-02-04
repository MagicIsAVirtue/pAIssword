import sklearn
from sklearn import cluster
import sys
from difflib import SequenceMatcher

#Opens files
first_name = open("first_names.txt", "r")
last_name = open("last_names.txt", "r")
five_hundred = open("500-worst-passwords.txt", "r")

#Define some variables so that computer happy
try:
    password = sys.argv[1]
except:
    print("Usage: pAIssword.py [password_to_check]")
    quit()

#Unique Symbols --\
#Capital Letters -- Distribution of unique characters
#Numbers ---------/

#Length
pass_length = len(password)


#Similarity to breached passes or names
#*Gets the list of known names (github.com/smashew/NameDatabases)
names = first_name.readlines()
names.extend(last_name.readlines())


#*Gets the list of worst passwords (github.com/danielmiessler/SecLists)
worst_passwords = five_hundred.readlines()

#*Compares password to the 500 worst ones, and then names

highest_breach_match = 0
for word in worst_passwords:
    breach_percentage = SequenceMatcher(None, word, password).ratio()
    highest_breach_match = max(highest_breach_match, breach_percentage)

print(highest_breach_match)

highest_name_match = 0
for name in names:
    name_percentage = SequenceMatcher(None, name.lower(), password.lower()).ratio()
    highest_name_match = max(highest_name_match, name_percentage)

print(highest_name_match)


#Closes files
first_name.close()
last_name.close()
five_hundred.close()
