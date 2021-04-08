import time

while True:
    old_time_str = input(' input time in format %H:%M:%S: ')
    old_time_struct = time.strptime("1971-01-01 " + old_time_str,
                                    "%Y-%m-%d %H:%M:%S")
    # start_time_struct = time.strptime("1971-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    old_time_float = time.mktime(old_time_struct)
    new_time_float = old_time_float + 1
    new_time_struct = time.localtime(new_time_float)
    new_time_str = time.strftime("%Y-%m-%d %H:%M:%S", new_time_struct)
    print(" Plus one second: " + new_time_str.split(' ')[-1]+'\n')
