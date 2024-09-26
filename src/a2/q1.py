import numpy as np
import matplotlib.pyplot as plt

# Years and corresponding transistor counts (in millions)
years_cpu = np.array([1972, 1974, 1978, 1982, 1985, 1989, 1993, 1997, 1999, 2000, 2003, 2004, 2007, 2008, 2012])
observed_transistors = np.array([0.0025, 0.005, 0.029, 0.12, 0.275, 1.18, 3.1, 7.5, 24.0, 42.0, 220.0, 592.0, 1720.0, 2046.0, 3100.0])

initial_year = 1972
initial_transistor_count = 0.0025  # Millions

# Compute based on Moore's Law
log_initial_transistor = np.log10(initial_transistor_count)
years_passed = years_cpu - initial_year
predicted_log_transistors = log_initial_transistor + (years_passed / 2) * np.log10(2)
predicted_transistors = 10**predicted_log_transistors

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(years_cpu, observed_transistors, 'bo-', label='Observed Transistors')
plt.plot(years_cpu, predicted_transistors, 'r--', label='Predicted by Moore\'s Law')
plt.ylabel('Transistors (millions)')
plt.title("CPU Transistor Count: Observed vs Moore's Law Prediction")
plt.legend()
plt.xlabel('Year')
plt.yscale('log')
plt.grid(True, which="both", linestyle="--")
plt.show()
