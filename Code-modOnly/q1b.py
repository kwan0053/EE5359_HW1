import numpy as np

def simulate_steps(start_state, steps=7, iterations=10000):
    # R1: 2X1 + X2 -> 4X3 (k1=1)  -> [-2, -1, 4]
    # R2: X1 + 2X3 -> 3X2 (k2=2)  -> [-1, 3, -2]
    # R3: X2 + X3  -> 2X1 (k3=3)  -> [2, -1, -1]
    
    results = []
    
    for _ in range(iterations):
        state = np.array(start_state, dtype=float)
        
        for _ in range(steps):
            x1, x2, x3 = state
            
            # Calculate weights (propensities)
            # R1: k1 * (x1 choose 2) * x2 = 1 * [x1(x1-1)/2] * x2
            w1 = 0.5 * x1 * (x1 - 1) * x2
            # R2: k2 * x1 * (x3 choose 2) = 2 * x1 * [x3(x3-1)/2] = x1 * x3 * (x3-1)
            w2 = x1 * x3 * (x3 - 1)
            # R3: k3 * x2 * x3 = 3 * x2 * x3
            w3 = 3 * x2 * x3
            
            total_w = w1 + w2 + w3
            
            # If no reactions can fire, break early
            if total_w == 0:
                break
                
            # Determine which reaction fires
            r = np.random.uniform(0, total_w)
            if r < w1:
                state += [-2, -1, 4]
            elif r < w1 + w2:
                state += [-1, 3, -2]
            else:
                state += [2, -1, -1]
        
        results.append(state)
        
    results = np.array(results)
    
    means = np.mean(results, axis=0)
    variances = np.var(results, axis=0)
    
    return means, variances

# Initial State S = [9, 8, 7]
m, v = simulate_steps([9, 8, 7])

print(f"After 7 steps (Average over 10,000 runs):")
print(f"X1: Mean = {m[0]:.2f}, Variance = {v[0]:.2f}")
print(f"X2: Mean = {m[1]:.2f}, Variance = {v[1]:.2f}")
print(f"X3: Mean = {m[2]:.2f}, Variance = {v[2]:.2f}")
