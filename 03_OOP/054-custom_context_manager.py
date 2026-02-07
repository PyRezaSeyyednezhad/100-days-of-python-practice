# Implemented custom context managers in Python for safe resource management and execution time profiling.

# First Method: Using a Class-Based Context Manager
from datetime import datetime

class ExecutionTimer:
    def __enter__(self):
        print("Entering context...")
        self.start_time = datetime.now()
        return self  

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = datetime.now()
        execution_time = (end_time - self.start_time).total_seconds()
        print(f"Execution time: {execution_time:.3f} seconds")
        
        # اگر بخواهی خطاها را قورت بدهی True برگردان
        # اینجا False یعنی اگر خطایی رخ دهد، به بیرون پاس داده شود
        return False


# if __name__ == "__main__":
#     with ExecutionTimer():
#         from time import sleep
#         sleep(2)
#         print("Work done")


# Second Method: Using the @contextmanager Decorator

from contextlib import contextmanager
from datetime import datetime

@contextmanager
def execution_timer():
    print("Entering context...")
    start_time = datetime.now()
    try:
        yield  # اینجا کنترل به بلاک with داده می‌شود
    finally:
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        print(f"Execution time: {execution_time:.3f} seconds")


if __name__ == "__main__":
    from time import sleep
    with execution_timer():
        sleep(1.5)
        print("Task finished")
