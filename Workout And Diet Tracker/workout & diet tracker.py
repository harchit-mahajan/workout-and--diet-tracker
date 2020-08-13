import datetime

def gettime():
    return datetime.datetime.now()


def take():
    
    c=int(input("Enter 1 for Workout and 2 for Diet : "))
    
    if(c==1):
        value=input("Enter workout\n")
        with open("my_workout.txt","a") as op:
            op.write(str([str(gettime())])+": "+value+"\n")
        print("successfully written")
    
    elif(c==2):
        value = input("Enter food item\n")
        with open("my_diet.txt", "a") as op:
            op.write(str([str(gettime())]) + ": " + value + "\n")
        print("successfully written")
    
    else:
        print("plz enter valid input ")
    
    
def retrieve():
    
    c=int(input("enter 1 for Workout and 2 for Diet : "))
    
    if(c==1):
        with open("my_workout.txt") as op:
            for i in op:
                print(i,end="")
    
    elif(c==2):
        with open("my_diet.txt") as op:
            for i in op:
                print(i, end="")
    
    else:
        print("plz enter valid input (harry,rohan,hammad)")


if __name__ == "__main__":
    print("HEALTH MANAGEMENT SYSTEM")
    print("1. ENTER DATA")
    print("2. RETRIEVE DATA")
    a=int(input("Enter 1 or 2 : "))

    if a==1:
        take()
    else:
        retrieve()