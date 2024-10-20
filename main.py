import matplotlib.pyplot as plt
from randomwalk import RandomWalk



while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9),dpi=50)
    ax.scatter(rw.x_values, rw.y_values, c=rw.x_values, cmap=plt.cm.Blues,
               edgecolors='none', s=15)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100)
    ax.set_title('First Data', fontsize=14)
    ax.set_xlabel("X Value", fontsize=14)
    ax.set_ylabel("Y Value", fontsize=14)
    ax.tick_params(labelsize=14)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
