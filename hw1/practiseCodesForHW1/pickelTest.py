import pickle
import bz2
import multiprocessing as mp
from math import cos
import dill
import pathos.multiprocessing as mp

#pickle
dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }

filename = 'dogs'
outfile = open(filename,'wb')

pickle.dump(dogs_dict,outfile)
outfile.close()

#unpickle
infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()

print(new_dict)
print(new_dict==dogs_dict)
print(type(new_dict))

#compress a pickle file to reuce size
sfile = bz2.BZ2File('smallerfile', 'w')
pickle.dump(dogs_dict, sfile)

##unpickle python2 objects in python 3
#infile = open(filename,'rb')
#new_dict = pickle.load(infile, encoding='latin1')

##In case of python2 objects having numpy arrays
#new_dict = pickle.load(infile, encoding='bytes')

#multiprocessing
'''Processes do not share memory space, so when they have to send information to each other, they use serialization, which is done using the pickle module.'''

p = mp.Pool(2) #amount of processors to use
p.map(cos, range(10))
print (p.map(cos, range(10)))

#Remember that lambda functions can't be pickled. So if you try to apply multiprocessing to a lambda function, it will fail.
dill.dump(lambda x: x**2, open('dillfile','wb'))

'''To use multiprocessing with a lambda function, or other data types unsupported by pickle, you will have to use a fork of multiprocessing called pathos.multiprocessing'''
p = mp.Pool(2)
lambda_map = p.map(lambda x: 2**x, range(10))

filename = 'lambda_dump'
outfile = open(filename,'wb')
dill.dump(lambda_map,outfile)
outfile.close()

infile = open(filename,'rb')
new_map = dill.load(infile)
infile.close()

print(new_map)
print(new_map==lambda_map)
print(type(new_map))
