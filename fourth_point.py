def maxsum(x:list)-> int:
    '''This function receives a list of numbers and returns 
    the maximum sum of two consecutive numbers'''

    maxX = max(x) # Find the maximum value in the list x
    if x.index(maxX) != len(x)-1:
        x1 = x[x.index(maxX)+1] # Find the value that is before the maximum value, and save it in a variable
    else: 
        x1 = 0 # If the maximum value is at the end, the value of the variable will be 0

    if x.index(maxX) != 0: # Find the value that is afer the maximum value, and save it in a variable
        x2 = x[x.index(maxX)-1]
    else : 
        x2 = 0 # If the maximum value is at the beginning, the value of the variable will be 0

    if (x1 == 0 or x2 == 0): # Here, we compare which value is greater and operate it with the maximum value
        if x1 == 0:  # If the value is negative we can´t comparate it to 0
            return x2 + maxX
        else: 
            return x1 + maxX  
    else:
        if (x1 > x2):
            return x1 + maxX
        else:
            return x2 + maxX

if __name__ == "__main__": # Function main, the starting point of the code
    x = [int(x) for x in input("Enter a list of numbers for which you want to know the maximum consecutive sum,\nwith a space between each number: \n").split()]
    print("The result of the maximum consecutive sum is:", maxsum(x=x))
