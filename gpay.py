import GP

hay=GP.GooglePay("hayagriva20@gmail.com","9789910987","Hayagriva Narayanan")
hay.OpenGpay()
hay.EmailVerification()
hay.MobileVerification()
hay.NameVerification()
hay.OTPVerification(15698,15698)
hay.BankVerification()
hay.SetPin("5114")
hay.EnteryourPin(2324,2324)

'''class Phone_pe(gp.GooglePay):                                                                                          
    def __init__(self,Email_ID,Phone_number,Name):
        super().__init__(Email_ID,Phone_number,Name)

    def open_phonepe(self):
        print("Phone pe")'''

        

for i in googlepay:                                                                                                             
    for j,k in i.items():                                                                                                       
        print(f"{j}:{k}")
