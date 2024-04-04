import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Example input data (user will replace with their own)
x = np.array([1, 2, 3, 9, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # Reshape to convert to a 2D array required by sklearn
y = np.array([2, 3, 5, 2, 1, 45, 3, 12, 5, 51])

# Perform linear regression
model = LinearRegression()
model.fit(x, y)

# Slope and intercept
slope = model.coef_[0]
intercept = model.intercept_

# Return calculated slope and intercept
slope, intercept

# Based on feedback, let's create a new plot with a cleaner and more aesthetic style.
# This time, we'll ensure the background is white, use only points (no "x"), and avoid gray color.

plt.rcParams.update(plt.rcParamsDefault)  # Reset to default values for a clean slate
plt.style.use('default')  # Use default style to ensure a white background and clean look

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Plot data points
ax.scatter(x, y, s=100, color='darkblue', label='', alpha=0.75, edgecolor='black')

# Plot the best fit line
ax.plot(x, model.predict(x), color='darkred', linewidth=2, label=f'$y = {slope:.2f}x + {intercept:.2f}$')

# Set titles and labels
ax.set_title('Linear Regression with Improved Styling', fontsize=16, fontweight='bold')
ax.set_xlabel('X-axis', fontsize=14)
ax.set_ylabel('Y-axis', fontsize=14)

# Add legend
ax.legend(loc='upper left', fontsize=12)

# Remove top and right borders for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust remaining spines to be less prominent
ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_linewidth(0.5)

# Adjust opacity and size of ticks to be less intrusive
ax.tick_params(colors='black', which='both', width=0.5)

plt.show()
