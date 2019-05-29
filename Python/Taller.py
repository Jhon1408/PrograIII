from pyDatalog import pyDatalog, pyEngine
import logging

#pyEngine.Logging = True
#logging.basicConfig(level=20)

pyDatalog.create_terms('factorial,N')

factorial[N] = N*factorial[N-1]
factorial[1] = 1

print(factorial[4]==N)  # prints N=6