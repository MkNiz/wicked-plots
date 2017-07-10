import matplotlib.pyplot as plt

numbers = [2, 4, 6, 8, 10, 12, 14]
faves = [1, 2, 4, 8, 12, 17, 9]

plt.scatter(numbers, faves, s=100)

# Set title, label axes
plt.title("Favorite Numbers", fontsize=24)
plt.xlabel("Number", fontsize=14)
plt.ylabel("People Who Appreciate", fontsize=14)

# Size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
