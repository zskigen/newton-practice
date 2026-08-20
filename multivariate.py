import jax 
import jax.numpy as jnp 

def gradient(f, x):
    """
    computes gradient of function
    """
    return jax.grad(f)(x)
    
def gradient2(f, x):
    """
    computes second gradient of a function
    """
    return jax.hessian(f)(x)


def optimize(x0, f, tol=1e-4):
    # Convert input to a jax array for vector math
    x0 = jnp.array(x0, dtype=jnp.float32)
    
    # H_inverse * grad
    step = jnp.linalg.solve(gradient2(f, x0), gradient(f, x0))
    x_new = x0 - step
    x = x0
    
    # jnp.linalg.norm replaces 'abs()' for checking vector distances
    while jnp.linalg.norm(x_new - x) > tol:
        x = x_new
        step = jnp.linalg.solve(gradient2(f, x), gradient(f, x))
        x_new = x - step
        
    return {"x": x_new, 'value': f(x_new)}