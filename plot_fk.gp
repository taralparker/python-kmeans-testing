#!/usr/bin/gnuplot
set term post eps color enh "Times-Bold" 20
set output "guassian3.eps"
set title "f(K)"
set xtics nomirror
set nokey
set xlabel "Number of Clusters"
set yrange [0:1.4]
set grid ytics lt 1 lw 1.2 lc rgb "#bbbbbb"
set xtics (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)
plot "./guass3.dat" title "f(K)" with linespoints ls 1 lt 1 lc 7 lw 3 pt 7 ps 1.5

