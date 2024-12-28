import numpy as np

def f(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

def riemann_sum(n):
    dx = 1 / n 
    total_sum = 0

    for i in range(n):
        x = i * dx
        for j in range(n):
            y = j * dx
            for k in range(n):
                z = k * dx
                total_sum += f(x, y, z)

    return total_sum * dx**3  

def monte_carlo_integration(num_samples):
    samples_x = np.random.uniform(0, 1, num_samples)
    samples_y = np.random.uniform(0, 1, num_samples)
    samples_z = np.random.uniform(0, 1, num_samples)

    values = f(samples_x, samples_y, samples_z)
    integral = np.mean(values)  
    return integral

def main():
    n_riemann = 100 
    num_samples_monte_carlo = 100000 

    riemann_result = riemann_sum(n_riemann)
    monte_carlo_result = monte_carlo_integration(num_samples_monte_carlo)

    print(f"Riemann Sum Result with n={n_riemann}: {riemann_result}")
    print(f"Monte Carlo Method Result with {num_samples_monte_carlo} samples: {monte_carlo_result}")

if __name__ == "__main__":
    main()
