def validator(*args):
    gate=False
    if args[1]=="int":
        while not(ans:=input(args[0])).isnumeric():
            print("Please don't enter whitespace!"if" "in ans else"Please enter a number!")
        gate=True
    elif args[1]=="str":
        while not(ans:=input(args[0])).isalpha():
            print("Please don't enter whitespace!"if" "in ans else"Please enter a letter/word!")
        gate=True
    else:
        return ans if gate else validator(x for x in args)