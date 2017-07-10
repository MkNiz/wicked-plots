import matplotlib.pyplot as plt

points = [1, 2, 4, 8, 12, 17, 9]
plt.plot(points, linewidth=5)

# Chart title, label axes
plt.title("Representation of My List", fontsize=20)
plt.xlabel("Index", fontsize=14)
plt.ylabel("Value", fontsize=14)

# Size of tick labels
plt.tick_params(axis="both", labelsize=14)

plt.show()
