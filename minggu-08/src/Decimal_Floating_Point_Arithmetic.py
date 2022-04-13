from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)
#output:
Decimal('0.74')

round(.70 * 1.05, 2)
#output:
0.73


Decimal('1.00') % Decimal('.10')
Decimal('0.00')
1.00 % 0.10
#output:
0.09999999999999995

sum([Decimal('0.1')]*10) == Decimal('1.0')
#output:
True
sum([0.1]*10) == 1.0
#output:
False


getcontext().prec = 36
Decimal(1) / Decimal(7)
#output:
Decimal('0.142857142857142857142857142857142857')