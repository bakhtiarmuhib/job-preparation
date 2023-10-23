from collections import deque

# list as stack
numbers_stack = [1,2,3,4,5]
numbers_stack.append(6) #push
numbers_stack.pop() #

# list as queue

queue = deque([1,2,3,4,5])
queue.append(6) # insert in last position
queue.popleft() # pop from left

