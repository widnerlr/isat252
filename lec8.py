"""
lec 8 , functions
"""
#def my_function(a,b=0):
     
    
   # print('a is ',a)
  #  print('b is ',b)
 #   return a + b 
    
    
#print(my_function(a=1))

#ex1 

#def calculate_abs(a):
    
 #   if type (a) is str:
 #       return ('wrong data type')
 #   if a > 0:
 #       return a
 #   if a < 0: 
  #      return -a
        
#print(calculate_abs('a'))


#ex2

#def function_1(m,n):
#   
 #   result=0
 #   for i in range (n,m+1):
 #       result=result+i
 #   return result
    
#print(function_1(m=5,n=3)) 

#ex3

#def function_2(m,n):
    
 #   result=1
 #   for i in range (n,m+1):
  #      result=result*i
   #     print(i)
    #    print(result)
    
    #return result
    
#print(function_2(m=5,n=3))

#ex4
 
def cal_f(m):
    if m == 0:
        return(1)
    else:
        return m * cal_f(m-1)
print(cal_f(3))
    
    
def cal_p(m,n):
    return(cal_f(m)/cal_f(m-n))
print (cal_p(5,3))