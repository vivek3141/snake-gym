import os
import neat
import gym, snake_gym
import pickle
import multiprocessing as mp
from visualize import *

gym.logger.set_level(40)


class Train:
    def __init__(self, generations, parallel=5):
        self.generations = generations
        self.lock = mp.Lock()
        self.par = parallel

    def _fitness_func(self, genome, config, queue):
        env = gym.make('snake-tiled-v0')
        try:
            state = env.reset()
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            done = False
            reward = 0
            while not done:
                state = state.flatten()
                output = net.activate(state)
                output = Train._get_actions(output)
                s, reward, done, info = env.step(output)
                state = s

            fitness = -1 if reward == 0 else reward
            queue.put(fitness)
            env.close()
        except KeyboardInterrupt:
            env.close()
            exit()

    @staticmethod
    def _get_actions(a):
        return a.index(max(a))

    def _eval_genomes(self, genomes, config):
        idx, genomes = zip(*genomes)

        for i in range(0, len(genomes), self.par):
            output = mp.Queue()

            processes = [mp.Process(target=self._fitness_func, args=(genome, config, output)) for genome in
                         genomes[i:i + self.par]]

            [p.start() for p in processes]
            [p.join() for p in processes]

            results = [output.get() for p in processes]

            for n, r in enumerate(results):
                genomes[i + n].fitness = r

    def _run(self, config_file, n):
        config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                             neat.DefaultSpeciesSet, neat.DefaultStagnation,
                             config_file)
        p = neat.Population(config)
        p.add_reporter(neat.StdOutReporter(True))
        p.add_reporter(neat.Checkpointer(5))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)
        winner = p.run(self._eval_genomes, n)
        pickle.dump(winner, open('winner.pkl', 'wb'))
        draw_net(config, winner, True)
        plot_stats(stats, ylog=False, view=True)
        plot_species(stats, view=True)

    def main(self, config_file='config'):
        local_dir = os.path.dirname(__file__)
        config_path = os.path.join(local_dir, config_file)
        self._run(config_path, self.generations)


if __name__ == "__main__":
    t = Train(10000)
    t.main()
