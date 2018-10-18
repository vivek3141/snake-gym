import gym, snake_gym
import neat
import pickle

env = gym.make("snake-tiled-v0")
state = env.reset()
done = False
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     './config')
genome = pickle.load(open("winner.pkl", "rb"))
net = neat.nn.FeedForwardNetwork.create(genome, config)
reward = 0
while not done:
    state = state.flatten()
    output = net.activate(state)
    output = output.index(max(output))
    s, reward, done, info = env.step(output)
    state = s
env.close()
print("Length: {}".format(reward))
