import matplotlib.pyplot as plt

from walker import Walker

# Loop until the user quits
while True:
    # Plot the points to a random walk
    wk = Walker(50000)
    wk.do_walk()

    # Set the plotting window size
    plt.figure(figsize=(10, 6))

    points = list(range(wk.num_points))
    plt.scatter(wk.x_values, wk.y_values, c=points, cmap=plt.cm.Blues, edgecolor='none', s=1)

    # Emphasize the initial and ending positions
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(wk.x_values[-1], wk.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    more_walking = input("Do another walk?(y/n)\n~>")
    if more_walking == 'n':
        break
