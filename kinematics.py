class Kinematics:
    def __init__(self, **kwargs): 
        givens = {
            'init_vel': None, 
            'final_vel': None,
            'acc': None,
            'delta_time': None
        }

        for (field, val) in givens.items():
            setattr(self, field, kwargs.get(field, val))
    
    def final_velocity(self):
        # V = Vo + at
        if None not in (self.init_vel, self.acc, self.delta_time):
            self.final_vel = self.init_vel + self.acc * self.delta_time
            return self.final_vel
        else:
            return "NOT ENOUGH GIVENS"
    
    def average_acc(self):
        # a = (V - Vo) / t
        if None not in (self.init_vel, self.final_vel, self.delta_time):
            self.acc = (self.final_vel - self.init_vel) / self.delta_time
            return self.acc
        else: 
            return 

# Testing purposes
if __name__ == '__main__':
    x = Kinematics(init_vel=5, acc=-9.8, delta_time=10)
    print(x.final_velocity())
