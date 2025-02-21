
# 1. Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are
# sol:
# print('\n')
# print('Twinkle, twinkle, little star,\n  How I wonder what you are!\n\tUp above the world so high,\n\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n  How I wonder what you are!')

# 2.Write a Python program to find out what version of Python you are using.
# sol:
# import sys
# print("python version")
# print(sys.version)
# print("version_info")
# print(sys.version_info)

# 3.Write a Python program to display the current date and time.
# sol:
# import datetime

# now = datetime.datetime.now()
# print("current data and time")
# print(now.strftime("%Y-%m-%d %H-%M-%S"))

# 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# sol:
# from math import pi
# radius = float(input("Enter Radius: "))
# print((pi*radius*radius))
# print((3.14*radius*radius))

# 5 Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# sol:
# fname = input("Enter first Name: ")
# lname = input("Enter Last Name: ")
# print(lname+" "+fname)

# 6.Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')
# sol:

# nums = input("Enter numbers separated by comma: ")
# l1 = nums.split(",")
# print("List: ",l1)
# t1 = tuple(l1)
# print("Tuple: ",t1)


# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java
# sol:
# list1 = input("Enter Filename: ")
# filename = list1.split(".")
# print(filename[-1])


# Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[-1])


#  Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# # Sample Output : The examination will start from : 11 / 12 / 2014

# print("The examination will start from : %i / %i / %i" % exam_st_date)


# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

n = int(input("Enter the value of n:"))
n1=int("%s "% n)
n2=int("%s%s "% (n,n))
n3=int("%s%s%s "% (n,n,n))   
print(n1+n2+n3)


 
data= { 
    "batters": { 
        "batter": [ 
            { 
                "batter": [ 
                    { 
                        "batter": [{ 
                                "type": "Regular" 
                        }] 
                    }] 
            }] 
    } 
} 

value = data.get("batters",{}).get("batts",[{}])[0].get("batters",[{}][0]).get("batters",[{}][0]).get("type","Regular")
print(value)
