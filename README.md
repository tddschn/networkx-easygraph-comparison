# A Rough Comparison of the two Python Graph Libraries NetworkX and EasyGraph

**A work in progress**

[NetworkX](https://networkx.org)

[EasyGraph](https://github.com/easy-graph/Easy-Graph)

EasyGraph mentioned in this article refers to v0.2a38, unless specified otherwise.

- [A Rough Comparison of the two Python Graph Libraries NetworkX and EasyGraph](#a-rough-comparison-of-the-two-python-graph-libraries-networkx-and-easygraph)
  - [Overview](#overview)
  - [Dependencies](#dependencies)
  - [Graph I/O](#graph-io)

## Overview

![](./images/networkx-overview.png)

![](./images/Easy-Graph-overview.png)

## Dependencies

NetworkX, surprisingly, has no dependencies, only some optional dependencies, specified in its `requirements` directory.

Example: the `[default]` optional dependency group includes libraries like `matplotlib` for drawing.

The core functionalities of NetworkX (graph representation, graph algorithms) does not depend on any other libraries.

<!-- cSpell:disable -->
EasyGraph, on the other hand, specified a bunch of utility dependencies (`joblib`, `progressbar`, `tqdm`) heavy dependencies (`numpy`, `pandas`, `matplotlib`, `scikit-learn`, `tensorflow`) as required.

Its core classes don't require these dependencies.

`numpy` is heavily used in many of EasyGraph's code base, for various purposes:
- Graph representation (`graphml.py`, `ucinet.py`, `gexf.py`)
- Utility code (`alias.py`, `to_numpy_matrix`, `to_numpy_array`)
- Almost all files that implement some SHS detection algorithms (`maxBlock.py` and many others)

ML libs `sklearn` and `tensorflow` are used only for implementing SHS detection algorithms.

The utility functions aren't really necessary and could be moved to optional deps.


<!-- cSpell:enable -->

## Graph I/O

![](images/networkx-readwrite.png)

![](images/eg-readwrite.png)
