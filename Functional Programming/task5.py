import time

def measure_me(n):
    total = 0
    for i in range(n):
        total += i * i

    return total

def with_timing(func):

    def inner(*args, **kwargs):
        t1 = time.process_time_ns()
        result = func(*args, **kwargs)
        t2 = time.process_time_ns()
        print(f'Process completed in {t2 - t1} ns')
        return result

    return inner


measure_me = with_timing(measure_me)

print(measure_me(30))