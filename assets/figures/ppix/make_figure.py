import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.constants import physical_constants


def get_reference_data():
    filename = "ProtoporphyrinUVVis.txt"
    df = pd.read_csv(filename, sep="\t")
    df.fillna(0, inplace=True)
    df.columns = ["M cm^-1", "M Abs", "D cm^-1", "D Abs"]
    return df


if __name__ == "__main__":
    import subprocess
    from scipy.constants import physical_constants

    #
    # Get Data
    #
    df_ref = get_reference_data()
    df_cas = pd.read_csv("sa-3-mcscf.csv")
    df_pt2 = pd.read_csv("sa-3-mcscf_nevpt2.csv")

    ev_2_cm_1 = physical_constants["electron volt-inverse meter relationship"][0] * 1e-2
    mono_cm_1 = np.array([2.0982, 2.2845]) * ev_2_cm_1
    di_cm_1 = np.array([2.0646, 2.2353]) * ev_2_cm_1

    #
    # Plotting
    #
    plt.figure()
    sns.set_style("darkgrid")
    sns.set_palette("muted")
    bar_height = 0.002

    # Monoanion
    plt.subplot(2, 1, 1)
    plt.title("Monoanion Absorption")
    s_i = np.argsort(df_ref["M cm^-1"])
    plt.plot(df_ref["M cm^-1"][s_i], df_ref["M Abs"][s_i], c="k", label="Expt.")
    # plt.bar(mono_cm_1, [bar_height] * 2, label="TDDFT", width=120)
    plt.bar(
        df_cas.iloc[0, 1:3].values, [bar_height] * 2, label="CASSCF", width=120,
    )

    ax1 = plt.gca()
    plt.xlim((14000, 29000))
    plt.ylabel("Abs. (arb.)")
    plt.legend(loc="upper right")

    # Dianion
    plt.subplot(2, 1, 2)
    plt.title("Dianion Absorption")
    plt.plot(df_ref["D cm^-1"], df_ref["D Abs"], c="k", label="Expt.")
    # plt.bar(di_cm_1, [bar_height] * 2, label="TDDFT", width=120)

    plt.bar(
        df_cas.iloc[1, 1:3].values, [bar_height] * 2, label="CASSCF", width=120,
    )
    ax2 = plt.gca()
    plt.xlim((14000, 29000))
    plt.ylabel("Abs. (arb.)")
    plt.xlabel("Energy cm$^{-1}$")

    plt.tight_layout()
    plt.savefig("ppix_spectrum_1.png", dpi=900)

    # Second plot
    ax1.bar(
        df_pt2.iloc[1, 1:3].values, [bar_height] * 2, label="NEVPT2", width=120,
    )
    ax2.bar(
        df_pt2.iloc[5, 1:3].values, [bar_height] * 2, label="NEVPT2", width=120,
    )
    ax1.legend(loc="upper right")
    plt.savefig("ppix_spectrum_2.png", dpi=900)

    # Third plot
    fs = 15  # fontsize
    bbox = dict(boxstyle="round", ec="k", fc="none")
    ax1.text(15800, 0.0015, "S$_1$", fontsize=fs, bbox=bbox)
    ax1.text(18700, 0.0015, "S$_2$", fontsize=fs, bbox=bbox)

    ax2.text(15700, 0.0016, "S$_1$", fontsize=fs, bbox=bbox)
    ax2.text(18300, 0.0016, "S$_2$", fontsize=fs, bbox=bbox)

    ax1.set_xlim((14000, 21000))
    ax2.set_xlim((14000, 21000))
    ax1.set_xticks(np.arange(14, 21) * 1000)
    ax2.set_xticks(np.arange(14, 21) * 1000)
    plt.savefig("ppix_spectrum_3.png", dpi=900)
