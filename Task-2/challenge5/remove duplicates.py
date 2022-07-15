from datetime import date

person_list=[{'name':'Amy','DOB':date(1987,5,3),'nationality':'Australia'},{'name':'Bob','DOB':date(1989,3,4),'nationality':'Australia'},{'name':'Cindy','DOB':date(1988,5,2),'nationality':'India'},{'name':'Emma','DOB':date(1990,5,23),'nationality':'New Zealand'},{'name':'Amy','DOB':date(1987,5,3),'nationality':'Australia'},{'name':'Sandy','DOB':date(1987,5,3),'nationality':'Australia'}]

def remove_duplicates(person_list):
    print("The original person list:\n",person_list)
    seen = set()
    new_l = []
    for d in person_list:
        t = tuple(sorted(d.items()))
        if t not in seen:
            seen.add(t)
            new_l.append(d)
    print("The person list after duplicate removal:\n",new_l)

remove_duplicates(person_list)