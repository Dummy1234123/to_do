from read import main as r
from write import main as w

while True:
    ans = input("Do you want to add or read tasks? ")
    if ans == "add":
        w()
    if ans == "read":
        r()
    if ans == "q":
        break


