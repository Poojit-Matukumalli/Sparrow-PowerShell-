from re import fullmatch

def cmd_echo(x):  # This is echo
        return x

def cmd_calc(x):
    def mathexpr(s):
        return bool(fullmatch(r"[0-9+\-*/().\s]+",s))
    if mathexpr(x) == True:
        output = eval(x)
        return output
    else:
        return "Enter a valid expression"
