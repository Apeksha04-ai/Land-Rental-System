
def check_avaliability_of_land(kitta_num):   #function to check the availiability of land based on kitta number
 
 with open('sample.txt','r') as file :       # opened file from sample.txt in read mode
  
  txt = file.readlines()                     # read eachlines of the txt and store it in a variable named lines

 for line in txt:                              #Iterated through each line 
  
  arr = line.strip().split(',')        # split each line of text into a list using the comma as a separator

  if arr[0]==kitta_num:                  #check whether kitta  number matches the provided one or not
      
      if arr[-1]=="Available":           # If kitta number matches it checks if land is available or not

        ( print(f"The land with kitta number {kitta_num} is Available ."))  #prints "Available " along with kitta number 
      else:
       ( print(f"The land with kitta number {kitta_num} is Not  Available ."))   #prints "Not  Available " along with kitta number 

 return f"\n The land with the kitta number {kitta_num} is not found. "    # If kitta number doesnot match it returns kitta num not found 
 
def showAvailable():         
  with open('sample.txt', 'r') as lines:    
    for line in lines:     
      arr = line.strip().split(', ')
      if arr[-1] == "Available":
        print(f"\n{line}")


def showNotAvailable():    
  with open('sample.txt', 'r') as lines:    
    for line in lines:     
      arr = line.strip().split(', ')
      if arr[-1] == "Not Available":
        print(f"\n{line}")
   

    
   

   


 
 
  



 

