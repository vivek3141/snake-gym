# Snake AI
Contains a gym environment for the classic game snake.
<br>
Implementation for the NEAT algorithm and RL agents can be found in `examples/`

## Implementing
* `env.render()` is not implemented, running it will raise `NotImplementedError`.
* `env.reset()` opens the GUI for the game. 
* `env.fps` contains the fps to run the game at. You can set it using:
    ```python
    env.fps = 60
    ```
