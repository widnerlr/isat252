"""
lab8 functions
"""
#3.1

#demo_str='hello world!'
#def cal_words(input_str):
#    return len(input_str.split())

#3.2

#print(cal_words(demo_str))

#3.3

num_list = [1,2,3,4,5,6]

def find_min(input_list):
    
    min_num = num_list[0]

    for num in num_list:
        if type (num) is not str:
            if min_num >= num:
                 min_num= min_num 
    return(min_num)
    
#3.4 

print(find_min((num_list)))

#3.5 
mix_list = [1,2,3,4,'a',6]
print(find_min(mix_list))