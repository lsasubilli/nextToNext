def has_int():
  count=0
  random_arr=[1,3,5,5,2]
  for x in range(len(random_arr)):
    if random_arr[count]==random_arr[count+1]:
      print("The value of "+str(random_arr[count])+" is "+str(random_arr[count]))
      break;
    count=count+1
    
has_int()
