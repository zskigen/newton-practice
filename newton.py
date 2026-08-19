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
         func_val = function_value(value) 
         derivative_calc = derivative(x0)

         #check if derivative is too close to 0 

         if derivative_calc < 1e-9:
             then print("too close to 0")

        #Calculate the next x

        x_n1 = current_x - f_x0 / f_x0prime

        #check if the difference between x_n1 and x0 is tiny
        if abs(x_n1 - x) < 1e-9:
            then break 
       #update  current x to be the new x_new for the next round
        


    
        
    
    
    