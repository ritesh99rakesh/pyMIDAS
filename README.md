# MIDAS implementation in Python

Python implementation of [C++](https://github.com/bhatiasiddharth/MIDAS) code by [Siddharth Bhatia](https://github.com/bhatiasiddharth)

## Installation

You can install and use the package by cloning this repository in your project folder:

```
git clone https://github.com/ritesh99rakesh/pyMIDAS.git
```

## Table of Contents

  - [Features](#features)
  - [Use Cases](#use-cases)
  - [Installation](#getting-started)
  - [Demo](#demo)
  - [Datasets](#datasets)
  - [MIDAS in other Languages](#midas-in-other-languages)
  - [Online Articles](#online-articles)
  - [Citation](#citation)

## Features

  - Finds Anomalies in Dynamic/Time-Evolving Graphs
  - Detects Microcluster Anomalies (suddenly arriving groups of
    suspiciously similar edges e.g. DoS attack)
  - Theoretical Guarantees on False Positive Probability
  - Constant Memory (independent of graph size)
  - Constant Update Time (real-time anomaly detection to minimize harm)
  - Up to 48% more accurate and 644 times faster than the state of the
    art approaches

For more details, please read the paper - [MIDAS: Microcluster-Based
Detector of Anomalies in Edge
Streams](https://www.comp.nus.edu.sg/~sbhatia/assets/pdf/midas.pdf).
*Siddharth Bhatia, Bryan Hooi, Minji Yoon, Kijung Shin, Christos
Faloutsos*. AAAI 2020.

## Use **Cases**

1.  Intrusion Detection
2.  Fake Ratings
3.  Financial Fraud

## Example

Inside the pyMIDAS directory

```python
from midas import midas
import pandas as pd

# Load dataset
data = pd.read_csv("dataset.csv", names=['src', 'dst', 'timestamps'])

# Anomaly Scores
anomaly_scores = midas(
    data.src, data.dst, data.timestamps,
    num_rows=2,
    num_buckets=769
)
```

For more examples, refer to [examples](https://github.com/ritesh99rakesh/pyMIDAS/tree/master/example) folder of this repository.

## Datasets

1.  [DARPA](https://www.ll.mit.edu/r-d/datasets/1998-darpa-intrusion-detection-evaluation-dataset):
    [Original
    Format](https://www.comp.nus.edu.sg/~sbhatia/assets/datasets/darpa_original.csv),
    [MIDAS
    format](https://www.comp.nus.edu.sg/~sbhatia/assets/datasets/darpa_midas.csv)
2.  [TwitterWorldCup2014](http://odds.cs.stonybrook.edu/twitterworldcup2014-dataset)
3.  [TwitterSecurity](http://odds.cs.stonybrook.edu/twittersecurity-dataset)

## MIDAS in other Languages

1.  [C++](https://github.com/bhatiasiddharth/MIDAS) by [Siddharth
    Bhatia](https://github.com/bhatiasiddharth)
2.  [Rust](https://github.com/scooter-dangle/midas_rs)
    by [Scott Steele](https://github.com/scooter-dangle)
3.  [Ruby](https://github.com/ankane/midas) by [Andrew
    Kane](https://github.com/ankane)

## Online Articles

1.  KDnuggets: [Introducing MIDAS: A New Baseline for Anomaly Detection
    in
    Graphs](https://www.kdnuggets.com/2020/04/midas-new-baseline-anomaly-detection-graphs.html)
2.  Towards Data Science: [Controlling Fake News using Graphs and
    Statistics](https://towardsdatascience.com/controlling-fake-news-using-graphs-and-statistics-31ed116a986f)
3.  Towards Data Science: [Anomaly detection in dynamic graphs using
    MIDAS](https://towardsdatascience.com/anomaly-detection-in-dynamic-graphs-using-midas-e4f8d0b1db45)
4.  Towards AI: [Anomaly Detection with
    MIDAS](https://medium.com/towards-artificial-intelligence/anomaly-detection-with-midas-2735a2e6dce8)

## Citation

If you use this code for your research, please consider citing our
paper.

``` markup
@article{bhatia2019midas,
  title={MIDAS: Microcluster-Based Detector of Anomalies in Edge Streams},
  author={Bhatia, Siddharth and Hooi, Bryan and Yoon, Minji and Shin, Kijung and Faloutsos, Christos},
  journal={arXiv preprint arXiv:1911.04464},
  year={2019}
}
```
