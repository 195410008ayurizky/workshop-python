from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
#output
0.57535828626024577
Timer('a,b = b,a', 'a=1; b=2').timeit()
#output:
0.54962537085770791