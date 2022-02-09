Testlist = [
               ["Romeo and Juliet","Shakespeare"],
               ["Othello","Play"],
               ["Macbeth","Tragedy"]
               ]
Value = "Tragedy"
for index, lst in enumerate(Testlist):
  if Value in lst:
    print( index, lst.index(Value) )