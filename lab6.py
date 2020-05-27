"""
lab 6 5/27
"""
#3.1

#for num in range(6):
 #   if num != 3:
  #      print(num)
        
#3.2

#result_32 = 1

#for num in range(1,6):
 #   result_32= result_32 * num 
#print(result_32) 
    
#3.3

#result_33 =  0

# num in range(1,6):
 #  result_33=result_33 + num 
#print(result_33)

#3.4 

#result_34 = 1

#for num in range(3,9):
 #   result_34=result_34 * num
#print(result_34)

#3.5

#result_351=1

#for num in range(1,9):
 #   result_351=result_351 * num
    
#result_352=1  

#for num in range(1,4):
 #   result_352=result_352* num
#print(result_351/result_352) 

#3.6

result= 0

for word in 'this is my 6th string'.split():
    result=result+1
print(result)

#3.7

my_tweet = {
            'favorite_count': '1138',
            'lan':'eng',
            'coordinates':(-75,40),
            'entities':
                {
                    "hashtags":[ "Preds ", "Pens", " SingIntoSpring "]
                    
                }
            }
result=0
for hastag in my_tweet['entities']['hashtags']:
    result=result+1
print(result)

            
            

