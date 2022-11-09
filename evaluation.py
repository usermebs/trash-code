

def isSimpleArg(a):
    """ fonction booléenne qui retourne vrai si a'' est un élément simple ou pas , dans 
    le contexte de mon code cela revient à vérifier si 'a' est un float ou un int """
    return isinstance(a,(float,int))

def isOp(op):
    return op in ["+","-","*","/"]

def isSimpleExpression(exp):
    return len(exp)==3 and isSimpleArg(exp[0]) and isOp(exp[1]) and isSimpleArg(exp[2]) 

def eval(exp):
    if isSimpleExpression(exp):
        op= exp[1]
        if op=="+":
            return exp[0]+exp[2]
        if op=="-":
            return exp[0]-exp[2]
        if op=="*":
            return exp[0]*exp[2]
        if op=="/":
            return exp[0]/exp[2]
    
    elif :
