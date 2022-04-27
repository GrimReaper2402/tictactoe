probability ={
    "B_T":0.002,
    "B_F":0.998,
    "E_T":0.001,
    "E_F":0.999,
    "ABE_T":0.94,
    "ABE_F":0.06,
    "AB_T":0.95,
    "AB_F":0.05,
    "AE_T":0.31,
    "AE_F":0.69,
    "A_T":0.001,
    "A_F":0.999,
    "DA_T":0.91,
    "DA_F":0.09,
    "D_T":0.05,
    "D_F":0.95,
    "SA_T":0.75,
    "SA_F":0.25,
    "S_T":0.02,
    "S_F":0.98
    }

def E_prob(E):
    if(E==1):
        return probability["E_T"]
    else :
        return probability["E_F"]

def B_prob(B):
    if(B==1):
        return probability["B_T"]
    else :
        return probability["B_F"]

def D_prob(D,A):
    if(A==1 and D==1):
        return probability["DA_T"]
    elif(A==1 and D==0):
        return probability["DA_F"]
    elif(A==0 and D==1):
        return probability["D_T"]
    else:
        return probability["D_F"]


def S_prob(S,A):
    if(A==1 and S==1):
        return probability["SA_T"]
    elif(A==1 and S==0):
        return probability["SA_F"]
    elif(A==0 and S==1):
        return probability["S_T"]
    else:
        return probability["S_F"]

def A_prob(E,B,A):
    if(E==1 and B==1 and A==1):
        return probability["ABE_T"]
    elif(E==1 and B==1 and A==0):
        return probability["ABE_F"]
    elif(E==1 and B==0 and A==1):
        return probability["AE_T"]
    elif(E==1 and B==0 and A==0):
        return probability["AE_F"]
    elif(E==0 and B==1 and A==1):
        return probability["AB_T"]
    elif(E==0 and B==1 and A==0):
        return probability["AB_F"]
    elif(E==0 and B==0 and A==1):
        return probability["A_T"]
    else:
        return probability["A_F"]

def prob():
    iE=int(input("Enter if Earthquake happened(yes=1,no=0) "))
    iB=int(input("Enter if Buglary happened(yes=1,no=0) "))
    iA=int(input("Enter if alarm has raised(yes=1,no=0) "))
    iD=int(input("Enter if David called(yes=1,no=0) "))
    iS=int(input("Enter if Sophia called(yes=1,no=0) "))
    PE=E_prob(iE)
    PB=B_prob(iB)
    PA=A_prob(iE,iB,iA)
    PD=D_prob(iD,iA)
    PS=S_prob(iS,iA)
    #print(PE,PB,PA,PD,PS)
    P=(PE*PA*PB*PD*PS) 
    print("Probability is {:.10f}".format(P))

prob()
