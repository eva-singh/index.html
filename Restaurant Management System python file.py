import pickle
import math
# User Defined Functions/Methods
L=[]
price=[]
#functions for admin login
def addrecord():
    try:
with open('ecar.dat','rb+')as F: L=pickle.load(F)
while True:
itemno=int(input('item no: ')) itemname=input('item name: ') itemprice=int(input('item price: ')) L1=[itemno, itemname, itemprice] L.append(L1)
                more=input('more?')
                if more in 'noNONo':
break F.seek(0)
pickle.dump(L,F)
            print('option 1')
    except:
print('option 2')
L=[]
with open('ecar.dat','wb')as F:
while True:
itemno=int(input('item no: ')) itemname=input('item name: ') itemprice=int(input('item price: ')) L1=[itemno, itemname, itemprice] L.append(L1)
more=input('more?')
if more in 'noNONo':
break pickle.dump(L,F)
def displaymenu():
with open('ecar.dat','rb')as F:
data=pickle.load(F)
         for i in data:
            print(i)
def editrecord():
with open('ecar.dat', 'rb+')as F:
L=pickle.load(F) while True:
                n=int(input('which item would you like to edit? (enter item
number) (enter 0 to exit)'))
                for i in L:
                    if i[0]==n:
                        print(i)
                        while True:
reply=int(input('what would you like to edit? 1-refno, 2-name, 3-price, 4-complete record, 5-done'))
        if n==0:
            break
F.seek(0) pickle.dump(L,F)
def deleterecord():
with open('ecar.dat', 'rb+')as F:
L=pickle.load(F) while True:
if reply==1:
    newrefno=int(input('enter new refno'))
    for j in L:
        if j[0]==newrefno:
            print('refno already exists')
    else:
        i[0]=newrefno
if reply==2:
    newname=input('enter new name')
    i[1]=newname
if reply==3:
    newprice=int(input('enter new price'))
    i[2]=newprice
if reply==4:
    newrefno=int(input('enter new refno'))
    newname=input('enter new name')
    newprice=int(input('enter new price'))
    i[0]=newrefno
    i[1]=newname
    i[2]=newprice
    print('record changed')
    print('new record:',i)
if reply==5:
    break


n=int(input('which record would you like to delete? (enter item
            for i in L:
                if i[0]==n:
print(i) L.remove(i)
                    print('record deleted')
                    break
            else:
                print('item with reference number',n,'does not exist')
            more=input('would you like to continue?')
            if more in 'NOnoNo':
break F.seek(0)
pickle.dump(L,F)
def searching():
with open('ecar.dat','rb')as F:
txt=pickle.load(F) while True:
3:price'))
rep=int(input('how would you like to navigate? 1: refno, 2: name,
if rep==1:
    refno=int(input('enter refno'))
    for i in txt:
        if i[0]==refno:
            print(i)
break else:
        print('record does not exist')
if rep==2:
    count=0
    name=input('enter name of dish')
    for i in txt:
        if i[1]==name:
            print(i)
            count+=1
    if count==0:
        print('record does not exist')
if rep==3:
    count1=0
    price=int(input('enter price of dish'))
    for i in txt:
        if i[2]==price:
            print(i)
            count1+=1
    if count1==0:
        print('record does not exist')

             more=input('would you like to continue searching?')
            if more in 'noNONo':
break
#functions for customer of the restaurant
def lookmenu():
with open("ecar.dat",'rb') as F: data=pickle.load(F) print("Here is the menu:") for i in data:
print(i)
def whattoorder():
with open("ecar.dat",'rb') as F:
data=pickle.load(F) O=[]
global price price=[]
while True:
order=input("What would you like to order? (enter the RefNo.)") for i in range(0,len(data)):
if int(order)==int(data[i][0]): O.append(data[i]) price.append(data[i][2])
ask=input("Would you like to order something else?") if ask in "NOnoNon":
break
print("This is your order", O)
def generatebill():
    global price
print("Your total bill comes out to be Rs.", sum(price)) try:
with open('earnings.dat','rb+')as F: L=pickle.load(F) L[0]+=sum(price)
F.seek(0)
pickle.dump(L,F) except:
with open('earnings.dat','wb')as F: L=[0]
L[0]+=sum(price) pickle.dump(L,F)
def earnings():
with open('earnings.dat', 'rb')as F:
L=pickle.load(F)
print('total earnings =',sum(L))

 # Main Code
print("❤ Welcome to ECAR ❤") print('ADMIN LOGIN: 1, CUSTOMER: 2') reply=int(input('ADMIN LOGIN/ CUSTOMER?')) print()
if reply==1:
while True:
print('Admin Options:-')
print()
print('To add items in menu: 1\nTo display menu: 2\nTo edit menu: 3\nTo
delete items from menu: 4\nTo navigate through menu: 5\nTo Display total
earnings: 6\nTo LogOut: 7')
        p=int(input('Enter your choice'))
        if p==1:
            addrecord()
        elif p==2:
            displaymenu()
        elif p==3:
            editrecord()
        elif p==4:
            deleterecord()
        elif p==5:
            searching()
        elif p==6:
            earnings()
        elif p==7:
break else:
            print('invalid input, please try again')
elif reply==2:
while True:
print('customer options:-')
print()
print('To view the menu: 1\nTo place an order: 2\nTo generate the bill:
3\nIf you are done: 4')
        q=int(input('Enter your choice'))
        if q==1:
            lookmenu()
        elif q==2:
            whattoorder()
        elif q==3:
            generatebill()
        elif q==4:
break else:
            print('invalid input, please try again')
