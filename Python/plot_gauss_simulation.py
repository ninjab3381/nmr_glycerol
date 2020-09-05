import matplotlib.pyplot as plt


def read_file(filename):
    ppm_list = []
    rel_intensity_list = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split(",")
            ppm = float(str(fields[0]).strip())
            rel_intensity = float(str(fields[1]).strip())
            ppm_list.append(ppm)
            rel_intensity_list.append(rel_intensity)
    f.close()
    return ppm_list, rel_intensity_list


def plot_line(ppm_list, rel_intensity_list, color, linestyle, label):
    ax.plot(ppm_list, rel_intensity_list, color=color, linestyle=linestyle, label=label)


if __name__ == "__main__":
    freq = input("Enter Jump Frequency: ")
    sigma = input("Enter Sigma in percent: ")
    ppm_list2, rel_intensity_list2 = read_file("../GAUSS_SKEWED/jump_freq_1200/Simulation_Spectra_Avg/1200Hz_simulation_15sigma_lognormal_skewed2_for_plotting.csv")
    fig, ax = plt.subplots()
    plot_line(ppm_list2, rel_intensity_list2, "red", "dotted", "Avg. Simulation")
    ax.set_xlabel('ppm')
    ax.set_ylabel('relative intensity')
    plt.suptitle('Weighted Avg. Simulation Results')
    ax.set_title('Jump Freq = ' + freq + ' & Sigma = ' + sigma + '%')
    ax.set_xlim(-120, -50)
    ax.invert_xaxis()
    plt.legend(loc='upper right')
    plt.show()
