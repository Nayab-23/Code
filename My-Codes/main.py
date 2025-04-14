

StackData = [""] * 10 
StackPointer = -1  
base_pointer = 0 
Stack_Full  = 10 
Item = 0 
global StackPointer , StackData

def PrintArray() : 

  for i in range(0 , len(StackData)) :
     print(StackData[i]) 

  print(StackPointer)


def push() : 
  global Stack_Full , StackData , StackPointer
  if StackPointer > Stack_Full -1  : 
    return False
  else : 
    StackPointer += 1 
    StackData[StackPointer] =  Item  
    return True

for i in range(0 , 11) : 
  num = int(input("Enter your number :" ))
  if push(num) == True : 
    print("Sucessfully added")
  else : 
    print("Stack is full")

PrintArray

push(11)
push(12)
push(13)





