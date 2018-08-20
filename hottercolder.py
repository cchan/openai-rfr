# Based on https://gym.openai.com/envs/HotterColder-v0/
import numpy as np

class ManualHotterColderAgent(object):
    def __init__(self):
        self.currStep = 0.3
        pass
    def act(self, state, reward):
        if state == 0:
            self.prevGuess = 0.5
        if state == 1:
            self.prevGuess += self.currStep
        elif state == 3:
            self.prevGuess -= self.currStep
        self.currStep *= 0.8
        return self.prevGuess

class HotterColderEnvironment:
    def __init__(self):
        self.target = np.random.random()
    def episode(self, action):
        state = 1 if action < self.target else 2 if action == self.target else 3
        reward = - (action - self.target) ** 2
        return state, reward

if __name__ == "__main__":
    agent = ManualHotterColderAgent()
    env = HotterColderEnvironment()
    state = 0
    reward = 0
    for i in range(20):
        state, reward = env.episode(agent.act(state, reward))
        print(state, reward)
