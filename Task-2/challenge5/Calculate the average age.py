from datetime import date

from numpy import average

person_list=[{'name':'Amy','dob':date(1987,5,3),'nationality':'Australia'},{'name':'Bob','dob':date(1989,3,4),'nationality':'Australia'},{'name':'Cindy','dob':date(1988,5,2),'nationality':'India'},{'name':'Emma','dob':date(1990,5,23),'nationality':'New Zealand'}]

# Calculate age
def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def ave_age(person_list):
    age_list=[]
    for person in person_list:
        age_list.append(age(person['dob']))
    print(age_list)
    return average(age_list)
