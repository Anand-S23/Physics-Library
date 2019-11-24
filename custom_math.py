import math
 
def quadratic(self, a, b, c):
 
    d = b**2 - 4 * a * c
  
    if d > 0:
        ans_one = (-b - math.sqrt(d)) / (2 * a)
        and_two = (-b + math.sqrt(d)) / (2 * a)
        
        return ans_one, ans_two
    return "Error occured, could not preform action - discriminat is negative"
