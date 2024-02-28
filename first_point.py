def calculator(first_numb, second_numb, oper) ->int:
    '''This function receives a word and returns True or false
    depending on whether the word is a palindrome or not'''
    
    y, z = int(first_numb), int(second_numb) # Transform both values: str into values: int, and assigning a variable for each one
    match oper: # Use "match" to no use "elif" (The last one could make the same thing)
        case "+": # It evaluates the value of oper and, dependent on it, makes a determinate operation
            return y + z
        case "-":
            return y - z
        case "*":
            return y * z
        case _:
            return y / z

if __name__ == "__main__": # Function main, the starting point of the code

    fst = input("Enter the first number: ") # Receive the values for the operation
    scd = input("Enter the second number: ")
    oper = input("Enter the sing of operation that you wanna do: ") # You can't dive by 0, so we add a conditional
    while (oper == "/" and scd == "0" ):
        print("You can't divide by 0")
        scd = input("Enter another number: ")
      
    print("The result of this operation is: ", calculator(fst, scd, oper))