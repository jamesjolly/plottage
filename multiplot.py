#!/usr/bin/python
"""
plottage 0.1
Copyright (C) 2013, James Jolly (jamesjolly@gmail.com)
See MIT-LICENSE.txt for legalese and README.md for usage.
"""

import sys
from matplotlib import pyplot
from scipy import inf

c_colorwheel = [
   '#FF0000',
   '#EF000F',
   '#DF001F',
   '#CF002F',
   '#BF003F',
   '#AF004F',
   '#9F005F',
   '#8F006F',
   '#7F007F',
   '#6F008F',
   '#5F009F',
   '#4F00AF',
   '#3F00BF',
   '#2F00CF',
   '#1F00DF',
   '#0F00EF',
   '#0000FF'
]

c_markerwheel = [
   'x-',
   'o-',
   '>-',
   's-',
   'p-',
   'd-'
]

def read_vals(filename):
   x = [ ]
   y = [ ]
   infile = open(filename, 'r')
   for line in infile:
      fields = line.split()
      if len(fields) < 2:
          continue
      x.append(float(fields[1]))
      y.append(float(fields[0]))
   infile.close()
   return x, y

def add_series(datafile, series_no, marker, color):
    y, x = read_vals(datafile)
    pyplot.plot(
        x,
        y,
        marker,
        color=color,
        linewidth=2.0,
        label=datafile
        )
    return min(x), max(x), min(y), max(y)

def save_plot(x_start, x_end, y_start, y_end, title, x_label, y_label, outfile):
    pyplot.axis([x_start, x_end, y_start, y_end])
    pyplot.xlabel(x_label)
    pyplot.ylabel(y_label)
    pyplot.legend(loc='upper left')
    pyplot.title(title)
    pyplot.savefig(outfile)

if __name__ == "__main__":

    argc = len(sys.argv)
    argc_required = 5
    if argc <= argc_required:
       print 'argument error, try: ./multiplot.py figure.png title xlabel ylabel series1.txt (series2.txt series3.txt ...)'
       sys.exit(0)

    colorinc = max(len(c_colorwheel)/(argc - argc_required), 1)
    all_min_x, all_max_x, all_min_y, all_max_y = inf, -inf, inf, -inf
    for i in range(argc_required, argc):
        min_x, max_x, min_y, max_y = add_series(
            datafile=sys.argv[i],
            series_no=i,
            marker=c_markerwheel[i % len(c_markerwheel)],
            color=c_colorwheel[((i - argc_required)*colorinc) % len(c_colorwheel)]
            )
        all_min_x = min(min_x, all_min_x)
        all_max_x = max(max_x, all_max_x)
        all_min_y = min(min_y, all_min_y)
        all_max_y = max(max_y, all_max_y)
    save_plot(
        x_start=all_min_x, 
        x_end=all_max_x,
        y_start=all_min_y, 
        y_end=all_max_y, 
        title=sys.argv[2], 
        x_label=sys.argv[3], 
        y_label=sys.argv[4], 
        outfile=sys.argv[1]
        )

