import numpy as np

def print_dirichlet(x):
    obj = x
    if obj["error"] == 1:
        print(
            f"ERROR! nstar is too small! (nstar={obj['nstar']}), Sum of Pn is (should be 1) {sum([obj['Pn'](n) for n in range(obj['nstar'] + 1)])}"
        )

    print(f"Number of Brands in the Category = {obj['nbrand']}")
    print(f"Brand List : {', '.join(obj['brand_name'])}")
    print(
        f"\nBrands' Market Shares: {', '.join(map(str, np.round(obj['brand_share'], 3)))}"
    )
    print(
        f"Brands' Penetration: {', '.join(map(str, np.round(obj['brand_pen_obs'], 3)))}"
    )

    obj["period_print"]()

    print(
        f"\nCategory Penetration = {round(obj['cat_pen'], 2)}, with Buying Rate = {round(obj['cat_buyrate'], 2)}"
    )
    print("Estimated Dirichlet Model Parameters:")
    print(
        f"NBD: M = {round(obj['M'], 2)}, K = {round(obj['K'], 2)}; Dirichlet: S = {round(obj['S'], 2)}\n"
    )