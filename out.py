def qsort(arr):
  if len(arr) <= 1:
    return arr
  else:
    return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])
