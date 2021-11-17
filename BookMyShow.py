class Book_My_Show:
        def __init__(self):
            print("\n")
            print("***Welcome To Book My Show***")
            #r= Number Of Rows in Theator
            #c= Number Of Columns in Theator
            self.r=int(input("Enter The Number Of Rows in Theator:- \n"))
            self.c=int(input("Enter The Number Of Columns in Theator:- \n"))

            #To Display Arrangement
            self.s=[0]*self.r
            self.t=[' ']+[str(i+1) for i in range (self.c)]
            for i in range(self.r):
                self.s[i]=[str(i+1)]+['S']*self.c           

            #calculating income
            self.result=self.r*self.c
            if self.result<=60:
                self.income=self.result*10
            if self.result>60:
                if (self.r)%2==0:
                    self.income=self.result*9
                else:
                    var=(self.r)//2
                    self.income=(8*var*(self.c))+(10*(self.r)-var)*(self.c)
            self.current_income=0
            self.user_info={}
            self.options()

        #Option Choice
        def options(self):
            print("\n")
            print("*********\n")
            print("Select Following Options\n")
            print("1. Show The Seats")
            print("2. Buy Your Ticket")
            print("3. Statistics")
            print("4. Show User Information")
            print("0. Exit\n")
            print("*********")
            
            x=input()
            if x=="1":
                self.show_tickets()
            elif x=="2":
                self.buy_tickets()
            elif x=="3":
                self.show_statistics()
            elif x=="4":
                self.show_userInfo()
            elif x=="0":
                self.exit()
            else:
                print("Please Choose Appropriate Option")
        
        #Function to Show Tickets
        def show_tickets(self):
            print("\n")
            print("Theator")
            print(' '.join(self.t))
            for i in self.s:
                print(' '.join(i))
            print("\n")
            print("\t S = Vacant \t\t B = Booked")
            self.options()

        #Function to Buy Tickets
        def buy_tickets(self):
            x1=int(input("Enter Row Number:- "))
            x2=int(input("Enter Column Number:- "))

            if self.result<=60:
                price=10
            if self.result>60:
                if x1>(self.r)/2:
                    price=8
                if x1<(self.r)/2:
                    price=10
            print("Price Of Ticket :- "+str(price))
            print("Would You like to Buy :-")
            print("Press 'y' For Yes \n Press 'n' For No")

            yes_or_no=input("Enter Your Choice 'Y' or 'N' \n")
            if yes_or_no=="Y" or yes_or_no=="y":
                self.current_income=self.current_income+price

            #Gathering User Details
                self.user_info[x1+x2]={}
    
                self.user_info[x1+x2]["Name"]=input("Name:- ")

                self.user_info[x1+x2]["Gender"]=input("Gender:- ")
                if self.user_info[x1+x2]["Gender"]=="M" or self.user_info[x1+x2]["Gender"]=="m" or self.user_info[x1+x2]["Gender"]=="F" or self.user_info[x1+x2]["Gender"]=="f":
                    pass
                else:
                    print("Please Choose Appropriate Gender...")
                    self.user_info[x1+x2]["Gender"]=input("Gender:- ")

                self.user_info[x1+x2]["Age"]=input("Age:- ")
                if self.user_info[x1+x2]["Age"].isnumeric() and int(self.user_info[x1+x2]["Age"])>0 and int(self.user_info[x1+x2]["Age"])<=70:
                    pass
                else:
                    print("Please Enter Correct Age...")
                    self.user_info[x1+x2]["Age"]=input("Age:- ")

                self.user_info[x1+x2]["Ticket_Price"]=price

                self.user_info[x1+x2]["Phone_Number"]=input("Phone Number:- ")
                if self.user_info[x1+x2]["Phone_Number"].isnumeric() and len(self.user_info[x1+x2]["Phone_Number"])==10:
                    pass
                else:
                    print("Please Enter Correct Phone Number... ")
                    self.user_info[x1+x2]["Phone_Number"]=input("Phone Number:- ")

                print("\n")
                print("*** Booked Successfully***")
                self.s[int(x1)-1][int(x2)]="B"
            if yes_or_no=="n" or yes_or_no=="N":
                print("Thank You!!")

            self.options()

        #Function to Show booked and Vacant seats
        def show_statistics(self):
            print("\n")
            print("Number Of Tickets Purchesed:- "+str(len(self.user_info)))
            print("current_income:- $"+str(self.current_income))
            print("Total income:- $"+str(self.income))
            print("Percentage:- "+str((self.current_income*100)/self.income)+" %")

            print("*********")

            self.options()

        #Function to Show User Details
        def show_userInfo(self):
            if len(self.user_info)==0:
                print("Theator is completly Vacant...")
                self.options()

            print("To Get User Information")
            l=int(input("Enter Row Number "))
            m=int(input("Enter Column Number "))
            k=l+m

            if k in self.user_info:
                print("Name:- ",self.user_info[k]["Name"])
                print("Gender:- ",self.user_info[k]["Gender"])
                print("Age:- ",self.user_info[k]["Age"])
                print("Ticket Price:- ",self.user_info[k]["Ticket_Price"])
                print("Phone Number:- ",self.user_info[k]["Phone_Number"])
                print("*********")
            else:
                print("Row "+str(l)+" and Column "+str(m)+" Is not Booked Yet!!!")
            self.options()

        def exit(self):
            pass

BMS=Book_My_Show()
