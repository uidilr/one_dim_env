import gym
from gym import spaces
import numpy as np

class TwoDimEnv(gym.Env):
    def __init__(self, episode_length=100):
        self.max_episode_length = episode_length
        self.min_action, self.max_action = -1, 1
        self.action_space = spaces.Box(low=self.min_action, high=self.max_action, shape=(2,), dtype=np.float32)
        self.observation_space = spaces.Box(low=-10, high=10, shape=(2,), dtype=np.float32)
        self.reset()

    def step(self, a):
        a = np.clip(np.asarray(a), self.min_action, self.max_action)
        self.state += a
        reward = -np.sum(np.square(self.state))
        self.episode_length += 1
        done = self.episode_length >= self.max_episode_length
        return self.state, float(reward), done, {}

    def reset(self):
        self.state = np.random.uniform(low=-5, high=5, size=(2,))
        self.episode_length = 0
        return self.state


if __name__ == "__main__":
    env = TwoDimEnv()

    n_episode = 5
    for _ in range(n_episode):
        done = False
        s = env.reset()
        while not done:
            s, reward, done, _ = env.step(np.asarray([0.01,0.01]))
            print(s, reward, done)
