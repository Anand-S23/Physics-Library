class kinematics:
    def __init__(self, equation=None, init_vel=None, final_vel=None, acc=None, delta_time=None):
        self.equation = equation 
        self.init_vel = init_vel
        self.final_vel = final_vel
        self.acc = acc
        self.delta_time = delta_time
    
    def find_final_vel(self):
        # V = Vo + at
        if None not in (self.init_vel, self.acc, self.delta_time):
            self.final_vel = self.init_vel + self.acc * self.delta_time
            return self.final_vel
        else:
            return "NOT ENOUGH GIVENS"
    
    def find_acc(self):
        # a = (V - Vo) / t
        if None not in (self.init_vel, self.final_vel, self.delta_time):
            self.acc = (self.final_vel - self.init_vel) / self.delta_time
            return self.acc
        else: 
            return 

# Testing purposes
if __name__ == '__main__':
    x = kinematics(init_vel=5, acc=-9.8, delta_time=10)
    print(x.find_final_vel())