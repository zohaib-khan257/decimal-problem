





from decimal import Decimal, getcontext
from fractions import Fraction
 
getcontext().prec = 28
 
 
def float_roundtrip(a, b):
    quotient = a / b
    result = quotient * b
    return quotient, result
 
 
def decimal_roundtrip(a, b):
    da, db = Decimal(a), Decimal(b)
    quotient = da / db
    result = quotient * db
    return quotient, result
 
 
def exact_roundtrip(a, b):
    quotient = Fraction(a, 1) / Fraction(b, 1)
    result = quotient * b
    return quotient, result
 
 
def report(a, b):
    print(f"\n{'=' * 55}")
    print(f"  {a} / {b}, then result * {b}")
    print(f"{'=' * 55}")
 
    fq, fr = float_roundtrip(a, b)
    print(f"float    : {a}/{b} = {fq!r}")
    print(f"           back to   = {fr!r}")
    print(f"           lost/gained = {a - fr!r}")
 
    dq, dr = decimal_roundtrip(a, b)
    print(f"decimal  : {a}/{b} = {dq}")
    print(f"           back to   = {dr}")
    print(f"           lost/gained = {Decimal(a) - dr}")
 
    xq, xr = exact_roundtrip(a, b)
    print(f"fraction : {a}/{b} = {xq}  (~{float(xq):.15f})")
    print(f"           back to   = {xr}")
    print(f"           lost/gained = {a - xr}  <-- always exactly 0, no rounding used")
 
 
if __name__ == "__main__":
    for a, b in [(100, 3), (10, 7), (1, 3), (22, 7)]:
        report(a, b)