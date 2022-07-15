from datetime import date
import datetime

person_list=[{'name':'Amy','DOB':date(1987,5,3),'nationality':'Australia'},{'name':'Bob','DOB':date(1989,3,4),'nationality':'Australia'},{'name':'Cindy','DOB':date(1988,5,2),'nationality':'India'},{'name':'Emma','DOB':date(1990,5,23),'nationality':'New Zealand'}]

# Check if name is in the list of person
def check_name(name):
    for p in person_list:
        if name == p['name']:
            return True
    return False

# Check if key is in the list of key
def check_key(key):
    if key in person_list[0].keys():
        return True
    return False

# Check if date of birth is valid or not
def check_date(year,month,day):
    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        return False
    return True

def alter():
    # Input name, key and value that want to be changed and check if they are valid
    print('Input the name that you want to make changes with:')
    name=input()
    if check_name(name)==False:
        print('Name not found!')
    else:
        print('Input the key that you want to make changes with:')
        key=input()
        if check_key(key)==False:
            print('Key not found!')
        
        # If every input are valid, go for the altering processes
        else:
                if key=='DOB':    
                    print('Input the new year that you want to set:')
                    year=int(input())
                    print('Input the new month that you want to set:')
                    month=int(input())
                    print('Input the new day that you want to set:')
                    day=int(input())
                else:
                    print('Input the new value that you want to set:')
                    value=input()
                
                print('List before change:\n', person_list)
                for p in person_list:
                    
                        if key=='DOB':
                            if check_date==False:
                                print('DOB is invalid!')
                            else:
                                p[key]=date(year,month,day)
                        else:
                            p[key]=value
                        name_found=True
                        print('Change done!')
                        print('List after change:\n',person_list)


alter()