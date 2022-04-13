from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)
#output:
26932
a[1:3]
#output:
array('H', [10, 700])


from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())
#output:
Handling task1


unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)


import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
scores
#output:
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]


from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
[heappop(data) for i in range(3)]  # fetch the three smallest entries
#output:
[-5, 0, 1]