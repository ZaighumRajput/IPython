from ggplot import *
diamonds.head()

p + geom_point() + geom_line() + stat_smooth(color='blue')