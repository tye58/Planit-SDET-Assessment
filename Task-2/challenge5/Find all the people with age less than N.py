from datetime import date

person_list=[{'name':'Amy','dob':date(1987,5,3),'nationality':'Australia'},{'name':'Bob','dob':date(1989,3,4),'nationality':'Australia'},{'name':'Cindy','dob':date(1988,5,2),'nationality':'India'},{'name':'Emma','dob':date(1990,5,23),'nationality':'New Zealand'}]

# Calculate age
def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Find people with less age than N
def less_age(person_list,N):
    less_age_list=[]
    for person in person_list:
        person['age']=age(person['dob'])
        if person['age']<N:
            less_age_list.append(person['name'])
    print('People with age less than',N,'is(are)',less_age_list)
    return less_age_list


less_age(person_list,34)