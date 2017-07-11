import matplotlib.pyplot as plt

from walker import Walker

# Make a random walker, plotting the points
wk = Walker()
wk.do_walk()

plt.scatter(wk.x_values, wk.y_values, s=15)
plt.show()
