
    



#os.path join
import os
files = os.listdir()
now = os.getcwd()

for file in files:
  print(os.path.join(now,file)):