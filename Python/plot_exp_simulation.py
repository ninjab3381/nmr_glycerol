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
    plt.plot(ppm_list, rel_intensity_list, color=color, linestyle=linestyle, label=label)


if __name__ == "__main__":
    freq = input("Enter Freq: ")
    sigma = input("Enter Sigma in percent: ")
    ppm_list1, rel_intensity_list1 = read_file("../DIGITIZED_SPECTRA/jump_freq_800/DATA/dig_spectra_800.csv")
    plot_line(ppm_list1, rel_intensity_list1, "green", "dashed", "Experiment")
    ppm_list2, rel_intensity_list2 = read_file("../GAUSS_SKEWED/jump_freq_800/Simulation_Spectra_Avg/800Hz_simulation_15sigma_lognormal_skewed1_for_plotting.csv")
    plot_line(ppm_list2, rel_intensity_list2, "red", "dotted", "Avg. Simulation")
    plt.xlabel('ppm')
    plt.ylabel('relative intensity')
    plt.suptitle('Experiment vs. Weighted Avg. Simulation Results')
    plt.title('Freq = ' + freq + 'Hz & Sigma = ' + sigma + '%')
    plt.xlim(-50, -120)
    plt.legend(loc='upper right')
    plt.show()
