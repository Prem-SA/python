name=input("enter your name:")
mobile=input("enter yoour mobile number:")
print("1.avadi to ponamalle")
print("2.avadi to porur")
src=int(input("enter the source  to dest route:"))
print("1.mini")
print("2.sedan")
print("3.suv")
vech=int(input("choose the vechile :"))
if(src==1 and vech==1):
    print("*******************************BILL***********************************")
    print("\tNAME:",name)
    print("\tMOBILE:",mobile)
    cost=(10*5)+80
    print("\tTHE TOTAL KM TRAVELLED =10")
    print ("\tTHE TOTAL COST:",cost)
elif(src==1 and vech==2):
   print("*******************************BILL***********************************")
   print("\tNAME:",name)
   print("\tMOBILE:",mobile)
   cost=(10*5)+100
   print("\tTHE TOTAL KM TRAVELLED =10")
   print ("\tTHE TOTAL COST:",cost)
elif(src==1 and vech==3):
    print("*******************************BILL***********************************")
    print("\tNAME:",name)
    print("\tMOBILE:",mobile)
    cost=(10*5)+150
    print("\tTHE TOTAL KM TRAVELLED =10")
    print ("\tTHE TOTAL COST:",cost)
elif(src==2 and vech==1):
    print("*******************************BILL***********************************")
    print("\tNAME:",name)
    print("\tMOBILE:",mobile)
    cost=(20*5)+80
    print("\tTHE TOTAL KM TRAVELLED =20")
    print ("\tTHE TOTAL COST:",cost)
elif(src==2 and vech==2):
   print("*******************************BILL***********************************")
   print("\tNAME:",name)
   print("\tMOBILE:",mobile)
   cost=(20*5)+100
   print ("\tTHE TOTAL COST:",cost)
elif(src==2 and vech==3):
    print("*******************************BILL***********************************")
    print("\tNAME:",name)
    print("\tMOBILE:",mobile)
    cost=(20*5)+150
    print("\tTHE TOTAL KM TRAVELLED =20")
    print ("\tTHE TOTAL COST:",cost)
else:
    print("enter the valid choice")



