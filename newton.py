def derivative(f, x, h=1e-5):
        """
        compute derivative
        """
        return (f(x + h) - f(x - h)) / (2 * h)

    
def newtons_method(x0, function): 
    while x0 = 1e-9:
        current_x = x0
        f_x0 = function lambda x: 0 
        f_x0prime = derivative(function)
        x_n1 = current_x - f_x0 / f_x0prime
    
    
    