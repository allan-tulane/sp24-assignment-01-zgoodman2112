"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x<=1:
      return x
    else:
      ra = foo(x-1)
      rb = foo(x-2)
      return ra+rb

def longest_run(mylist, key):
  count = 0
  longest_count = 0
  for i in range(len(mylist)): #iterate thru list
      if mylist[i] == key:  #if current element is key, add to count
        count = count + 1
        longest_count = max(longest_count, count) #updating longest count to when count was the highest. 
                                                  #This gets the number of the most consecutive key elements
      else:
        count = 0 #when the current element is no longer the key, reset count to 0
  return longest_count


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    if len(mylist) == 0:          #if list is empty
      return Result(0, 0, 0, True)
    elif len(mylist) == 1:        #if list has 1 element
      if mylist[0] == key:
        return Result(1, 1, 1, True)  #if that 1 element matches the key
      else:
        return Result(0, 0, 0, False) #if that 1 element does not match the key

    #Separating list into left_list and right_list by splitting down   the middle
    middle = len(mylist)//2
    left_list = mylist[:middle]
    right_list = mylist[middle:]

    #Recursively call function for both sides and return Result       object as output
    left_side = longest_run_recursive(left_list, key)
    right_side = longest_run_recursive(right_list, key)

    #If the whole list is the key, this will be true
    is_entire = left_side.is_entire_range and right_side.is_entire_range

    #Stores the size of the left and right sizes
    l_size = left_side.left_size
    r_size = right_side.right_size

    #split_run_val stores the number of consecutive key elements when it overlaps from the left to right side 
    if mylist[middle] == key and mylist[middle-1] == key:
      split_run_val = left_side.right_size + right_side.left_size
    else:
      split_run_val = 0

  #If the entire left side is consecutive, update the value of l_size by adding it to the consecutive run on the right side 
    if left_side.is_entire_range:
      l_size = l_size + right_side.left_size
  #If the entire right side is consecutive, update the value of r_size by adding it to the consecutive run on the left side 
    if right_side.is_entire_range:
      r_size = r_size + left_side.right_size

  #Calculates the longest consecutive run by taking the maximum of the longest sizes of the left and right sides and the split run value. 
    longest = max(left_side.longest_size, right_side.longest_size, split_run_val)

  #Return the Result object with updated values for each of these attributes
    return Result(l_size, r_size, longest, is_entire)

  



  

  



