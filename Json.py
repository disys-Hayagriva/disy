db = {"customer": {"10": {"ID": "1000", "name": "H ", "DOB": "17/04/2000", "Gender": "M", "Age": "20","Zip code": "08145-2323", "Amount ": "1467.20"},"2000": {"ID": "2000", "name": "Jina ", "DOB": "03/03/2000", "Gender": "F", "Age": "25","Zip code": "08136-2324","Amount ": "1500.20"},"20": {"ID": "20", "name": "Fama", "DOB": "01/04/1999", "Gender": "M", "Age": "25","Zip code": "08124-6565","Amount ": "1500.20"}}}
for i in db.values():
     #print(i)
     for j in i.values():
          for k,l in j.items():
               if k == "Age" and int(l)>25:
                    print(j,l)
               else:
                    print("No Customer Found in the Database")
               break
