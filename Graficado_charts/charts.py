import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 500, 300]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie31.png')
    plt.close()