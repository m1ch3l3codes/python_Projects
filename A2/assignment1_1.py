#INPUT two values
#RETURN A and B
def myAnd(A,B):
     print (A,B, "A and B =" , A and B)
     return A and B


#INPUT two values
#RETURN A or B 
def myOr(A,B):
     print ("A or B is" , A or B) 
     return A or B 


#INPUT one value
#RETURN not A
def myNot(A):
     print (not A)
     return not A 


#INPUT two values
#RETURN not (A and B) (called nand)
#REQUREMENTS use only previous functions
def myNand(A,B):
     print (not A) or (not B)
     return A or B 

#INPUT two value 
#RETURN not (A or B) (called nor)
#REQUIREMENTS use only previous functions
def myNor(A,B):
     print (not A) and (not B)
     return not A and not B

#INPUT two values A,B
#Return material implication A => B 
#REQUIREMENTS use only previous functions
def myImplication(A,B):
     return not (A) or B

#INPUT two values A,B
#RETURN A or B 
#REQUIREMENTS only use myNand gate
def DeMorganNand(A,B):
     print (A and B) 
     return not (A and B) 