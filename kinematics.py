class Kinematics:
    def __init__(self, **kwargs): 
        givens = {
            'dx': None,
            'initial_x': None,
            'final_x': None,
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
        elif None not in (self.initial_vel, self.acc, self.time):
            self.dx = self.initial_vel * self.time + .5 * self.acc * self.time**2 
        else:
            return "NOT ENOUGH GIVENS"
        return self.dx
        
    def final_velocity(self):
        # V = Vo + at
        if None not in (self.initial_vel, self.acc, self.time):
            self.final_vel = self.initial_vel + self.acc * self.time
        # V = 2 delta x / t - Vo
        elif None not in (self.initial_vel, self.final_vel, self.time):
            self.final_vel = 2*self.dx / self.time - self.initial_vel
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
