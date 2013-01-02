plottage
========

plottage is where I plan to dump a variety of cleaned-up visualization tools I've written in the past. Most of these use matplotlib.

This first iteration just contains multiplot, a tool that displays one or more series in a single 2D figure. multiplot tries to make it distinguish between series by using different colors and point markers.

Try it out with the example data included:

./multiplot.py example_figure.png "test title" "test x label" "test y label" series1.txt series2.txt series3.txt

Edit constants c_colorwheel and c_markerwheel if you want to draw from a different set of styles. multiplot assumes adjacent c_colorwheel values are equally different from each other.

If you find plottage useful or have a suggestion for new tool or killer feature, let me know! jamesjolly@gmail.com
