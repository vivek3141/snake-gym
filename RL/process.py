import snake_gym
import gym
import cv2
import numpy as np

env = gym.make("snake-v0")
state, r, d, inf = env.step(1)
state = cv2.cvtColor(state, cv2.COLOR_BGR2RGBA)
cv2.imshow("a", state)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
