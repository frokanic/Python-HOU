from typing import Final

"""
In Python, variables are declared as shown below, and are always mutable. 
'Final' can be used to indicate that a variable should not change its value, 
but this works as a hint for type checkers, rather than an enforcement 
of immutability.
"""

price = 50
price_final: Final = 100
