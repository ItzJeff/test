def validator(*args):
    gate=False
    if args[1]=="int":
        while not(ans:=input(args[0])).isnumeric():
            print("Please enter a number!")
        gate=True
    elif args[0]=="str":
        while not(ans:=input(args[0])).isalpha():
            print("Please enter a letter/word!")
        gate=True
    else:pass