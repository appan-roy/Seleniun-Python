import os

with open(os.getcwd()+"\\FileHandling\\Demo2.txt","a") as f:
    f.write("\nAppending text")
    f.write("\nBye")