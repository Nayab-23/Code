score = []

def highscore() : 
  global score
  with open("scores.txt","r") as file:
    for i in file :
      parts = i.split().strip()
      if len(parts) == 2 :
        name = parts[0]
        score = parts[1]
        
        
        
    

