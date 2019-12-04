import pickle
import bz2
import multiprocessing as mp
from math import cos
import dill
import pathos.multiprocessing as mp


#unpickle
filename = '/home/kavindie/Documents/git_repo/homework_fall2019/hw1/cs285/policies/experts/Ant.pkl'
infile = open(filename,'rb')
data = pickle.load(infile, encoding='bytes') #encoding param is only in python3
infile.close()

#expert data only has 2 demos
print(data.keys())
GaussianPolicyData = data["GaussianPolicy"] #you can have nonlin_type as well
hidden = GaussianPolicyData["hidden"] #you can have 'obsnorm', 'logstdevs_1_Da', 'out'
FeedforwardNet = hidden["FeedforwardNet"] #only this
layer_0 = FeedforwardNet["layer_0"]#only this
AffineLayer = layer_0["AffineLayer"]
W = AffineLayer["W"]
print (AffineLayer.keys())
print(type(W))
print(W.shape)

obsnorm = GaussianPolicyData["obsnorm"] #you can have 'obsnorm', 'logstdevs_1_Da', 'out'
Standardizer = obsnorm["Standardizer"]
print (Standardizer.keys())
print(type(Standardizer))

