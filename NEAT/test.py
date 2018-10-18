import gym, snake_gym
import random

env = gym.make("snake-tiled-v0")
state = env.reset()
done = False
while not done:
    state, reward, done, _ = env.step(random.randint(0, 3))

print("Length: {}".format(reward))
