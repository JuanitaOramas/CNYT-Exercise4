from MATRIX-VECTOR-LIBRARY import *


#PROGRAMMING CHALLENGES
def probability (pos,v):
    a=normVector(v[pos])
    b=normVector(v)
    probability=(a/b)
    return probability*100
  

def stateVectorClick(a,b,c):
    b=[b]
    i=0
    while i<c:
        b=prodMv(a,b)
        i+=1
    return b[0]

def VectorProduct(v,v1):
    answer = 0 
    for i in range(len(v)):
        answer+=v[i]*v1[i]
    return answer
  
  
# Exercise # 4.4.1
def UnitaryVerify(u1,u):
    
    if unitMatrix(m)(U1) and unitMatrix(m)(u):
        answer =  matrixProduct(u1,u)
        return unitMatrix(answer)

# Exercise # 4.4.2 
def Experiment(v,n,clicks):
    for i in range(clicks):
        v = multiScalarMatrixCplx(v,n)
    return v
