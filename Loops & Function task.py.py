#to register
#u need fIRST AND LAST NAME and password, email
#generate user account

#to login:
#(email) and password

#bank operations

#1. to initialize system:
import random
import datetime 

database = {44328: ["louisa", "okogwu", "louiloui@gmail.com", "louiloui", 500000]

} #dictionary

e = datetime.datetime.now()


print ("Today's date is  %s/%s/%s" % (e.day, e.month, e.year))



def initializing():

    print ("The time now is  %s:%s" % (e.hour, e.minute))
    print("Welcome to AlphaOmega bank! How can we serve you today?")

      #important so that if one chooses a false option it will take them back to do you have an account with us
    HaveAccount = int(input("Do you have an account with us?: 1 (Yes) 2 (No) \n")) 
      #if it's  a yes or no just add it straight up to the input
                               #depending on their answer they can either go straiht to login or they register.
    if(HaveAccount == 1):
            
        login()
    elif(HaveAccount ==2):
            
        print(register())
    else:
        print("You have selected an invalid option, please try again!")
        initializing()    


#5. generate account number 
def generateACCOUNTNUMBER():
    print("This is your account number")
                                                    #user doesnt need to see              #so they can use their 2acc number later
    return random.randrange(11111,99999)


           

#2. to create a login function use the def function
#to login:
#(email), acc num, and password

def login():
    print("***Login***")



    useraccountnumber = int(input("Enter your Account Number \n"))

    validAccountnumber = accountnumberValidation(useraccountnumber)

    if validAccountnumber:

        password = input("Enter your password \n")



    for accountnumber, userdetails in database.items():
        if(accountnumber == (useraccountnumber)):  #add int
            
        
            if(userdetails[3] == password):

                bankoperations(userdetails) 
            else:
                          #put in the user details 2in bank operations.
                print("Invalid account number or password, please try again!")
                login()
        else:
                          #put in the user details 2in bank operations.
                print("Invalid account number, please try again!")
                login()
    

    else:
        initializing()

    
                    

#user validation
def accountnumberValidation(accountnumber):
    #check if acc number is not empty
    #check if account number is 5 digits   use len(variable)
    #check if account number is an integer use try exceppt

    if accountnumber:

        if len(str(accountnumber)) == 5:                                        #to make sure it is a 5 digit, first convert to a string
            
            try:
                int(accountnumber) 
                return True        #why cant we use if 
            except ValueError:

                print("Invalid Account number, account number should be an integer")

                login()  
   
            except TypeError:
                print("Invalid")
                return False      
            


        
        else:
            print("Account number should be 5 digits")
            return False

    else:

        print("Account Number is required")  

        
        initializing()


                  #because in the deatils, password is in range 3 thus 3rd index[]



#3. to create a register function #to register
#u need username and password, email
#generate user account
def register():

    print("***Register***")

    email=input("What is your email address? \n")
    firstname = input("what is your First name? \n")
    lastname = input("What is your Last name? \n")
    password = input("create a password \n")

    accountnumber = generateACCOUNTNUMBER()   #calling the #5. function
    
    database[accountnumber] = [firstname,lastname,email,password, 0] 
    
    #return database #to be sure instead call the login function so that they can login afyter registr   #print("this is the register function"
    
    
    print("Your Account has been created")
    print("== === ===== === ==")

    print("Your account number is %d" % accountnumber)
    print("Make sure you keep it safe")

    print("== === ===== === ==")

    login()  #so you go straigh to login






#4. to create a operational  function
def bankoperations(userdetails):  #comes in after login
    print("Welcome %s %s! " % (userdetails[0], userdetails[1]))


        
    differentoptions = int(input("What would you like to do?: 1 (Withdrawal) 2 (Deposit) 3 (Balance) 4 (Complaint) 5 (Logout) 6 (Exit) \n"))

    if (differentoptions == 1):
        
        Withdrawal(userdetails)

    elif(differentoptions == 2):
        
        Deposit(userdetails)

    elif(differentoptions==3):
        
        Balance(userdetails)

    elif(differentoptions==4):
        
        Complaint(userdetails)

    elif(differentoptions ==5):
        
        login()
    elif(differentoptions == 6):
        
        Exit()

    else:

        print("You have selected an invalid option, please try again!")
        bankoperations(userdetails)

               #we are gonna define each of the operations


def anotherTransaction(userdetails):
    anotherTransactionn = int(input("Would you like to perform another transaction?: 1 (Yes)  2 (No) \n"))

    if(anotherTransactionn == 1 ):
        bankoperations(userdetails)

    elif(anotherTransactionn == 2):
        print("Thank you for banking with us today")
        login()
       

    else:

        print("You have selected an invalid option, please try again!")

        anotherTransaction(userdetails)

def advancedoptions(userdetails):
    advancedoption = int(input("Would you like to check our advanced options?: 1 (Yes)  2 (No) 3 (Return) \n"))

    if(advancedoption == 1 ):

        preferableservices(userdetails)   

    elif(advancedoption == 2):
        print("Thank you for banking with us today, have a nice day!")
        login()

    elif(advancedoption==3):
        Complaint(userdetails)    

    else:
        print("Invalid option, please try again" )
        advancedoptions(userdetails)


def preferableservices(userdetails):
    whatcanwehelpwith = int(input("What is your preferable mode of service: 1 (Customer service number)  2 (Customer service email) 3 (Return) \n"))

    if (whatcanwehelpwith == 1):
            print("Our customer Service number is '2233455' ")
            anotherTransaction(userdetails)

            print("Thank you for banking with us today!")
            anotherTransaction(userdetails)

    elif(whatcanwehelpwith ==2):
            print("Our customer Service email is 'loui@alphaomegabank' ")
            print("Thank you for banking with us today!") 

    elif(whatcanwehelpwith== 3):

        advancedoptions(userdetails)       
    else:
            print("Invalid option, please try again" )   

            preferableservices(userdetails)      

def Withdrawal(userdetails):
    withdrawal = int(input("How much would you like to withdraw? \n"))
    if(withdrawal < userdetails[4]):
                print("Thank you for banking with us please take your cash.")

                anotherTransaction(userdetails)
    else:
        print("Insufficient funds, try again!")
        Withdrawal(userdetails)
    

#get current bal, check amount to wothdraw  n check if curr bal is > withdrawal. deduct withdrawn amoun
# t

def Deposit(userdetails):
    cashdeposit= int(input("How much would you like to deposit? \n"))
    if(cashdeposit >0):
        userdetails[4] = (cashdeposit + userdetails[4])
        print("Your account has been credited.")

        print("Your current balance is %d."  % userdetails[4])
    else:
        print("Invalid, please deposit a higher amount")


    anotherTransaction(userdetails)     
           

def Balance(userdetails):

    print("Your current balance is %d" % userdetails[4])


    anotherTransaction(userdetails)

    
    

def Complaint(userdetails):
    input("What issue would you like to report? \n" )
    print("Thank you for contacting us %s, our support center will get back to you within 3 working days" % userdetails[0])

    advancedoptions(userdetails)
        


def Logout():
    print("Thank you for banking with us")
    login()

def Exit():
    Exit
       

###LET US SEE HOW 1. TURNS OUT###
initializing()
#initializing()
#print("Your account number is %s" % generateACCOUNTNUMBER())
#print(generateACCOUNTNUMBER())