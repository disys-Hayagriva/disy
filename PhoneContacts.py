class PhoneContacts:                                                                                   

    '''Functions'''
    
    def __init__(self,Firstname,Lastname,Phone_number,Email_ID,Groups,DOB):                            
        self.firstname=Firstname
        self.lastname=Lastname
        self.phonenumber=Phone_number
        self.emailid=Email_ID
        self.groups=Groups
        self.dob=DOB
        
        
    def Openphcontacts(self):
        print("Phone Contacts")
    
        
    def FirstnameVerification(self):
        if type(self.firstname) == str:
            if len(self.firstname) <= 15:                                                                                
                print("Firstnameame verified")
            else:
                raise ValueError("Firstnameame should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Firstname should contain letters only")
        
    def LastnameVerification(self):
        if type(self.lastname) == str:
            if len(self.lastname) <= 15:                                                                                
                print("Lastnameame verified")
            else:
                raise ValueError("Lastnameame should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Lastname should contain letters only")
        
    def PhonenumberVerification(self):
        if (len(self.phonenumber)==10):
            if type(self.phonenumber) == str:                                                                            
                print("Phone number verified")
            else:
                raise TypeError("Phone number should contain only integers ")
        else:
            raise ValueError("phone number should not be grater than or lesser than 10")
        
    def EmailidVerification(self):
        if type(self.emailid) == str:                                                                               
            if len(self.emailid) <= 25:                                                                              
                print("Emailid verified")
            else:
                raise ValueError("Emailid should not contain more than 25 values")
        else:
            raise TypeError("Invalid emailid")    
        

    def GroupsVerification(self):
        if type(self.groups) == str:

            '''Len function'''
            
            if len(self.groups) <= 10:                                                                              
                print("Groups verified")
            else:
                raise ValueError("Groups should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("Groups should contain letters only")

    '''Isinstance'''
    def DobVerification(self):
        if isinstance(self.dob,str):                                                                                

            '''Len Function'''
            
            if len(self.dob) <= 10:                                                                                 
                print("DOB verified")
            else:
                raise ValueError("DOB should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("DOB should contain numbers and symbols only")   
   


H=PhoneContacts("hayagriva","narayanan","9789910987","hayagriva20@gmail.com","Family","17/04/2000")
H.Openphcontacts()
H.FirstnameVerification()
H.LastnameVerification()
H.PhonenumberVerification()
H.EmailidVerification()
H.GroupsVerification()
H.DobVerification()



        
phone=[{"Firstname":"janani","Lastname":"narayanan","Phno":9854268725,"Email_id":"mjanani31@gmail.com","Groups":"Family","DOB":"31/03/2000"},                                  
           {"Firstname":"hayagriva","Lastname":"narayanan","Phno":9987968725,"Email_id":"hayagriva20@gmail.com","Groups":"Friends","DOB":"17/04/2000"},]


'''Looping'''

for i in phone:                                                                                                             
    for j,k in i.items():                                                                                                     
        print(f"{j}:{k}")

    
