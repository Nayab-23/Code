
##### STACKS

stack = [] * 10 
stack_full = 10 
base_pointer = 0 
top_pointer = - 1 

def pop() :
  global top_pointer , base_pointer , item 
  if top_pointer == base_pointer - 1  : 
    print( "Stack is empty") 
  
  else : 
    item = stack[top_pointer] 
    top_pointer -= 1 


def push() : 
  global top_pointer , item 
  if top_pointer < stack_full - 1 :
    top_pointer += 1 
    stack[top_pointer] = item 
  
  else :
    print("Stack is full")
    
  





 

    
    

    
  



