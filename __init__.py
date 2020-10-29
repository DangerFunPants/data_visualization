import matplotlib
import matplotlib as plt
import data_visualization.params as cfg

plt.rc("text", usetex=True)
plt.rc("font", **cfg.FONT)
matplotlib.rcParams["xtick.direction"]      = "in"
matplotlib.rcParams["ytick.direction"]      = "in"
matplotlib.rcParams["text.latex.preamble"]  = "\\usepackage{amsmath}\n"   \
                                              "\\usepackage{amssymb}\n"   \
                                              "\\usepackage{amsfonts}\n"  \
                                              "\\usepackage{amsthm}\n"    \
                                              "\\usepackage{graphics}\n" 
                                              
