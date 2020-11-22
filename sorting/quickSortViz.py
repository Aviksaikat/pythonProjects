def quickSort(array, l, h): 
    if l<h: 
        p = partition(array,l,h)
        quickSort(array,l,p-1)
        quickSort(array,p+1,h)
    print(array)
def partition(array,l,h): 
    i = l - 1 
    pivot = array[h] 
    temp =[] 
    for j in range(l,h):
        if(array[j]<=pivot):
            i+=1
            array[i],array[j] = array[j],array[i]
    
    array[i+1],array[h] = array[h],array[i+1]
    return i+1
    
quickSort([100,2,56,35,6],0,4)