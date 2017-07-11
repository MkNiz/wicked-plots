import matplotlib.pyplot as plt

numbers = [-5, 10, 70, 4, 24, 2, -30, 120]
mean = sum(numbers) / float(len(numbers))
distances = [abs(mean - x) for x in numbers]

plt.scatter(numbers, distances, c=distances, cmap=plt.cm.Blues, edgecolor='none', s=40)

# Set title, label axes
plt.title("Distances From Mean", fontsize=24)
plt.xlabel("Number", fontsize=14)
plt.ylabel("Distance", fontsize=14)

# Size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('distance_plot.png', bbox_inches='tight')
