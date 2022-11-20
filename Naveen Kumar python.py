num=int(input("enter the number"))
if (num%2==0):
    print("its an even number")
else:
    print("its an odd number")

    
def login():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if username == "naveen" and password == "12345":
        print("welcome naveen!")
    else:
        print("Invalid username or password.")

login()


# create a list of fruits and iterate through them.

fruits = ["apple", "gauva", "orange", "jackfruit", "grapes"]

for x in fruits:
  print(x)
