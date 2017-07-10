import matplotlib.pyplot as plt

numbers = [2, 4, 6, 8, 10, 12, 14]
points = [1, 2, 4, 8, 12, 17, 9]
plt.plot(numbers, points, linewidth=5)

# Chart title, label axes
plt.title("Favorite Numbers", fontsize=20)
plt.xlabel("Numbers", fontsize=14)
plt.ylabel("People Who Appreciate", fontsize=14)

# Size of tick labels
plt.tick_params(axis="both", labelsize=14)

plt.show()
