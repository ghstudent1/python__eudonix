
def calculator(nbr1,nbr2,opr):
    if opr=="+":
        return nbr1+nbr2
    elif opr=="-":
        return nbr1-nbr2
    elif opr=="*":
        return nbr1*nbr2
    elif opr=="/":
        return nbr1/nbr2
    else:
        return "invalid operation"



if __name__ == '__main__':
    while True:
        try:
            nbr1=float(input("plz enter first nbr"))
        except ValueError:
            print("the nember should be float ")
            continue
        opr = str(input("plz enter operator"))
        if opr not in["+","-","/","*"]:
                print("the opr should be in [+,-,*,/] ")
                continue
        try:
            nbr2 = float(input("plz enter second nbr"))
        except ValueError:
            print("the nember should be float ")
            continue
        print("Result = "+str(calculator(nbr1,nbr2,opr)))
        choice=input("enter q to quit or press any key to restart")
        if choice =="q":
            break
