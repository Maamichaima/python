import time

def get_seconds_1970():
    return (time.time())

second = get_seconds_1970()
print(f'Seconds since January 1, 1970: {second} or {second:.2e} in scientific notation')
