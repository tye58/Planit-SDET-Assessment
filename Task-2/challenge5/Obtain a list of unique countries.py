from datetime import date

person_list=[{'name':'Amy','DOB':date(1987,5,3),'nationality':'Australia'},{'name':'Bob','DOB':date(1989,3,4),'nationality':'Australia'},{'name':'Cindy','DOB':date(1988,5,2),'nationality':'India'},{'name':'Emma','DOB':date(1990,5,23),'nationality':'New Zealand'}]

# Is "unique countries" means the countries that only appear once?
def get_unique_country(person_list):
    unique_country=[]
    for person in person_list:
        unique_country.append(person['nationality'])
    
    unique_list = [i for i in unique_country if unique_country.count(i) == 1]
    print('The countries that only appear once (unique countries) are',unique_list)

get_unique_country(person_list)