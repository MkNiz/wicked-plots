import matplotlib.pyplot as plt

from walker import Walker

# Loop until the user quits
while True:
    # Plot the points to a random walk
    wk = Walker()
    wk.do_walk()

    plt.scatter(wk.x_values, wk.y_values, s=15)
    plt.show()

    more_walking = input("Do another walk?(y/n)\n~>")
    if more_walking == 'n':
        break
