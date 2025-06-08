import random
from datetime import datetime

def buy_land(land_id):
    customer_name = input("\nEnter your Name: ")
    while True:
        try:
            months_for_rent = int(input("\nEnter how long do you want to rent land (in months): "))
            break
        except ValueError:
            print("Please enter digits only for the number of months.")
    while True:
        try:      
            contact_num = int(input("\nEnter your contact number: "))
            if len(str(contact_num)) != 10:
                raise ValueError("Contact number must be a 10-digit integer.")
            break
        except ValueError as ve:
            if "invalid literal for int()" in str(ve): 
                print("Please enter digits only")
            else:
                print(ve)

    ran = random.randint(1,555)
    time = datetime.now()
    
    found = False  # Flag to check if the land ID is found
    
    with open('sample.txt', 'r') as lines:
        i = lines.readlines()
        
    with open('sample.txt', 'w') as lines:
        for line in i:
            arr = line.strip().split(', ')
            cost = months_for_rent * int(arr[4])
            if land_id == arr[0]:
                arr[-1] = 'Not Available'
                found = True  # Set the flag to True if land ID is found
            lines.write(', '.join(arr) + '\n')  # Write the modified line back to the file
            
    if not found:
        print("Land ID not found. Please enter a valid Kitta number.")
        return  # Exit the function if land ID is not found

    content = f"""
          +------------------------------------------------------------------+
          +     Techno Property Nepal : Rental Invoice of customer
          +   
          +   Customer Name : {customer_name}
          +    
          +   Contact No   :  {contact_num}      Date : {time}
          +--------------------------------------------------------------------+
          | Kitta No                |  {land_id} 
          | Location                |  {arr[1]}
          | Direction               |  {arr[2]} Faced 
          | Total Anna              |  {arr[3]}
          | Duration                |  {months_for_rent} Month
          | Price                   |   Rs.{cost} 
          +----------------------------------------------------------------------+
"""
    print(content)
    with open(f'Buy_{customer_name}{ran}.txt', 'w') as invoice:
        invoice.write(content)

    return
