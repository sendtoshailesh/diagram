"""
Python Matplotlib - Data Visualization
Install: pip install matplotlib numpy
"""

import matplotlib.pyplot as plt
import numpy as np

# Create figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Data Visualization Examples', fontsize=16)

# 1. Line Chart
x = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x), label='sin(x)', color='blue')
axes[0, 0].plot(x, np.cos(x), label='cos(x)', color='red')
axes[0, 0].set_title('Line Chart')
axes[0, 0].set_xlabel('X axis')
axes[0, 0].set_ylabel('Y axis')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# 2. Bar Chart
categories = ['Q1', 'Q2', 'Q3', 'Q4']
values = [23, 45, 56, 78]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
axes[0, 1].bar(categories, values, color=colors)
axes[0, 1].set_title('Quarterly Sales')
axes[0, 1].set_ylabel('Revenue ($K)')

# 3. Scatter Plot
x_scatter = np.random.randn(100)
y_scatter = np.random.randn(100)
colors_scatter = np.random.rand(100)
axes[1, 0].scatter(x_scatter, y_scatter, c=colors_scatter, cmap='viridis', alpha=0.6)
axes[1, 0].set_title('Scatter Plot')
axes[1, 0].set_xlabel('Feature 1')
axes[1, 0].set_ylabel('Feature 2')

# 4. Pie Chart
sizes = [30, 25, 20, 15, 10]
labels = ['Product A', 'Product B', 'Product C', 'Product D', 'Others']
explode = (0.1, 0, 0, 0, 0)
axes[1, 1].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
               shadow=True, startangle=90)
axes[1, 1].set_title('Market Share')

plt.tight_layout()
plt.savefig('data_visualization.png', dpi=300, bbox_inches='tight')
print("Chart saved as 'data_visualization.png'")
plt.show()
