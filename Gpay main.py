import GP

H=GP.GooglePay("hayagriva20@gmail.com","9789910987","H")
H.OpenGpay()
H.EmailVerification()
H.MobileVerification()
H.NameVerification()
H.OtpVerification(15698,15698)
H.BankVerification()
H.PanCardVerification()
H.SetPin("3117")
H.EnteryourPin(3465,3465)


'''(Inheritance)'''

class Phone_pe(GP.GooglePay):                                                                                          
    def __init__(self,EmailID,Phonenumber,Name):
        super().__init__(EmailID,Phonenumber,Name)

    def Openphonepe(self):
        print("Phone pe")
        
N=Phone_pe("hayagriva20@gmail.com","9789910987","H")
N.Openphonepe()
N.MobileVerification()
N.NameVerification()
N.OtpVerification(780965,780965)
N.BankVerification()
N.PanCardVerification()
N.SetPin("12345")
N.EnteryourPin(3117,3117)


'''Transaction List'''
        
googlepay=[{"name":"anirudh","gpaynum":7397266887,"type":"personal","transaction":"regular"},                       
           {"name":"aarthi","gpaynum":7305341565,"type":"personal","transaction":"regular"},
           {"name":"abishek","gpaynum":6381347949,"type":"personal","transaction":"rare"},
           {"name":"afridi","gpaynum":7358451054,"type":"personal","transaction":"never"},
           {"name":"ajay","gpaynum":7200636126,"type":"personal","transaction":"rare"},
           {"name":"amritha","gpaynum":9591236931,"type":"personal","transaction":"rare"},
           {"name":"aruf","gpaynum":8056464565,"type":"personal","transaction":"regular"},
           {"name":"anandh","gpaynum":9962454833,"type":"personal","transaction":"rare"},
           {"name":"ananthu","gpaynum":8015341851,"type":"personal","transaction":"rare"},
           {"name":"benin","gpaynum":7305624091,"type":"personal","transaction":"rare"},
           {"name":"cathy","gpaynum":8939509826,"type":"personal","transaction":"rare"},
           {"name":"dumbo","gpaynum":6369121983,"type":"personal","transaction":"regular"},
           {"name":"jaan","gpaynum":9862241232,"type":"personal","transaction":"regular"},
           {"name":"jina","gpaynum":9941297487,"type":"personal","transaction":"rare"},
           {"name":"jananiya","gpaynum":7150801990,"type":"personal","transaction":"regular"},
           {"name":"balaji","gpaynum":6382880108,"type":"personal","transaction":"rare"},
           {"name":"belgin","gpaynum":9945654815,"type":"personal","transaction":"regular"},]

for i in googlepay:                                                                                                             
    for j,k in i.items():                                                                                                       
        print(f"{j}:{k}")
    
