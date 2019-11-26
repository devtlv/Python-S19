### Exercise (medium)
#
#Make a function that receives a list and print:
#-  The number of elements in the list
#-  The minimum element in the list
#-  The maximum element in the list
#-  The sum of all the numbers in the list
#
###

def list_describer(l):
    print("Number of elements in this list:", len(l))
    print("Minimum element of this list:", min(l))
    print("Maximum element of this list:", max(l))
    print("All the elements of this list sum to:",sum(l))

list_describer([1,3,312,51234,31234,151,5715,262,341,4572,3452435,])
