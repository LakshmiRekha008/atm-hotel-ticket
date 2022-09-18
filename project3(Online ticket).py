print("*** WELCOME TO VR EXPRESS ***")


# Ticket Booking System.
def tickets():
    
    print("Your Booking is Successfully...")
    print("Your Ticket is Downloading....")
    print("*********** VR EXPRESS **********")
    print("-------------- Passengers Details --------------")
    print(f"Passenger Name: {name}")
    print(f"Age: {age}")
    print(f"sex: {sex}")
    print("--------------------------------------------------")
    print("-------------- Reservation Details --------------")
    print("Train Name: VR Express")
    print("Train Number: 4628")
    print(f"Deparature/Journey Date: {Depar_date}")
    print(f"Journey from: {jour1}")
    print(f"Journey To: {jour2}")
    print("----------------!Enjoy Your Journey!-------------")

user_tickets = {}

available_seats = ['1a', '2a', '19b', '20d', '21e', ]


start = "\nWould you like to start booking your ticket? (yes/no) "
name="Enter your Name: "
age="Enter Your Age: "
sex="Female/Male: "
mobile_num="Enter Your Mobile Number: "
Depar_date="Enter Your Journey Date:"
jour1="Journy From: "
jour2="Journy To: "
wanted_seats = "\nHow many seats are you booking today?"
wanted_seats+= "\nEnter the number: "
go_again_prompt = "Would you like to let someone else book their tickets? (yes/no) "

# Ask the user if he would like to start booking their tickets.
start = input(start)
if start.lower() == 'yes':
    
    while True:
        # Ask for the users name.
        name = input(name)
        age=input(age)
        sex=input(sex)
        mobile_num= int(input(mobile_num))
        Depar_date=input(Depar_date)
        jour1= input(jour1)
        jour2= input(jour2)
        print(f"Welcome To {jour1} To {jour2} Express!")

        # Empty list to store the seat(s) the user has chosen.
        seats = []

        wanted_seats = input(wanted_seats)
        wanted_seats = int(wanted_seats)
        if wanted_seats > len(available_seats):
            print(f"\n--I'm sorry, we only have {len(available_seats)} "
                "seats available--")
            print("--Please try again--")
           
        while True:

            # Show the user the available seats.
            print("\nHere are the available seats:")
            for seat in available_seats:
                print(seat)

            seat = "\nPlease enter the number of the seat you would like to book: "
            seat = input(seat)

            if seat in available_seats:
                available_seats.remove(seat)
    
            else:
                print("\n--I'm sorry you have chosen an invalid seat--"
                    "\n-Please try again-")
                continue

            # Add the chosen seat to the 'seats' list
            seats.append(seat)

            if wanted_seats > 1:
                print("\nYou can now choose another seat.")
                wanted_seats-=1
                continue
            else:
                break

        user_tickets[name] = seats

        if available_seats:
            go_again = input(go_again_prompt)
            if go_again == 'no':
                break
        else:
            break

    tickets()
    
    print("\nWe will now redirect you to the payment portal."
        "\nThank You for choosing us.")

else:
    print("You can always come by later!")




    


