from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


INPUT_FILE = Path(
    "CIL28778_separation_timeseries_frames39-57.csv"
)
PROCESSED_FILE = Path(
    "CIL28778_processed_timeseries.csv"
)
FIGURE_FILE = Path(
    "CIL28778_signal_separation_python.png"
)

DISPLAYED_FPS = 6.0


# Load the raw Fiji/ImageJ Results table
raw_data = pd.read_csv(INPUT_FILE)

# Retain the frame number and measured line length
data = raw_data[["Slice", "Length"]].copy()
data.columns = ["Frame", "Separation (pixels)"]

# Frame 1 corresponds to video time 0 seconds
data["Video time (s)"] = (
    data["Frame"] - 1
) / DISPLAYED_FPS

data = data[
    ["Frame", "Video time (s)", "Separation (pixels)"]
]

# Calculate summary measurements
initial = data["Separation (pixels)"].iloc[0]
final = data["Separation (pixels)"].iloc[-1]
duration = (
    data["Video time (s)"].iloc[-1]
    - data["Video time (s)"].iloc[0]
)

absolute_increase = final - initial
fold_increase = final / initial
percentage_increase = (
    absolute_increase / initial
) * 100
average_rate = absolute_increase / duration

# Save the cleaned time-series data
data.to_csv(PROCESSED_FILE, index=False)

# Display calculated results
print(f"Initial separation: {initial:.3f} pixels")
print(f"Final separation: {final:.3f} pixels")
print(f"Absolute increase: {absolute_increase:.3f} pixels")
print(f"Fold increase: {fold_increase:.3f}×")
print(f"Percentage increase: {percentage_increase:.1f}%")
print(f"Average apparent rate: {average_rate:.3f} pixels/s")

# Create the separation graph
fig, ax = plt.subplots(figsize=(9, 4.5))

ax.plot(
    data["Video time (s)"],
    data["Separation (pixels)"],
    color="black",
    marker="o",
    linewidth=1.8,
    markersize=5,
)

ax.set_title(
    "GFP-KNL-2 Signal Separation During First Mitosis",
    fontweight="bold",
)
ax.set_xlabel("Video time (s)")
ax.set_ylabel("Centre-to-centre separation (pixels)")
ax.set_ylim(0, 45)
ax.grid(True, color="lightgray", linewidth=0.7)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.tight_layout()
fig.savefig(FIGURE_FILE, dpi=300)
plt.close(fig)

print(f"\nProcessed data saved as: {PROCESSED_FILE}")
print(f"Graph saved as: {FIGURE_FILE}")
