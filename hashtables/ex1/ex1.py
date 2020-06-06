def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    for i in range(len(weights)):
        if weights[i] not in cache:
            cache[weights[i]] = [i]
        else:
            cache[weights[i]].append(i) 
   
    array = []
    for x in cache:
        target = limit - x
      
        if target in cache:
            array.append(cache[target])     

    finalArray = [item for sublist in array for item in sublist] 
    
    finalArray.sort(reverse=True)
    
    if len(array) < 1:
        return None
    else:
        return finalArray

print(get_indices_of_item_weights([4, 4], 2, 8))
