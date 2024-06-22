def factors(number):
    divisor = number
    if divisor < 0:
        divisor *= -1
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

factors(-7)