import numpy as np
import pandas as pd


def summary_dirichlet(
    obj,
    t=1,
    type=("buy", "freq", "heavy", "dup"),
    digits=2,
    freq_cutoff=5,
    heavy_limit=range(1, 7),
    dup_brand=1,
):
    obj["period_set"](t)  # change the time period

    result = {}

    for tt in type:
        if tt == "buy":
            pen_brand = [
                round(obj["brand_pen"](j), digits) for j in range(1, obj["nbrand"] + 1)
            ]
            pur_brand = [
                round(obj["brand_buyrate"](j), digits)
                for j in range(1, obj["nbrand"] + 1)
            ]
            pur_cat = [round(obj["wp"](j), digits) for j in range(1, obj["nbrand"] + 1)]
            r = pd.DataFrame(
                {"pen.brand": pen_brand, "pur.brand": pur_brand, "pur.cat": pur_cat},
                index=obj["brand_name"],
            )
            result[tt] = r.round(digits)

        elif tt == "freq":

            def prob_r(r, j):
                return sum(
                    [
                        obj["Pn"](n) * obj["p_rj_n"](r, n, j)
                        for n in range(r, obj["nstar"] + 1)
                    ]
                )

            r = np.zeros((obj["nbrand"], freq_cutoff + 2))
            for j in range(1, obj["nbrand"] + 1):
                r[j - 1, :] = [prob_r(i, j) for i in range(freq_cutoff + 1)] + [
                    sum(
                        [prob_r(i, j) for i in range(freq_cutoff + 1, obj["nstar"] + 1)]
                    )
                ]

            index = obj["brand_name"]
            columns = list(range(freq_cutoff + 1)) + [f"{freq_cutoff + 1}+"]
            result[tt] = pd.DataFrame(r, index=index, columns=columns).round(digits)

        elif tt == "heavy":
            r = np.zeros((obj["nbrand"], 2))
            Pn_sum = sum(
                [obj["Pn"](n) for n in heavy_limit]
            )  # Prob of Category Purchase Freq in Set "limit"
            for j in range(1, obj["nbrand"] + 1):
                if obj["check"]:
                    print("compute penetration")
                p0 = 1 - obj["brand_pen"](j, limit=heavy_limit)
                r[j - 1, 0] = 1 - p0 / Pn_sum

                if obj["check"]:
                    print("compute purchase rate")
                r[j - 1, 1] = (
                    obj["brand_buyrate"](j, heavy_limit)
                    * obj["brand_pen"](j)
                    / (Pn_sum - p0)
                )

            result[tt] = pd.DataFrame(
                r, index=obj["brand_name"], columns=["Penetration", "Avg Purchase Freq"]
            ).round(digits)

        elif tt == "dup":
            k = dup_brand
            r = np.zeros(obj["nbrand"])  # store result for Brand Duplication
            r[k - 1] = 1  # Brand Duplication with Itself is 100%

            b_k = obj["brand_pen"](k)  # penetration for Brand k (dup.brand)
            others = [
                j for j in range(1, obj["nbrand"] + 1) if j != k
            ]  # list of Other Brands that the Focal Brand Buyer may buy

            for j in others:
                p0 = sum(
                    [
                        obj["Pn"](i) * obj["p_rj_n"](0, i, [k, j])
                        for i in range(obj["nstar"] + 1)
                    ]
                )
                b_j_k = 1 - p0  # Composite Brand [k,j]  Penetration
                b_j = obj["brand_pen"](j)
                b_jk = b_j + b_k - b_j_k  # proportion buying BOTH brand j and k.
                b_j_given_k = b_jk / b_k
                r[j - 1] = b_j_given_k

            result[tt] = pd.Series(r, index=obj["brand_name"]).round(digits)

    return result