# First M87 EHT Results: Calibrated Data

**Authors:** The Event Horizon Telescope Collaboration et al.

**Date:** April 10, 2019

**Primary Reference:** [The Event Horizon Telescope Collaboration, et al. 2019c, ApJL, 875, L3 (M87 Paper III)](https://doi.org/10.3847/2041-8213/ab0c57)

**Data Product Code:** [2019-D01-01](https://eventhorizontelescope.org/for-astronomers/data)

**Brief Description:**

We release a data set to accompany the *First M87 Event Horizon Telescope
Results* paper series (EHT Collaboration et al. 2019a,b,c,d,e,f). The data set
is derived from the Science Release 1 (SR1) of the Event Horizon Telescope
(EHT)'s April 2017 observation campaign (EHT Collaboration et al. 2019c). It is
made public simultaneously with three imaging pipelines.

This data set contains M87 data for both low and high bands for all observed
days (April 5th, 6th, 10th, 11th, 2017). Data from the 2017 observations were
processed through three independent reduction pipelines (Blackburn et al. 2019,
Janssen et al. 2019, Paper III). This release includes the fringe fitted,
a-priori calibrated, and network calibrated data from the EHT-HOPS pipeline,
which is the primary data set for the First M87 EHT results. Independent flux
calibration is performed based on estimated station sensitvities during the
campaign (Issaoun et al.  2017, Janssen et al. 2019). A description of the data
properties, their validation, and estimated systematic errors is given in Paper
III with additional details in Wielgus et al. (2019).

The data are time averaged to 10 seconds and frequency averaged over all 32
intermediate frequencies (IFs). All polarization information is explicitly
removed. To make the resulting `uvfits` files compatible with popular
very-long-baseline interferometry (VLBI) software packages, the circularly
polarized cross-hand visibilities `RL` and `LR` are set to zero along with
their errors, while parallel-hands `RR` and `LL` are both set to an estimated
Stokes *I* value. Measurement errors for `RR` and `LL` are each set to sqrt(2)
times the statistical errors for Stokes *I*.

All `uvfits` files are located in the "`uvfits/`" subdirectory. Easy-to-read
`csv` and `txt` files are derived from the `uvfits` files and provided in
"`csv/`" and "`txt/`", respectively. Scripts that generate these files from the
original SR1 data are also included. Finally, the `run.sh` script in the top
directory will convert `uvfits` files into `csv` and `txt` files.

The three `tgz` files are gzipped tarballs that contains `uvfits`, `txt`, and
`csv` files, respectively. They are included in this repository for convenience.

**File Name Convention:**

The data files are named in the following convention:

    [Data-Release-Tag]_[Source]_[year]_[day-of-year]_[band]_[pipeline]_[stage]_StokesI.[format]

**Station Code Table:**

| UVFITS Code | Station Name                  | Location |
| ----------- | ----------------------------- | -------- |
| AA          | ALMA                          | Chile    |
| AP          | APEX                          | Chile    |
| AZ          | Submillimeter Telescope       | Arizona  |
| JC          | James Clerk Maxwell Telescope | Hawai'i  |
| LM          | Large Millimeter Telescope    | Mexico   |
| PV          | IRAM                          | Spain    |
| SM          | Submillimeter Array           | Hawai'i  |

**References:**

- [EHT Collaboration Data Portal Website](https://eventhorizontelescope.org/for-astronomers/data)
- [The Event Horizon Telescope Collaboration, et al. 2019a, ApJL, 875, L1 (M87 Paper I)](https://doi.org/10.3847/2041-8213/ab0ec7)
- [The Event Horizon Telescope Collaboration, et al. 2019b, ApJL, 875, L2 (M87 Paper II)](https://doi.org/10.3847/2041-8213/ab0c96)
- [The Event Horizon Telescope Collaboration, et al. 2019c, ApJL, 875, L3 (M87 Paper III)](https://doi.org/10.3847/2041-8213/ab0c57)
- [The Event Horizon Telescope Collaboration, et al. 2019d, ApJL, 875, L4 (M87 Paper IV)](https://doi.org/10.3847/2041-8213/ab0e85)
- [The Event Horizon Telescope Collaboration, et al. 2019e, ApJL, 875, L5 (M87 Paper V)](https://doi.org/10.3847/2041-8213/ab0f43)
- [The Event Horizon Telescope Collaboration, et al. 2019f, ApJL, 875, L6 (M87 Paper VI)](https://doi.org/10.3847/2041-8213/ab1141)
- [Blackburn, L., Chan, C.-k., Crew, G., et al. 2019, arXiv:1903.08832](https://ui.adsabs.harvard.edu/abs/2019arXiv190308832B/abstract)
- [Janssen, M., Goddi, C., van Bemmel, I., et al. 2019, arXiv:1902.01749](https://ui.adsabs.harvard.edu/abs/2019arXiv190201749J/abstract)
- [Issaoun, S., Folkers, T., Blackburn, L., et al. 2017, EHT Memo 2017-CE-02](https://eventhorizontelescope.org/for-astronomers/memos)
- [Janssen, M., Blackburn, L., Issaoun, S., et al. 2019, EHT Memo 2019-CE-01](https://eventhorizontelescope.org/for-astronomers/memos)
- [Wielgus, M., Blackburn, L., Issaoun, S., et al. 2019, EHT Memo 2019-CE-02](https://eventhorizontelescope.org/for-astronomers/memos)
