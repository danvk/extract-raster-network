# Extract Raster Network

Extract a network graph (nodes and edges) from a raster image.
See this [Stack Overflow question][1] for details.

## Quickstart

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ./extract_network.py samples/grid1.png '(0, 0, 255)'

## What this does

This takes a raster (PNG) image containing some kind of network (e.g. a street grid):

![Raster containing street grid](samples/00025.png)

and finds the nodes (e.g. intersections) and edges between them (e.g. streets):

![Image showing extracted street grid](samples/00025.grid.png)

Here the large circle are extracted nodes and the lines and small circles indicate the
extracted polylines for the edges between them.

## Algorithm

The general approach is:

1. Binarize the image by finding pixels matching a specific color.
2. [Skeletonize][skel] the image to make the "streets" 1px wide.
3. Find candidate nodes (see below).
4. Repeat until no two nodes are too close together:
   1. Use breadth-first search (flood fill) to connect nodes.
   2. If two connected nodes are within D of each other, merge them.
5. Run shapely's [`simplify`][simplify] on the paths between nodes to get polylines.

"Find candidate nodes" and "Use breadth-first search" are the interesting bits.
This code largely follows the approach from [NEFI][] with a few modifications:

- This uses the "Zhang-Suen" nodes (those with exactly 1 or 3+ neighbors) as a
  starting point (same as NEFI). This depends heavily on the skeleton being _exactly_
  1px wide, which is not always the case for complex intersections. To address this
  situation, we add candidate nodes at locally dense (2x2 or larger) locations in the
  skeleton.

- We do a breadth-first search from the candidate nodes, same as NEFI.
  The departures are that we:
  - Allow self-loops and multiple edges between the same pair of nodes.
    The image below contains examples of both of these.
  - Iteratively merge nodes that are too close to one another.

The final shapely `simplify` step does not change the network topology but is convenient
for visualizing and working with the resulting polyline.

### Visualization of the steps

TODO

## References

- [Stack Overflow question][1]
- [NEFI2][2], a GUI app for Network Extraction. See also [their 2018 paper][3].

[1]: https://stackoverflow.com/questions/69398683/extract-street-network-from-a-raster-image
[2]: https://github.com/05dirnbe/nefi
[3]: https://arxiv.org/pdf/1502.05241.pdf
[skel]: https://scikit-image.org/docs/stable/auto_examples/edges/plot_skeleton.html
[simplify]: https://shapely.readthedocs.io/en/stable/manual.html#object.simplify
[nefi]: https://github.com/05dirnbe/nefi/blob/260b2717ebc5fb94b2a241c5b73540b41f3dc6bf/nefi2/model/algorithms/guo_hall.py#L63
