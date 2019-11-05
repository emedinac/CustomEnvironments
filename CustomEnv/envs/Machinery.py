import gym
from gym import error, spaces, utils
from gym.utils import seeding

class MachineryEnv(gym.Env):
  metadata = {'render.modes': ['human']}
  def __init__(self):
    pass
  def step(self, action):
    return 0
  def reset(self):
    return 0
  def render(self, mode='human', close=False):
    return 0
