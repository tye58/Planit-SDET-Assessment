from datetime import date

person_list=[{'name':'Amy','DOB':date(1987,5,3),'nationality':'Australia'},{'name':'Bob','DOB':date(1989,3,4),'nationality':'Australia'},{'name':'Cindy','DOB':date(1988,5,2),'nationality':'India'},{'name':'Emma','DOB':date(1990,5,23),'nationality':'New Zealand'}]

def copy_list(person_list):
    print('The duplicated list is:')
    return person_list.copy()

print(copy_list(person_list))