import pickle
import bz2
import multiprocessing as mp
from math import cos
import dill
import pathos.multiprocessing as mp


#unpickle
filename = '/home/kavindie/Documents/git_repo/homework_fall2019/hw1/cs285/expert_data/expert_data_Ant-v2.pkl'
infile = open(filename,'rb')
data = pickle.load(infile, encoding='bytes') #encoding param is only in python3
infile.close()

#expert data only has 2 demos
print(data[0])
firstDemo = data[0]
obs = firstDemo['observation']
im_obs = firstDemo["image_obs"]
rewards = firstDemo["reward"]
act = firstDemo["action"]
next_obs = firstDemo["next_observation"]
terminal = firstDemo["terminal"]

#first observation = state
print(obs[0,:])
#reward with first observation
print (rewards.item((0,)))
#first action
print(act[0,:])
#next observation = state
print(next_obs[0,:])
#terminal condition
print(terminal.item((0,)))

#print (im_obs.size == 0)
print(firstDemo.keys())

