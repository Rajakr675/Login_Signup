
print("1).signup or 2).login or 3).remove -file")
import os
def choice():

    n=int(input("enter  your choice:- "))
    if n==1:
        return signup()
    elif n==2:
        return login()
    elif n==3:
        return remove()


def signup():
    userData = {"name": input("Enter your name: "), "email": input('Enter your email ID: '), "password": input('Enter your password: ')}
    f=open("data.txt","a")
    f.write(f"{userData}")
    f.write("\n")
    print('Successfully your signup is done.')    
def login():
    if os.path.exists("data.txt"):
        email = input('Enter your email: ')
        email = f'{email}'
        password2=input('Enter your password: ')
        password2 = f'{password2}'
        f1=open("data.txt", "r")
        data1=f1.read()
        
        if email in data1 and password2 in data1:
            c=""
            l=[]
            for i in data1:
                if i!="\n":
                    c=c+i
                else:
                    l.append(c)
                    c=""
            for j in l:
                if email in j and password2 in j:
                    print(j)
                    break

            else:
                print('Either of the user detail is wrong, pleaase check it once!!')            
        else:
            print('Sorry not exist your details!!')
    else:
        print("File does not exist!!")

def remove():
    if  os.path.exists("data.txt"):
        os.remove("data.txt")
        print("The file is deleted.")
    else:
        print("The file does not exist!!")

    

choice()


# var = "{'name': 'vikash', 'age': 5}"
# print(type(*var))
