class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        my_map = {} #Created a hashmap or say dictionary

        for i in arr:
            my_map[i] = my_map.get(i,0)+1  #loop to check occurences 

        
        occurrences = list(my_map.values())#Convert values or count to list 

        if len(occurrences) == len(set(occurrences)):
            return True
        else:
            return False

'''
Approach 1:

Create a dictionary

Loop in the arr get values and count in hashmap

Convert values in a list

len(occurrences)= Gives the total number of values (including duplicates).

len(set(occurrences)) = Gives the number of unique values only.

if len(occurrences) == len(set(occurrences)) == True else: False


#Approach 2:

#Use Constraints and intialize a array of constant size
#get occurences by adding +1000 in each element
#store in array and then sort the array
#loop in the sorted array

for (int i= 1; i<2001;i++){  
    if (vec[i]== vec[i-1] && vec[i]!=0):
        return False
    }
return True

#we get answer

'''