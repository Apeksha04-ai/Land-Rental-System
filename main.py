from write import *
from read import *
from operation import *

def main():
    while True:
        print("""
+-------------------------------+
|Press 1 to Rent
|Press 2 to Return
|Press 3 to Exit
+---------------------------------+""")
        try:
            choice = input("Please Enter Your Choice (1, 2, 3): ")
            if choice == '1':
                showAvailable()
                land_id = input("What is the kitta number of the land you want to rent ? : ")
                try:
                    if not land_id.isdigit():
                        raise ValueError("Kitta number must be a positive integer.")

                    if int(land_id) < 0:
                        raise ValueError("Kitta number cannot be negative.")
                except ValueError as ve:
                    print("Value Error:", ve)
                    continue

                buy_land(land_id)
                
            elif choice == '2':
                showNotAvailable()
                land_id = input("What is the kitta number of the land you want to return ? : ")
                try:
                    if not land_id.isdigit():
                        raise ValueError("Kitta number must be a positive integer.")

                    if int(land_id) < 0:
                        raise ValueError("Kitta number cannot be negative.")
                except ValueError as ve:
                    print("Value Error:", ve)
                    continue

                rent_land(land_id)
               
            elif choice == '3':
                print("Exiting the program...")
                break  # Exit the while loop and end the program
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except Exception as e:
            print("An error occurred:", e)

main()  
