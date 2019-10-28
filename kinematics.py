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
            't': None,
        }

        for (field, val) in givens.items():
            setattr(self, field, kwargs.get(field, val))
    
    def __str__(self):
        return 'KinematicBody class'

    def __repr__(self):
        return 'KinematicBody()'

    def displacement(self):
        # delta x = (delta v / 2) * t
        if None not in (self.initial_vel, self.final_vel, self.t):
            self.dx = ((self.initial_vel + self.final_vel) / 2) * self.t 
        # delta x = Vo*t + (1/2)a*t^2
        elif None not in (self.initial_vel, self.acc, self.t):
            self.dx = self.initial_vel * self.t + .5 * self.acc * self.t**2 
        # delta x = (V^2 - Vo^2) / 2a
        elif None not in (self.final_vel, self.final_vel, self.acc):
            self.dx = (self.final_vel**2 - self.initial_vel**2) / (2 * self.acc)
        else:
            return "NOT ENOUGH GIVENS"
        return self.dx
    
    def average_veloctiy(self):
        # V(bar) = delta x / delta t
        if None not in (self.dx, self.t):
            self.ave_vel = self.dx / self.t
        else:
            return "NOT ENOUGH GIVENS"
        return self.ave_vel
    
    def initial_velocity(self):
        # Vo = V - a*t
        if None not in (self.final_vel, self.acc, self.t):
            self.initial_vel = self.final_vel - (self.acc * self.t)
        # Vo = 2 delta x / t - V
        elif None not in (self.dx, self.t, self.final_vel):
            self.initial_vel = (2 * self.dx) / self.t - self.final_vel
        # Vo = sqrt(V**2 - 2a*delta x)
        elif None not in (self.final_vel, self.acc, self.dx):
            self.initial_vel = math.sqrt(self.final_vel**2 - 2 * self.acc * self.dx)
        # Vo = (delta x - (1/2)at^2) t 
        elif None not in (self.dx, self.acc, self.t):
            self.initial_vel = (self.dx - .5 * self.acc * self.t**2) / self.t
        else: 
            return "NOT ENOUGH GIVENS"
        return self.initial_vel

    def final_velocity(self):
        # V = Vo + at
        if None not in (self.initial_vel, self.acc, self.t):
            self.final_vel = self.initial_vel + self.acc * self.t
        # V = 2 delta x / t - Vo
        elif None not in (self.initial_vel, self.final_vel, self.t):
            self.final_vel = 2*self.dx / self.t - self.initial_vel
        # V = sqrt(Vo^2 + 2ax)
        elif None not in (self.initial_vel, self.acc, self.dx):
            self.initial_vel = math.sqrt(self.initial_vel**2 + 2 * self.acc * self.dx)
        else:
            return "NOT ENOUGH GIVENS"
        return self.final_vel
    
    def acceleration(self):
        # a = (V - Vo) / t
        if None not in (self.initial_vel, self.final_vel, self.t):
            self.acc = (self.final_vel - self.initial_vel) / self.t
        # a = 2(x- vt) / t^2
        elif None not in (self.dx, self.initial_vel, self.t):
            self.acc = 2 * (self.dx - self.initial_vel * self.t) / self.t**2
        else: 
            return "NOT ENOUGH GIVENS"
        return self.acc

    def time(self):
        pass
    

# Testing purposes
if __name__ == '__main__':
    x = Kinematics(initial_vel=0, acc=3.2, t=32.8)
    x2 = Kinematics(initial_vel=0, final_vel=10, t=10)
    print(x.displacement())
    print(x.final_velocity())
    print(x2.displacement())
    print(x2.final_velocity())
    print(x2.ave_acceleration())
