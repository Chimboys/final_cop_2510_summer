def second():
    print("B") #6
    #third() #What is going to be printed? Is there any problems with code?

def third():
    print("C") #4
    first()
  
def first():
    print("A") #5
    second()
    
print("D") #1

def main():
    print("E") #3
    third()

print("F") #2



if __name__ == "__main__":
    main()
    print("G") #7







