def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibo_sequence = [0, 1]

    while len(fibo_sequence) < n:
        next_number = fibo_sequence[-1] + fibo_sequence[-2]
        fibo_sequence.append(next_number)

    return fibo_sequence

