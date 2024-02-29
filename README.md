# First_challenge_OOP

### This is the first of many that will come in the future

## First point

This point said to me that I have to do a function that does basic 
operations (`+, -, *, /`), so I made a function that receives two numbers (`first_numb, second_numb`)
and an operation sign (`oper`), this will tell the function which kind of operation
it has to do with the two numbers.

```python
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
```

## Second point

This point said to me that I have to do a function that receives a string (`x`) and returns True if it's a palindrome, or else return False
knowing that a palindrome is a world that has the same reading backwards as forwards, I made a function that compares the first and last characters; 
making a comparison between the characters in the positions `x[i]` and `x[-i-1]`, with `i` having values between `0` and `len(x)/2` (this is the middle of the word
if the characters are the same until this, the word is a palindrome).

```python
def equal(x: str)-> bool :
    '''This function receives a word and returns True or false
    depending on whether the word is a palindrome or not'''

    for i in range(len(x)//2): # Compare the first and the last character, the second and the penultimate  
        if x[i] != x[-i-1]: # and continue comparing like this until reaching the characters that are in the middle of the word
            return False # When it does the comparison, if there are two different characters, it returns false
    return True # If all is equal, it returns True
    
if __name__ == "__main__": # Function main, the starting point of the code
    x: str = input("Enter the word that you think that is a palindrome:")
    print("The word",x, "is", str(equal(x))+"ly a palindrome")
```

## Third point

This point said to me that I have to do a function that receives a list of numbers (`x`) and returns a list with the primes numbers ordered (`list_primes`) in the first list. 
For solving it, I decided to use the sieve of Eratosthenes, because it's one of the many ways that you can find a prime number (I used this because I saw it in the
before semester, and I saw a video that talks about it, and I think it was an awesome form for finding a prime (The video: https://youtu.be/9vhJ8jplsgw, credits to: Daniel Carreon and Eratosthenes)). 

```python
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

```

## Fourth point

This point said to me that I have to do a function that receives a list of numbers (`x`) and gives the maximum summation of two consecutive numbers (`maxX + (a variable)`), 
I know that in the summary will be the maximum number  of the list, so I decided to find this maximum number after that, find the numbers before `x1` and after `x2` it, and compare it for
knowing which is greater, plus it with the maximum number, there will be a problem if the maximum number (`maxX`) is in the position `x[0]` (because it doesn't have a number before it)
or `x[len(x)-1]` (because it doesn't have a number after it), so I assigned to these values the number `0`, with this I solved a problem, but a new one 
appear, 0 is greater than any negative number, so I added a conditional that if some value `x1 or x2` == 0  don't make the comparative, and plus the number different from 0.

```python
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

```

## Fifth point

This point said to me that I have to do a function that receives a list of words (`x`) and returns it in the same ordered with the words that are anagrams (`list2`),
an anagram is a word that, depending on the ways you order the characters, makes a different world; knowing this, I made a code that makes 
a set of the worlds in the list (`sets_first, sets_second`), then count how many times each one (`set(word)`) appears (`list1`), and if it is greater than one, it will be an anagram; you 
would think, why using the count of each set and greater than one gives me the answer? It's for two reasons:                         
1. The sets don't count how many times a character appears, only if it appears or not.                                    
2. If there are two words with the same set of characters, it indicates that these words are anagrams, because with the characters of one, you could do the other.

```python
def anagram(x: list)-> list:
    '''This function receives a list of words and returns another 
    list of words that have anagrams of the first list'''

    sets_first = [set(i) for i in x]  # Make a set of each element in x (our original list)

    sets_second = [] 

    for z in x: # Makes another set of each element in x without repeat elements
        if set(z) not in sets_second: 
            sets_second.append(set(z))
    
    list1 = []

    a = 0 

    for i in sets_second: # A couner who will tell me how many times an anagram appears
        if i in sets_second[a:] and len(list1) > sets_second.index(i): # This part helps me to know if a count of an anagram has appeared before
            list1.append(list1[sets_second.index(i)]) # For don't make the same count many times
        else:
            if i in sets_first:
                list1.append(sets_first.count(i))
        a += 1

    list2 = []

    for j in list1: # Uses the preceding part 
        if j > 1: # if the count of an anagram is greater than 1 
            y = sets_first[list1.index(j)]
            for m in x:
                if set(m) == y:
                    list2.append(m) #it saves the word associated with the anagram

    return list2

if __name__ == "__main__": # Function main, the starting point of the code 
    x: list = [str(x) for x in input("Enter a list of words that you want to know if they are anagrams or not, \neach word separated by spaces and without capital letters: \n").split()] 
    print("The words that are anagrams of the previous list are:", anagram(x=x)) 

```
