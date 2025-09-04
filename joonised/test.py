import matplotlib.pyplot as plt
import numpy as np

# Set up colors
main_red = (215/255, 27/255, 47/255)
second_yellow = (232/255, 201/255, 43/255)

# Generate data
N = 50
t = np.linspace(0, 1, N)

# Create two noisy signals
np.random.seed(0)
signal_red = 0.5 * np.random.randn(N)
np.random.seed(1)
signal_yellow = 0.5 * np.random.randn(N)

# Delay/offset parameters
time_shift = 0.2
vertical_shift = -3

# Create shifted versions
t_shifted = t + time_shift
t_shifted_back = t - time_shift
signal_red_shifted = signal_red + vertical_shift
signal_yellow_shifted = signal_yellow + vertical_shift

# Prepare output directory
output_paths = []

# 1) Just red
plt.figure(figsize=(2.5, 2))
plt.plot(t, signal_red, color=main_red, linewidth=1)
plt.axis('off')
plt.tight_layout(pad=0)
path1 = "plot_1_red_only.svg"
plt.savefig(path1, dpi=300, transparent=True)
plt.close()

# 2) Just yellow
plt.figure(figsize=(2.5, 2))
plt.plot(t, signal_yellow, color=second_yellow, linewidth=1)
plt.axis('off')
plt.tight_layout(pad=0)
path2 = "plot_2_yellow_only.svg"
plt.savefig(path2, dpi=300, transparent=True)
plt.close()

# 3) Red + delayed, Yellow regular
plt.figure(figsize=(3, 2.5))
plt.plot(t_shifted, signal_red_shifted, color=main_red, linewidth=1)
plt.plot(t, signal_yellow, color=second_yellow, linewidth=1)
plt.axvline(0.2, color='black', linestyle='--', linewidth=0.7)
plt.axis('off')
plt.tight_layout(pad=0)
path3 = "plot_3_red_delayed.svg"
plt.savefig(path3, dpi=300, transparent=True)
plt.close()

# 4) Yellow + delayed, Red regular
plt.figure(figsize=(3, 2.5))
plt.plot(t, signal_red, color=main_red, linewidth=1)
plt.plot(t_shifted, signal_yellow_shifted, color=second_yellow, linewidth=1)
plt.axvline(0.2, color='black', linestyle='--', linewidth=0.7)
plt.axis('off')
plt.tight_layout(pad=0)
path4 = "plot_4_yellow_delayed.svg"
plt.savefig(path4, dpi=300, transparent=True)
plt.close()

# 5) Add the two delayed plots (pointwise addition)
# Interpolate onto a common timeline
t_combined = np.linspace(0, 1 + time_shift, 500)
from scipy.interpolate import interp1d

interp_red = interp1d(t_shifted, signal_red_shifted, bounds_error=False, fill_value=0)
interp_yellow = interp1d(t_shifted, signal_yellow_shifted, bounds_error=False, fill_value=0)

combined_signal = interp_red(t_combined) + interp_yellow(t_combined)

# Plot sum
plt.figure(figsize=(3.5, 3))
plt.plot(t_combined, combined_signal, color='black', linewidth=1)
plt.axvline(0.2, color='black', linestyle='--', linewidth=0.7)
plt.axis('off')
plt.tight_layout(pad=0)
path5 = "plot_5_sum.svg"
plt.savefig(path5, dpi=300, transparent=True)
plt.close()
