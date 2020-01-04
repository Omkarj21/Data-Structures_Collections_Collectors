# Important Packages = math, binary, decimal, fraction
# -------------------------------------
# Numerical literals :
#     integer, float, complex
# -------------------------------------
# Output: <class 'int'>
print(type(2))
# Output: <class 'float'>
print(type(2.0))
# Output: (15+2j)
a = 9 + 2j
print(a + 6)
# Output: True
print(isinstance(a, complex))
# -------------------------------------
# Output: 59
print(0b111011)
# Output: 173 (171 + 2)
print(0xAB + 0b10)
# Output: 250
print(0xFA)
# Output: 9
print(0o11)
# -------------------------------------
# fractions Module
from fractions import Fraction as f
# Output: 3/2
print(f(1.5))
# Output: 5
print(f(5))
# Output: 1/3
print(f(1,3))
# Output: 2/3
print(f(1,3) + f(1,3))
# Output: 6/5
print(1 / f(5,6))
# Output: False
print(f(-3,10) > 0)
# Output: True
print(f(-3,10) < 0)
# -----------------------------------------------------------------------------------------------
# math module
import math
# Output: 3.141592653589793
print(math.pi)
# Output: -1.0
print(math.cos(math.pi))
# Output: 22026.465794806718
print(math.exp(10))
# Output: 3.0
print(math.log10(1000))
# Output: 1.1752011936438014
print(math.sinh(1))
# Output: 720
print(math.factorial(6))
# -------------------------------------
# decimal module
from decimal import Decimal as D
# Output: Decimal('3.3')
print(D('1.1') + D('2.2'))
# Output: Decimal('3.000')
print(D('1.2') * D('2.50'))
# -------------------------------------