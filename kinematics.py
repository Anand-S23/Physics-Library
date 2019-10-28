class Kinematics:
    def __init__(self, **kwargs): 
        givens = {
            'delta_x': None,
            'initial_vel': None, 
            'final_vel': None,
            'acc': None,
            'time': None,
        }

        for (field, val) in givens.items():
            setattr(self, field, kwargs.get(field, val))
    
    def delta_x(self):
        # delta x = (delta v / 2) * t
        if None not in (self.initial_vel, self.final_vel, self.time):
            self.delta_x = ((self.initial_vel + self.final_vel) / 2) * self.time 
            return self.delta_x
        else:
            return "NOT ENOUGH GIVENS"
        
    
    def final_velocity(self):
        # V = Vo + at
        if None not in (self.initial_vel, self.acc, self.time):
            self.final_vel = self.initial_vel + self.acc * self.time
            return self.final_vel
        elif None not in (self.initial_vel, self.final_vel, self.time):
            self.final_vel = 2*self.delta_x / self.time - self.initial_vel
            return self.delta_x
        else:
            return "NOT ENOUGH GIVENS"
    
    def ave_acceleration(self):
        # a = (V - Vo) / t
        if None not in (self.initial_vel, self.final_vel, self.time):
            self.acc = (self.final_vel - self.initial_vel) / self.time
            return self.acc
        else: 
            return "NOT ENOUGH GIVENS"

# Testing purposes
if __name__ == '__main__':
    x = Kinematics(initial_vel=5, acc=-9.8, time=10)
    print(x.final_velocity())
