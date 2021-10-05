# Extract Raster Network

Extract a network graph (nodes and edges) from a raster image.
See this [Stack Overflow question][1] for details.

## Quickstart

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ./extract_network.py samples/grid1.png

## What this does

This takes a raster (PNG) image containing some kind of network (e.g. a street grid):

![Raster containing street grid](samples/00025.png)

and finds the nodes (e.g. intersections) and edges between them (e.g. streets):

![Image showing extracted street grid](samples/00025.grid.png)

Here the large circle are extracted nodes and the lines and small circles indicate the
extracted polylines for the edges between them.

## Algorithm

## References

- [Stack Overflow question][1]
- [NEFI2][2], a GUI app for Network Extraction. See also [their 2018 paper][3].

[1]: https://stackoverflow.com/questions/69398683/extract-street-network-from-a-raster-image
[2]: https://github.com/05dirnbe/nefi
[3]: https://arxiv.org/pdf/1502.05241.pdf
