class Phonetracking:

        def Whatsapp(self,mon,wed,fri):
            self.mon={"Screentime":45,"Notifications received":23,"Frequency":10}
            self.wed={"Screentime":20,"Notifications received":20,"Frequency":20}
            self.fri={"Screentime":60,"Notifications received":25,"Frequency":20}
            print("time spent on Whatsapp in the past week was:",mon+fri+sun)

        def Snapchat(self):
            self.mon={"Screentime":10,"Notifications received":10,"Frequency":25}
            self.wed={"Screentime":10,"Notifications received":10,"Frequency":25}
            self.fri={"Screentime":10,"Notifications received":10,"Frequency":25}
            print("time spent on snapchat in the past week was:",mon+fri+sun)

        def Youtube(self):
            self.mon={"Screentime":20,"Notifications received":2,"Frequency":2}
            self.wed={"Screentime":20,"Notifications received":0,"Frequency":2}
            self.fri={"Screentime":10,"Notifications received":3,"Frequency":2}
            print("time spent on Youtube in the past week was:",mon+fri+sun)


        def Instagram(self):
            self.mon={"Screentime":45,"Notifications received":47,"Frequency":8}
            self.wed={"Screentime":55,"Notifications received":23,"Frequency":6}
            self.fri={"Screentime":45,"Notifications received":10,"Frequency":10}
            print("time spent on Instagram in the past week was:",mon+fri+sun)


Return = Phonetracking()
Return.Whatsapp(mon,wed,fri)
Return.Snapchat(mon,wed,fri)
Return.Youtube(mon,wed,fri)
Return.Instagram(mon,wed,fri)

