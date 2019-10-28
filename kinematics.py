import math

class KinematicBody:
    def __init__(self, **kwargs): 
        givens = {
            'dx': None,
            'initial_x': None,
            'final_x': None,
            'ave_vel': None,
            'initial_vel': None, 
            'final_vel': None,
            'acc': None,
            'time': None,
        }

        for (field, val) in givens.items():
            setattr(self, field, kwargs.get(field, val))
    
    def displacement(self):
        # delta x = (delta v / 2) * t
        if None not in (self.initial_vel, self.final_vel, self.time):
            self.dx = ((self.initial_vel + self.final_vel) / 2) * self.time 
        # delta x = Vo*t + (1/2)a*t^2
        elif None not in (self.initial_vel, self.acc, self.time):
            self.dx = self.initial_vel * self.time + .5 * self.acc * self.time**2 
        # delta x = (V^2 - Vo^2) / 2a
        elif None not in (self.final_vel, self.final_vel, self.acc):
            self.dx = (self.final_vel**2 - self.initial_vel**2) / (2 * self.acc)
        else:
            return "NOT ENOUGH GIVENS"
        return self.dx
    
    def initial_velocity(self):
        # Vo = V - a*t
        if None not in (self.final_vel, self.acc, self.time):
            self.initial_vel = self.final_vel - (self.acc * self.time)
        # Vo = 2 delta x / t - V
        elif None not in (self.dx, self.time, self.final_vel):
            self.initial_vel = (2 * self.dx) / self.time - self.final_vel
        # Vo = sqrt(V**2 - 2a*delta x)
        elif None not in (self.final_vel, self.acc, self.dx):
            self.initial_vel = math.sqrt(self.final_vel**2 - 2 * self.acc * self.dx)
        # Vo = (delta x - (1/2)at^2) t 
        elif None not in (self.dx, self.acc, self.time):
            self.initial_vel = (self.dx - .5 * self.acc * self.time**2) / self.time
        else: 
            return "NOT ENOUGH GIVENS"
        return self.initial_vel

    def final_velocity(self):
        # V = Vo + at
        if None not in (self.initial_vel, self.acc, self.time):
            self.final_vel = self.initial_vel + self.acc * self.time
        # V = 2 delta x / t - Vo
        elif None not in (self.initial_vel, self.final_vel, self.time):
            self.final_vel = 2*self.dx / self.time - self.
        # V = sqrt(Vo^2 + 2ax)
        elif None not in (self.initial_vel, self.acc, self.dx):
            self.initial_vel = math.sqrt(self.initial_vel**2 + 2 * self.acc * self.dx)
        else:
            return "NOT ENOUGH GIVENS"
        return self.final_vel
    
    def acceleration(self):
        # a = (V - Vo) / t
        if None not in (self.initial_vel, self.final_vel, self.time):
            self.acc = (self.final_vel - self.initial_vel) / self.time
        else: 
            return "NOT ENOUGH GIVENS"
        return self.acc
    

# Testing purposes
if __name__ == '__main__':
    x = Kinematics(initial_vel=0, acc=3.2, time=32.8)
    x2 = Kinematics(initial_vel=0, final_vel=10, time=10)
    print(x.displacement())
    print(x.final_velocity())
    print(x2.displacement())
    print(x2.final_velocity())
    print(x2.ave_acceleration())
