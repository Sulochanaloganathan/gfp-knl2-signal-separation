# gfp-knl2-signal-separation
Quantitative Fiji/ImageJ analysis of GFP-KNL-2 centromeric signal separation during first mitosis in a C. elegans embryo.
# GFP-KNL-2 Centromeric Signal Separation

## Overview

This repository presents a secondary quantitative analysis of GFP-KNL-2 centromeric signal dynamics during the first mitotic division of a *Caenorhabditis elegans* embryo. Manual centre-to-centre measurements were performed using Fiji/ImageJ.

## Objective

To quantify the change in distance between two GFP-KNL-2 centromeric signals during first mitosis.

## Dataset

- **Organism:** *Caenorhabditis elegans*
- **Fluorescent marker:** GFP-KNL-2
- **Biological process:** First mitotic division
- **Frames analysed:** 39–57
- **Displayed video time:** 6.333–9.333 seconds
- **Data source:** [Cell Image Library CIL:28778](https://www.cellimagelibrary.org/images/28778)

## Analysis workflow

1. The fluorescence region was isolated from the side-by-side fluorescence/DIC movie.
2. Identical display settings of 0–255 were maintained across all frames.
3. The straight-line tool in Fiji/ImageJ was used to measure centre-to-centre signal separation.
4. Measurements were recorded for 19 consecutive frames.
5. Data were transferred to Microsoft Excel for calculation and visualization.

## Key results

| Metric | Value |
|---|---:|
| Initial separation | 12.824 pixels |
| Final separation | 40.106 pixels |
| Absolute increase | 27.282 pixels |
| Fold increase | 3.127× |
| Percentage increase | 212.7% |
| Average apparent separation rate | 9.094 pixels/s |

The measurements showed a generally progressive increase in GFP-KNL-2 signal separation, with minor frame-to-frame fluctuations.

## Data

- [Raw Fiji measurements: frames 39–57](CIL28778_separation_timeseries_frames39-57.csv)

## Interpretation

The increasing distance is consistent with separation of GFP-KNL-2-positive centromeric structures during first mitosis. KNL-2 labels centromeric regions; therefore, the results should not be described as measurements of entire chromosome separation.

## Limitations

- Only one embryo was analysed.
- Signal centres were selected manually.
- Spatial-calibration metadata were unavailable, so distances are reported in pixels.
- Video time was derived from the displayed playback rate.
- No biological replicates or inferential statistical tests were included.

## Tools

- Fiji/ImageJ
- Microsoft Excel
- Microsoft PowerPoint
- Microsoft Word
 
## Data attribution

The original microscopy data were obtained from Cell Image Library entry CIL:28778. The original movie is not redistributed in this repository and remains subject to the licence specified by the data provider.

## Author

**Sulochana Loganathan**
