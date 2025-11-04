
import math

def factorial(n):
    """Return n! (the factorial of n)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return 1 if n == 0 else n * factorial(n - 1)

def combinations(n, r):
    """Return number of combinations (n choose r)."""
    if r > n:
        return 0
    return math.comb(n, r)  
def permutations(n, r):
    """Return number of permutations (n permute r)."""
    if r > n:
        return 0
    return math.perm(n, r)  

def main():
    n = 5
    r = 3

    print(f"n = {n}, r = {r}")
    print(f"Factorial of {n}: {factorial(n)}")
    print(f"Combinations (n choose r): {combinations(n, r)}")
    print(f"Permutations (n permute r): {permutations(n, r)}")

if __name__ == "__main__":
    main()
