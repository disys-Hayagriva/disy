class GooglePay:                                                                                   
    
    '''(FUNCTION)'''
    
    def __init__(self,EmailID,Phonenumber,Name):                                                                  
        self.emailid=EmailID
        self.mobile=Phonenumber
        self.name=Name
        
    def OpenGpay(self):
        print("Google Pay")
        
    '''(Value Validation)'''
    
    def EmailVerification(self):  
        if type(self.emailid) == str:                                                                               
            if len(self.emailid) <= 30:                                                                              
                print("email-id verified")
            else:
                raise ValueError("the email-Id should not contain more 30 values")
        else:
            raise TypeError("invalid emailid")


    '''(TYPE VALIDATION)'''
    
    def MobileVerification(self):                      
        if (len(self.mobile)==10):
            if type(self.mobile) == str:                                                                            
                print("phone number verified")
            else:
                raise TypeError("the phone should contain only integers ")
        else:
            raise ValueError("the phone number should not be grater than or lesser than 10")
        

    '''(To verify/validate the length)'''
    
    def NameVerification(self):
        if type(self.name) == str:                     
            if len(self.name) <= 20:                                                                                
                print("name verified")
            else:
                raise ValueError("The name should contain lesser than or equal to 20 letters")
        else:
            raise TypeError("The name should contain letters only")

    def OtpVerification(self,code,otp):
        if(otp==code):
            print("otp verified")
        else:
            raise ValueError("The otp you are entered is not correct")

    def BankVerification(self):
        self.Account=[]
        self.Accountnumber=3426789012
        self.CVV=924
        self.Account.append(self.Accountnumber)                                                                
        print(self.Account)
        print("Bank account Verified")

    def PanCardVerification(self):
        self.pannumber="RTYUI2345B"
        if (len(self.pan_number) == 10):
            print("pan card verified")
        else:
            raise ValueError("Inavlid Pan_number")

    def SetPin(self,number):
        self.pin=number
        if (len(self.pin)==4 or len(self.pin) ==6):
            print("your pin is successfully created")
        else:
            raise ValueError("Invalid pinnumber")

    def EnteryourPin(self,match,pin):
        self.match=match
        self.pin=pin
        if self.match==self.pin:
            print("DONE")
        else:
            raise ValueError("pin not matched")








    
