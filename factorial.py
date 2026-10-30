def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(f"5! = {factorial(5)}")
