from datetime import datetime

"""
Decorator used to determine calculation time for a function
"""
def runtime_calc(func):
    def wrapper():
        step_time_start = datetime.now()
        func()
        step_time_end = datetime.now()
        step_time_interval = step_time_end - step_time_start
        s = step_time_interval.seconds
        ms = f'00{int(step_time_interval.microseconds / 1000)}'[-3:]
        step_time_string = f'{s % 60}.{ms}'
        print(f"Runtime for this iteration: {step_time_string} seconds")
    return wrapper

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
