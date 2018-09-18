import snake_gym
import gym
import random

env = gym.make("snake-v0")
done = False
env.reset()
while not done:
    step = random.randint(0, 3)
    state, reward, done, info = env.step(step)
