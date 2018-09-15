import snake_gym
import gym
from PIL import Image

env = gym.make("snake-v0")
state, r, d, inf = env.step(1)
print(state)
img = Image.fromarray(state, 'RGBA')
img.save('my.png')
img.show()
