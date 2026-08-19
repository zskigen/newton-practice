def derivative(f, x, h=1e-5):
        """
        compute derivative
        """
        return (f(x + h) - f(x - h)) / (2 * h)

def function_value(function, value):
    return function(value)


def newtons_method(x0, function): 
     while True:
         #calculate function value and derivative value at current x
         func_val = function_value(function, x0) 
         derivative_calc = derivative(function, x0)

         #check if derivative is too close to 0
         if abs(derivative_calc) < 1e-9:
             print("too close to 0")
             break

         #Calculate the next x
         x_n1 = x0 - (func_val / derivative_calc)

        #check if the difference between x_n1 and x0 is tiny
         if abs(x_n1 - x0) < 1e-9:
             return x_n1
       
        #update  current x to be the new x_new for the next round
        x0 = x_n1


    
    
    
    