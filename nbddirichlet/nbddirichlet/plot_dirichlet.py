import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_dirichlet(x, t=4, brand=None, incr=1, result=None):
    tseq = np.arange(0, t + incr, incr)
    nt = len(tseq)
    if brand is None:
        brand = np.arange(1, x['nbrand'] + 1)
    nb = len(brand)
    nc = plt.cm.rainbow(np.linspace(0, 1, nb))

    if result is None:
        r_pen = np.zeros((nb, nt))
        r_buy = np.ones((nb, nt))

        def bmat(j):
            ct = tseq[j]
            x['period_set'](ct)
            r_pen[:, j] = np.array([x['brand_pen'](int(b)) for b in brand])
            r_buy[:, j] = np.array([x['brand_buyrate'](int(b)) for b in brand])

        np.array([bmat(j) for j in range(1, nt)])
    else:
        r_pen = result['pen']
        r_buy = result['buy']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot([0] + [t] * nb, [0] + list(r_pen[:, -1]), 'o')
    ax1.set_title(f"Theoretical Penetration Growth\nof Retailer Over {t} Quarters")
    ax1.set_xlabel("Quarters")
    ax1.set_ylabel("Penetration")
    ax1.set_yticks(np.arange(0.1, 1.1, 0.05))
    ax1.grid(True, which='major', axis='y', linestyle='--', alpha=0.7)
    for i in range(nb):
        ax1.plot(tseq, r_pen[i, :], linestyle='-', linewidth=2, color=nc[i])
    ax1.legend(x['brand_name'], loc='upper left')

    ax2.plot(np.tile(tseq, (nb, 1)).T, r_buy.T, 'o')
    ax2.set_title(f"Theoretical Shopping Rate\nGrowth Over {t} Quarters")
    ax2.set_xlabel("Quarters")
    ax2.set_ylabel("Shopping Frequency")
    ax2.set_yticks(np.arange(2, np.max(r_buy) + 0.6, 0.5))
    ax2.grid(True, which='major', axis='y', linestyle='--', alpha=0.7)
    for i in range(nb):
        ax2.plot(tseq, r_buy[i, :], linestyle='-', linewidth=2, color=nc[i])
    ax2.legend(x['brand_name'], loc='upper left')

    plt.tight_layout()
    plt.show()

    r_pen = pd.DataFrame(r_pen, index=x['brand_name'], columns=tseq)
    r_buy = pd.DataFrame(r_buy, index=x['brand_name'], columns=tseq)

    return {'pen': r_pen, 'buy': r_buy}