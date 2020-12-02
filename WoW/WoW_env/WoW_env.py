import gym
from gym import spaces
import numpy as np
from .WoW import WoW

class WoW_env(gym.Env):
    # metadata = {'render.modes' : ['human']}
    def __init__(self):
        self.game = WoW()
        self.action_space = spaces.Discrete(22)
        self.observation_space = spaces.Box(np.array([0, 0, 0, 0, 0, 0, 0, 0]), np.array([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]), dtype=np.int) # information about x and y of all players 

    def reset(self):
        del self.game
        self.game = WoW()
        obs = self.game.Observe()

        return obs

    def step(self, action):
        self.game.Action(action)
        obs = self.game.Observe()
        reward = self.game.Evaluate()
        done = self.game.Is_Done()

        return obs, reward, done, {}
  