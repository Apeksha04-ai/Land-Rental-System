import datetime
import random

def calculate_fine(months_delayed):
    # Fine amount per month of delay
    fine_per_month = 1000  # Assuming Rs. 1000 fine per month of delay
    # Calculate fine for each month of delayty
    fine = months_delayed * fine_per_month
    return fine             

def rent_land(kitta_num):
    a = input("\nEnter your name: ")
    while True:
        try:
            initial_rental_months = int(input("\nHow many months was the initial rental agreement? "))
            break
        except ValueError:
            print("Please enter digits only for the number of months.")
    while True:
        try:
            months_delayed = int(input("\nHow many months have been exceeded? "))
            if months_delayed < 0:
                raise ValueError("Months cannot be negative.") 
            break
        except ValueError:
            print("Please Enter digits only")
    ran = random.randint(1,444)

    with open('sample.txt', 'r') as file:
        lines = file.readlines()

    invoice_content = ""
    found = False
    with open('sample.txt', 'w') as file:
        for line in lines:
            arr = line.strip().split(', ')
            if kitta_num == arr[0]:
                found = True
                if arr[-1] == 'Not Available':
                    arr[-1] = 'Available'
                    # Calculate fine based on exceeded period
                    fine = calculate_fine(months_delayed)
                    # Calculate total payable amount including fine
                    total_amount = initial_rental_months * int(arr[4]) + fine

                    # Get current date and time
                    return_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # Construct invoice content
                    invoice_content = f"""
                +-------------------------------------------------------------------------------+
                    Techno Property Nepal : Return Invoice of Customer

                    customer Name : {a}                 Return Date and Time: {return_date}
                +--------------------------------------------------------------------------------+
                | Kitta No                        |    {arr[0]}
                | Location                        |    {arr[1]}
                | Direction                       |    {arr[2]}
                | Area of Land (anna)             |    {arr[3]}
                | Duration of Rent                |    {initial_rental_months} months
                | Price of the Land (per month)   |    Rs.{arr[4]}
                | Exceeded Period                 |    {months_delayed} months
                | Fine                            |     Rs.{fine}
                ----------------------------------------------------------------------------------+
                | Total Amount                    |     Rs.{total_amount}                          
                +----------------------------------------------------------------------------------+"""

                    # Write invoice content to file
                    with open(f'return_{a}{ran}.txt', 'w') as invoice:
                        invoice.write(invoice_content)
            file.write(', '.join(arr) + '\n')

    if not found:
        print(f"\nLand with the kitta number {kitta_num} not found")

    # Print invoice content
    print(invoice_content)

