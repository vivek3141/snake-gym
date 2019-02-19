# Snake-AI
## Snake-Gym
[![Downloads](https://pepy.tech/badge/snake-gym)](https://pepy.tech/project/snake-gym)
[![PyPi Version](https://img.shields.io/pypi/v/snake-gym.svg)](https://pypi.python.org/pypi/snake-gym)
[![Python Compatibility](https://img.shields.io/pypi/pyversions/snake-gym.svg)](https://pypi.python.org/pypi/snake-gym)
[![License](https://img.shields.io/pypi/l/snake-gym.svg)](https://pypi.python.org/pypi/snake-gym)<br>

Contains a gym environment for the classic game snake.

### Implementing
* `env.render()` is not implemented, running it will raise `NotImplementedError`.
* `env.reset()` opens the GUI for the game. 
* `env.fps` contains the fps to run the game at. You can set it using:
    ```python
    env.fps = 60
    ```
### Installation
For the latest installation, run
```bash
git clone https://github.com/vivek3141/snake-ai
pip install -e .
```
You can install the latest release by
```bash
pip install snake-gym
```

### Creating The Environment
The environment can be created by doing the following:
```python
import gym
import snake_gym
env = gym.make("snake-v0")
```

### Environments
* `snake-v0` Returns a 150x150 RGB image in the form of a numpy array for the observations
* `snake-tiled-v0` Returns a 10x10 matrix for the observations. 
    * `0` is empty space
    * `1` is the snake
    * `2` is the food
