def febrec(start):
    if(start<=1):
        return start;
    else:
        return (febrec(start-1)+febrec(start-2))
    
def febitr(start):
    n1=0
    n2=1
    sum=0
    for i in range(0,start):
        if(i<=1):
            sum=i
        else:
            sum=n1+n2
            n1=n2
            n2=sum
        print(sum, " ")

def main():
    ch=0
    while(ch!=3):
        print("Choice 1: Recursive function")
        print("Choice 2: Iterative Function")
        print("Choice 3: Exit")
        ch=int(input("Enter Choice: "))
        if(ch==1):
            n1=int(input("Enter number of terms for fabonnaci series: "))
            print("Fabonnaci series using recurrsion: ")
            for i in range(0,n1):
                print(febrec(i)," ")
        elif(ch==2):
            n2=int(input("Enter number of terms for fabonnaci series: "))
            print("Fabonnaci series using iteration: ")
            febitr(n2)
        elif(ch==3):
            print("Exiting!")
            exit(0)
        else:
            print("Wrong choice,Enter again!")
            
if __name__=="__main__":
    main()
