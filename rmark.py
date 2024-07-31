from random import choice, randint
from sys import argv
import justlogit as jli
import time

# Parsing args

args = {}

nextisvalue = None

for i in argv:
    if i[0] == '-':
        dtctd = False
        if i[1] == '-':
            ready = ''
            for cntr in range(2, len(i)):
                ready += i[cntr]
            dtctd = True
        else:
            ready = ''
            for cntr in range(1, len(i)):
                ready += i[cntr]
            if ready == 'n':
                ready = 'numbers'
                dtctd = True
            elif ready == 'c':
                ready == 'choice'
                dtctd = True
            elif ready == 'v':
                ready = 'verbose'
                dtctd = True
        if dtctd == True:
            nextisvalue = ready
            args[nextisvalue] = None
    elif nextisvalue != None:
        args[nextisvalue] = i
        nextisvalue = None


if "verbose" in args.keys():
    verbose = True
else:
    verbose = False
    

if "choice" in args.keys():
    mode = True
else:
    mode = False

try:
    numbers = int(args['numbers'])
except KeyError:
    numbers = 100000000

logger = jli.createLogger(printLogs = verbose, fileName = "rbenchmark.log")

logger.log('rMark 1.0.1 loaded')


logger.info(f'Configuration: {numbers} factors, verbose: {verbose}')

print("rMark 1.0.1")

print(f"Starting benchmark with numbers={numbers} and mode={mode}")

logger.info('Starting benchmark...')

starttime = round(time.time() * 1000)

if mode == True:
    logger.info("Selected mode: choice()")
    rng = range(1, 1000)
    for i in range(1, numbers):
        choice(range)
else:
    logger.info("Selected mode: randint()")
    for i in range(1, numbers):
        randint(1, 1000)

endtime = round(time.time() * 1000)

totaltime = endtime - starttime

logger.log(f'Testing ended. Result: {totaltime}')

print(jli.sinfo)

print(f'rMark points: {totaltime}')

logger.log('Exiting...')
