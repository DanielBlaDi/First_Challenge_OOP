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
