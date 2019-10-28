# Physics Library 
Python library which will help preforming physics computations. 

## Kinematics 

It is a work in progress, only 1D kinematics implemented. Somethings to keep in mind is the units of what is passed in. This program does not deal with units, so if the answer needs to be in a certain unit, keep that in mind. Later on down the road, there might be a feature like that implemented.

Current Features
- displacement: returns the change in x of the object, depending on the parameters
- final_velocity: returns the final velocity of the object, depending on the parameters
- acceraltion: returns the acceraltion of the object, depending on the parameters (this is only if acceration is constant)

Parameters
- dx: change in x (Xf - Xo)
- inital_x: the starting x postion
- final_x: the ending x postion
- inital_vel: the starting velocity
- final_vel: the ending velocity
- acc: the acceraltion
- time: the time period 
 

Some example code: 

```
import kinematics

car = Kinematics(inital_vel=0, final_vel=10, time=10)
car_acc = car.accleration()

print(car_acc)

'''
# Ouput
>>> 1.0 
'''
```