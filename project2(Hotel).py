class hotelmanage:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1000,name='',mobile_number='',cindate='',coutdate='',rno=1):

        print ("\n\n***** WELCOME TO PMJL HOTEL *****\n")
        self.name=name
        self.mobile_number=mobile_number
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        
    def details(self):

        self.name=input("\nEnter your Fullname: ")
        self.mobile_number=input("\nEnter your mobile number: ")
        self.cindate=input("\nEnter your checkin date: ")
        self.coutdate=input("\nEnter your checkout date: ")
        print("Your room no.:",self.rno,"\n")
        
    def room(self):#sel1353

        print ("We have the following rooms for you :-")

        print("""
        **********************

        1.  Class A ----> 5000

        2.  Class B ----> 4000

        3.  Class C ----> 3000

        4.  Class D ----> 2000
       
        5.  Class E ---> 1000

        ***********************
        """)

        x=int(input("Enter the number of your choice: "))

        n=int(input("For How Many Days Did You Stay: "))

        if(x==1):

            print ("you have choose room Class A")

            self.s=5000*n

        elif (x==2):

            print ("you have select room Class B")

            self.s=4000*n

        elif (x==3):

            print ("you have select room Class C")

            self.s=3000*n

        elif (x==4):
            print ("you have select room Class D")

            self.s=2000*n

        elif (x==4):
             print ("you have select room Class E")

             self.s=1000*n


        else:

            print ("please choose a room")

        print ("your choosen room rent is =",self.s,"\n")

    def food(self):

        print("***** RESTAURANT MENU *****")

        print("1.Dessert ---> 100")
        print("2.Drinks ---> 50")
        print("3.Breakfast ---> 90")
        print("4.Lunch ---> 110")
        print("5.Dinner ---. 150")
        print("6.Exit")

        while (1):

            c=int(input("Enter the number of your choice:"))


            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+100*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+50*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+90*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+110*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+150*d

            elif (c==6):
                break 
            else:
                print("You've Enter an Invalid Key")

        print ("Total food Cost=Rs",self.r,"\n")

    def display(self):

        print ("******HOTEL BILL******")
        print ("----------------- Customer details ------------------")

        print ("Customer name:",self.name)
        print ("Customer mobile number:",self.mobile_number)
        print ("Check in date:",self.cindate)
        print ("Check out date",self.coutdate)
        print ("Room no.",self.rno)
        print ("Your Room Rent is:",self.s)
        print ("Your Food bill is:",self.r)
        
        print("------------------ Thank You ! Visit again ----------------")

        self.rt=self.s+self.t+self.p+self.r

        print ("Your Purchased is:",self.rt)
        print ("Our Service Charges is",self.a)
        print ("Your Total Purchased is:",self.rt+self.a,"\n")
        
        self.rno+=1

def main():
    a=hotelmanage()

    while (1):
        print("1.Customer Data")
        
        print("2.Room Rent")

        print("3.Food Purchase")

        print("4.Total cost")

        print("5.EXIT")

        b=int(input("\nEnter the number of your choice:"))

        if (b==1):
            a.details()

        elif (b==2):

            a.room()               

        elif (b==3):

            a.food()

        elif (b==4):

            a.display()

        elif (b==5):

            quit()

main()