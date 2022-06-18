#! usr/bin/python3
from sys import argv 
import datetime
import argparse
def capitalize(name):
    a = set()
    a.add(name.capitalize())
    a.add(name.upper())
    a.add(name.lower())
    a.add(name.title())
    return a
def create(f,l,name):
    
    wordlist = capitalize(name)
    for d in range(f,l):
        d = str(d)
      #  print(f"Calculating from {f} to {l}")

        for w in wordlist:
            print (w+d)
            print(w+'-'+d)
    for w in wordlist:
        for i in range(5):
            for j in ['1','2','3','4','5']:
                print(w+j*i)

f = 2005
l = datetime.datetime.now().year

ap = argparse.ArgumentParser()
ap.add_argument("name" ,help="name of wifi or other keyword")
ap.add_argument("-f","--first",type=int,help ="first date(defaults to 2005")
ap.add_argument("-l","--last",type=int,help="last date(drfaults to current year)")
args = vars(ap.parse_args())


ft = args["first"] 
lt = args["last"]

#try: 
#    f = int(ft)
#    l = int(lt)
#except ValueError:
#    if (ft != "" or lt != ""):
#        exit(1)
   
name = args["name"]


create(f,l,name)

    

