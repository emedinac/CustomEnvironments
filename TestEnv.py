import gym
import CustomEnv
import numpy as np

env = gym.make('valves-v0')

state = env.reset()
counter = 0
reward = None
while counter != 50000:
    env.render()
    actions = np.random.choice([-1,1],env.action_space.shape)
    # state, reward, done, info = env.step(env.action_space.sample())
    state, reward, done, info = env.step(actions) 
    counter += 1
    if done:
        state = env.reset()
    if counter%5000==0:
        state = env.reset()
    print(counter, done, reward)