#! /usr/bin/python3
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
        
        l = ['1','2','3','4','5']
        for i in range(5):

            for n,j in enumerate(l):
                print(w+j*i)
        for i in range(10):    
            print(w+ "".join(l[:i]))
            print(w+"-"+"".join(l[:i]))
f = 2005
l = datetime.datetime.now().year

ap = argparse.ArgumentParser()
ap.add_argument("-n","--name" ,action = 'append',help="name of wifi or other keyword")
ap.add_argument("-f","--first",type=int,help ="first date(defaults to 2005")
ap.add_argument("-l","--last",type=int,help="last date(drfaults to current year)")
ap.add_argument("-p","--phone",action='append',help="phone/anything  else")
ap.add_argument("-o","--load",help="load extra wordlist")

args = vars(ap.parse_args())


ft = args["first"] 
lt = args["last"]

#try: 
#    f = int(ft)
#    l = int(lt)
#except ValueError:
#    if (ft != "" or lt != ""):
#        exit(1)
common = {
        "123456",
        "123456789",
        "qwerty",
        "password",
        "12345",
        "qwerty123",
        "1q2w3e",
        "12345678",
        "111111",
        "1234567890"

        }
if (args["load"] != None):
    with open(args["load"],'r') as load:
        lines = load.readlines()
        for line in lines:
            common.add(line)
if (args["phone"] != None):
    for p in args["phone"]:
        common.add(p)
[print(c) for c in common]

if args["name"] != None:
    for name in args["name"]:
        create(f,l,name)

    

