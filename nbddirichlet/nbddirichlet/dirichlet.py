import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import beta, comb

def dirichlet(
    cat_pen,
    cat_buyrate,
    brand_share,
    brand_pen_obs,
    brand_name=None,
    cat_pur_var=None,
    nstar=50,
    max_S=30,
    max_K=30,
    check=False,
):
    nbrand = len(brand_pen_obs)
    if brand_name is None:
        brand_name = ["B" + str(i) for i in range(1, nbrand + 1)]

    M0 = M = cat_pen * cat_buyrate

    def eq1(K):
        cp = np.log(1 - cat_pen)
        return (K * np.log(1 + M / K) + cp) ** 2

    if cat_pur_var is None:
        result = minimize_scalar(eq1, bounds=(0.0001, max_K), method="bounded")
        K = result.x
    else:
        K = M**2 / (cat_pur_var - M)

    def pzeron(n, j, S):
        alphaj = S * brand_share[j]
        if n == 0:
            r = 1
        else:
            a = np.arange(n)
            num = np.log(S - alphaj + a)
            den = np.log(S + a)
            r = np.exp(np.sum(num - den))
        return r

    def p_rj_n(rj, n, j):
        if isinstance(j, (int, np.integer)):
            alphaj = S * brand_share[j - 1]
        elif isinstance(j, float):
            alphaj = S * brand_share[int(j) - 1]
        else:
            alphaj = 0
            for j_val in j:
                alphaj += S * brand_share[j_val - 1]
        return alphaj  # Added return statement

    def Pn(n):
        if n == 0:
            g = 0
        else:
            a = np.arange(n)
            num = np.log(K + a)
            den = np.log(1 + a)
            g = np.sum(num - den)
        return np.exp((-K) * np.log(1 + M / K) + g + n * np.log(M / (M + K)))

    def brand_pen(j, limit=np.arange(nstar + 1)):
        if check:
            print("In brand_pen, nstar =", limit[-1])
        p0 = sum([Pn(i) * p_rj_n(0, i, j) for i in limit])
        return 1 - p0

    def brand_buyrate(j, limit=np.arange(1, nstar + 1)):
        def buyrate_n(n, j):
            rate = np.arange(1, n + 1)
            return sum([r * p_rj_n(r, n, j) for r in rate])

        if check:
            print("In brand_buyrate, nstar =", limit[-1])
        return sum([Pn(n) * buyrate_n(n, j) for n in limit]) / brand_pen(j)

    def wp(j, limit=np.arange(1, nstar + 1)):
        return sum([n * Pn(n) * (1 - p_rj_n(0, n, j)) for n in limit]) / brand_pen(j)

    def eq2(S, j):
        t_pen = 1 - sum([Pn(i) * pzeron(i, j, S) for i in range(nstar + 1)])
        o_pen = brand_pen_obs[j]
        return (t_pen - o_pen) ** 2

    def Sj(j):
        result = minimize_scalar(eq2, bounds=(0, max_S), args=(j,), method="bounded")
        if check:
            print(
                "Objective Value is", result.fun, "at S =", result.x, ", and Brand =", j
            )
        return result.x

    if check:
        print("Finding Optimum S for Each Brand ...")
    Sall = np.array([Sj(j) for j in range(nbrand)])
    bp = np.percentile(Sall, [25, 50, 75])
    outlier = Sall[(Sall < bp[0]) | (Sall > bp[2])]
    outlier2 = Sall[Sall > bp[2]]
    outliers = np.concatenate((outlier, outlier2))
    schoose = np.array([x not in outliers for x in Sall])

    if check and len(outliers) > 0:
        print(
            "Removing These Outliers of S:",
            outliers,
            ", for brands:",
            np.where(~schoose)[0] + 1,
        )

    S = np.average(Sall[schoose], weights=np.array(brand_share)[schoose])

    if (
        sum([Pn(n) for n in range(nstar + 1)]) < 0.99
        or abs(sum([n * Pn(n) for n in range(nstar + 1)]) - M0) > 0.1
    ):
        print("nstar is too small! (nstar =", nstar, ")")
        error = 1
    else:
        error = 0

    if error != 0:
        # Handle the error case
        print("Error occurred during the computation. Please check the input parameters and nstar value.")
        return None

    def period_set(t):
        global M  # Use global to modify the global variable 'M'
        M = M0 * t

    def period_print():
        print("Multiple of Base Time Period:", round(M / M0, 2), ", Current M =", M)

    dpar = {
        "S": S,
        "M": M,
        "K": K,
        "nbrand": nbrand,
        "nstar": nstar,
        "cat_pen": cat_pen,
        "cat_buyrate": cat_buyrate,
        "brand_share": brand_share,
        "brand_pen_obs": brand_pen_obs,
        "brand_name": brand_name,
        "period_set": period_set,
        "period_print": period_print,
        "p_rj_n": p_rj_n,
        "Pn": Pn,
        "brand_pen": brand_pen,
        "brand_buyrate": brand_buyrate,
        "wp": wp,
        "check": check,
        "error": error,
    }

    return dpar