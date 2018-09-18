import snake_gym
import gym
import random

env = gym.make("snake-v0")
done = False
env.reset()
while True:
    step = random.randint(0, 3)
    state, done, reward, info = env.step(step)
