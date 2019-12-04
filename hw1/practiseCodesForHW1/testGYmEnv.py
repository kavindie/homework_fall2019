'''import gym
env = gym.make('Ant-v1')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
env.close()'''

#The above can be done as follows in a more sophisticated way
import gym
env = gym.make('Ant-v1')
for i_episode in range(2):
    observation = env.reset()
    for t in range(10):
        env.render()
        #print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()

print(env.action_space)
#> Box(8,)
print(env.observation_space)
#> Box(11,)
print(env.observation_space.high)
#> array([ inf 111 times])
print(env.observation_space.low)
#> array([-inf 111 times])

from gym import spaces
space = spaces.Discrete(8) # Set with 8 elements {0, 1, 2, ..., 7}
x = space.sample()
assert space.contains(x)
assert space.n == 8

space2 = spaces.Box(low = -9, high = 2, shape = [4,2])
x = space2.sample()
print(type(space2))
print(x)
assert space2.contains(x)

from gym import envs
print(envs.registry.all())
allEnvs = list(envs.registry.all())
lastEnv= allEnvs[-1]
lastEnvID = lastEnv.id


