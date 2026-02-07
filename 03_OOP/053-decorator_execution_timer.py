# I implemented a reusable execution-time decorator in Python to profile function performance without modifying business logic.
from datetime import datetime
from time import sleep
from functools import wraps

def timer(func):
    @wraps(func)
    def innerFunc(*args, **kwargs):
        start = datetime.now()  
        try:
            result = func(*args, **kwargs) 
            return result
        finally:
            end = datetime.now()
            execution_time = (end - start).total_seconds()
            print(f"[TIMER] Function '{func.__name__}' executed in {execution_time:.3f} seconds")
    return innerFunc


@timer
def sleeps(seconds: int):
    sleep(seconds)
    return f"Done sleeping for {seconds} seconds"


@timer
def add(a: int, b: int):
    sleep(1)
    return a + b


if __name__ == "__main__":
    print(sleeps(2))
    print(add(2, 5))
