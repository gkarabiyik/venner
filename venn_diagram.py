from matplotlib_venn import venn2
import matplotlib.pyplot as plt
import os

def create_venn_diagram(genes1, genes2):
    set1 = set(genes1)
    set2 = set(genes2)

    plt.figure(figsize=(8, 8))
    venn2([set1, set2], ('Set 1', 'Set 2'))

    venn_path = 'static/venn_diagram.png'
    plt.savefig(venn_path)
    plt.close()
    return venn_path
