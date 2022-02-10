def has_int():
  #initializing an incrementing type variable
  count=0
  random_arr=[1,3,5,5,2]
  for x in range(len(random_arr)):
    if random_arr[count]==random_arr[count+1]:
      print(str(random_arr[count])+" is next to "+str(random_arr[count])+" in this array!")
      break;
    count=count+1
    
has_int()
#lets go it works
