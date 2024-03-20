from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

class RandomWalker(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        self.model.grid.move_agent(self, self.random.choice(self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)))

class WalkerModel(Model):
    def __init__(self, N):
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(10, 10, torus=True)
        for i in range(N):
            a = RandomWalker(i, self)
            self.schedule.add(a)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()