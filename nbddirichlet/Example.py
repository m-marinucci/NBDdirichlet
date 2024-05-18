from nbddirichlet import dirichlet
from nbddirichlet import print_dirichlet
from nbddirichlet import summary_dirichlet
from nbddirichlet import plot_dirichlet

cat_pen = 0.56  # Category Penetration
cat_buyrate = 2.6  # Category Buyer's Average Purchase Rate in a given period
brand_share = [0.25, 0.19, 0.1, 0.1, 0.09, 0.08, 0.03, 0.02]  # Brands' Market Share
brand_pen_obs = [0.2, 0.17, 0.09, 0.08, 0.08, 0.07, 0.03, 0.02]  # Brand Penetration
brand_name = ["Colgate DC", "Macleans", "Close Up", "Signal", "ultrabrite",
            "Gibbs SR", "Boots Priv. Label", "Sainsbury Priv. Lab."]


# Estimate the NBD-Dirichlet model parameters
dpar = dirichlet(cat_pen, cat_buyrate, brand_share, brand_pen_obs)
for key, value in dpar.items():
    print(f"{key}: {value}")


# clear the print_dirichlet function

# Generate summary statistics
summary = summary_dirichlet(dpar, t=1, type=['buy', 'freq', 'heavy', 'dup'])

print(summary)


