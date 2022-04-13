import math
math.cos(math.pi / 4)
#output:
0.70710678118654757
math.log(1024, 2)
#output:
10.0

import random
random.choice(['apple', 'pear', 'banana'])
#output:
'apple'
random.sample(range(100), 10)   # sampling without replacement
#output:
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
random.random()    # random float
#output:
0.17970987693706186
random.randrange(6)    # random integer chosen from range(6)
#output:
4

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
#output:
1.6071428571428572
statistics.median(data)
#output:
1.25
statistics.variance(data)
#output:
1.3720238095238095