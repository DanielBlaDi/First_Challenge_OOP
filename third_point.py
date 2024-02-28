def prime(x: list)-> list:
    '''This function receives a list of numbers and returns 
    a list with the primes numbers of the original list'''

    maxX = max(x)+1 #Maximum value

    list2 = [True] * (maxX) # Uses the sieve of Eratosthenes; this makes a list of len(Maximum value+1) of Trues because the maximum value could be a prime
    list2[0], list2[1] = False, False # the numbers 0 and 1 aren't primes

    primes = [] # Here we are gonna save our primes numbers

    for i in range(2, maxX): #start in the number 2
        if list2[i] == True: # the numbers that have the value true are primes numbers
            primes.append(i) # Save the value
            for j in range(i*2, maxX, i): # This part makes all the multiples of value True (i) will be False
                list2[j] = False          # Starts with i*2 because its the first multiple of i
                                          # Makes steps of i because the multiples of i => i+i+i = 3i

    filtre = set(x) & set(primes) # Comparate the original list with the prime list
    list_primes = (list(filtre)) # Gives me the values of the first list that are primes numbes
    list_primes.sort()  #And sort this number
    
    return list_primes


if __name__ == "__main__": # Function main, the starting point of the code
    x = [int(x) for x in input("Enter a list of numbers for which you want to know the primes numbers that it contains,\nwith a space between each number: \n").split()]
    primes = prime(x=x)
    if primes == []:
        print("There aren't primes numbers on this list")
    else:
        print("The primes in the list are:", primes)
