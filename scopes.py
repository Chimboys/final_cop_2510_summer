x = 10

def func2():
    print("Finally, x is ", x)

def func():
    global x
    x = 30
    print("No, I actually meant " , x)
    x = x+5
    func2()
    

def main(x):
    print("x value is ", x)
    x = 50
    print("I meant x value is ", x)
    func()
    


if __name__ == "__main__":
    main(20)
    

