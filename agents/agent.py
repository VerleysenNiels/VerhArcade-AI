"""
This file contains the baseclass agent, every custom agent should inherit from
this class and override the functions that they need

Base agent selects a random action to play
"""

import numpy as np

class Agent:
  """
  Base class of an agent
    init: constructor
    act: retrieves the current state of the game and selects the action to take
    reset: reset the agent before playing a new game
  """
  def __init__(self, num_actions):
    """
    Constructor
      num_actions (int): number of actions that the agent can take
    """
    self.num_actions = num_actions

  def act(self, state):
    """
    Selects an action based on the state of the environment
      state (object): state retrieved from gym
    """
    return np.random.randint(0, self.num_actions)

  def reset(self):
    """
    Reset the agent before playing a new game
    You only need to implement this if your agent stores some information about 
    the game somewhere
    """
    return