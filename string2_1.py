#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  new_list = set()
  start_index = 0
  while start_index < len(nums)-1:
    if nums[start_index]==nums[start_index+1]:
      nums.pop(start_index+1)
      start_index = 0
    else:
      start_index = start_index + 1
  '''
  for (index,item) in enumerate(nums,start=0):
    if item==nums.index(index):
      nums.remove(nums.index(index))
  '''
  return nums


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  new_list = list()
  list1Len = len(list1)
  list2Len = len(list2)
  biggerList = list()
  smallerList = list()
  if list1Len > list2Len:
    biggerList = list1
    smallerList = list2
  else:
    biggerList = list2
    smallerList = list1
  item1Marked = False
  indexAdded = 0
  indexS = 0
  indexB = 0
  for item1 in biggerList:
    for item2 in smallerList:
      if item1 < item2 and item1 not in new_list:
        new_list.append(item1)
      elif item2 < item1 and item2 not in new_list:
        new_list.append(item2)
      elif item1==item2:
        new_list.append(item2)
        if not item1Marked:
            new_list.append(item1)
            item1Marked = True
      indexS = indexS + 1
    indexB = indexB + 1
    if indexB > len(smallerList):
        new_list.append(item1)

  return new_list

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
