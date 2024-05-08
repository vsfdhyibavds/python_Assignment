def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False

print(large_power(10, 3))  # Output: False
print(large_power(10, 4))  # Output: True


def is_greater_than_5000(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False

print(is_greater_than_5000(10, 3))  # Output: False
print(is_greater_than_5000(10, 4))  # Output: True


def is_divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

print(is_divisible_by_ten(20))  # Output: True
print(is_divisible_by_ten(17))  # Output: False


def divisible_by_ten(num):
    return num % 10 == 0

print(divisible_by_ten(20))  # Output: True
print(divisible_by_ten(17))  # Output: False

