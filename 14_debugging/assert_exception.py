import traceback

# assertions target programmer errors VS exceptions target user errors

#assertions check if condition is met in code (sanity check)
begonia_yckroad = {'yck_road': 'green', 'begonia': 'red'}

def switch_lights(intersection):
    for direction in intersection.keys():
        if intersection[direction] == 'green':
            intersection[direction] = 'yellow'
        elif intersection[direction] == 'yellow':
            intersection[direction] = 'red'
        elif intersection[direction] == 'red':
            intersection[direction] = 'green'
    assert "red" in intersection.values(), "no lights are red" + str(intersection)
try: #always fails in this case
    switch_lights(begonia_yckroad)
except AssertionError:
    error_log = open('.\\14_debugging\\error_log.txt', 'a')
    error_log.write(traceback.format_exc() + '\n')
    error_log.close()
    print("error was logged")

#exceptions catch errors and stops code
try:
    raise Exception('error test')
except: #will run either way because raise exception always leads to error
    error_log = open('.\\14_debugging\\error_log.txt', 'a') #creates or appends
    error_log.write(traceback.format_exc() + '\n') #writes the exception error and cause
    error_log.close()
    print('error was logged')