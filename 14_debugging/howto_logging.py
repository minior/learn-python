import logging

print(5+2)

logging.disable(logging.DEBUG) # disables all log messages critical or below (5 levels)
logging.basicConfig(filename='.\\14_debugging\\logging.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# inc "filename=" argument to save log to file
# long string with % is just the entire logging statement
 
#not working factorial calculator
logging.debug('start of prog') # .debug is lowest log level

def factorial_calc(n):
    logging.debug('start of factorial (%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.warning('return value is %s' % (total)) # this still logs because warning > debug
    print(total) 

factorial_calc(5)


#a simple factorial calculator (WORKS)
def factorial_calc(n):
    total = 1
    for i in range(n): # we can also do range(1, n+1) ie. start from 1, iterate n+1 times
        total *=(i+1)
    print(total) 

factorial_calc(5)