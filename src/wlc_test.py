##########################################################################################
#
# WLC code testing
#
# Written by Matt Lakin
##########################################################################################

import wlc
import math
import matplotlib.pyplot as plt
import numpy
import time
import sys
import os

# Create and plot samples, as a test
def test(all_nums_ssDNA_nucleotides, all_nums_samples):
    num_rows = len(all_nums_ssDNA_nucleotides)
    num_cols = len(all_nums_samples)
    assert num_rows > 0
    assert num_cols > 0
    fig_width_inches = 4.25 * num_cols # Attempt at smart scaling
    fig_height_inches = 2.2 * num_rows # Attempt at smart scaling
    (fig, axarr) = plt.subplots(num_rows, num_cols, sharex=True, sharey=True, figsize=(fig_width_inches, fig_height_inches))
    axarr = numpy.array([axarr]) if num_rows == 1 and num_cols == 1 else axarr
    for (rdx, num_ssDNA_nucleotides) in enumerate(all_nums_ssDNA_nucleotides):
        for (cdx, num_samples) in enumerate(all_nums_samples):
            this_ax = axarr[rdx] if num_cols == 1 else axarr[cdx] if num_rows == 1 else axarr[rdx,cdx]
            nt_ssDNA = 0.68                      # length per ssDNA nucleotide in nanometres (0.68 nm)
            s = 2                                # persistence length of ssDNA in nanometres (2 nm)
            L = num_ssDNA_nucleotides * nt_ssDNA # total length of 6nt ssDNA domain in metres
            # Compute the actual values for the probability density function (only needed for verification purposes)
            min_R = 0.0
            epsilon = 1e-12 #16
            max_R = L - epsilon # Probability density calculations fail for R >= L
            num_slices = 1000
            actual_xs = numpy.linspace(min_R, max_R, num_slices)
            actual_ys = [wlc.wlc_prob_density(R,s,L) for R in actual_xs]
            # Collect the required number of sampled extension values
            start = time.time()
            print('Producing WLC samples... ', end='')
            sys.stdout.flush()
            wlc_samples = [wlc.get_a_wlc_sample(s,L,num_slices) for _ in range(0, num_samples)]
            print('Done!')
            sys.stdout.flush()
            end = time.time()
            # Plot a histogram of sampled extension values, compared against the plotted expected distribution
            num_histogram_bins = 100
            histogram_bins = numpy.linspace(min_R, max_R, num_histogram_bins)
            this_ax.hist(wlc_samples, histogram_bins, normed=True, facecolor='blue', edgecolor=None) # Histogram of samples
            this_ax.plot(actual_xs, actual_ys, color='red')      # Actual probability density function
            this_ax.axvline(x=min_R, color='red', linestyle=':') # Mark minimum extension
            this_ax.axvline(x=max_R, color='red', linestyle=':') # Mark maximum extension
            if rdx == num_rows - 1:
                this_ax.set_xlabel('Extension (nm)')
            if cdx == 0:
                this_ax.set_ylabel('Probability density')
            label_margin = 0.075
            label_text = (str(num_ssDNA_nucleotides)+'nt ssDNA'+os.linesep+
                          #str(num_samples)+' samples'+os.linesep+
                          ('{:,}'.format(num_samples))+' samples'+os.linesep+
                          'Runtime: '+('{0:0.1f}'.format(end-start))+'s')
            this_ax.text(1.0-label_margin, 1.0-label_margin, label_text, transform=this_ax.transAxes,
                         horizontalalignment='right', verticalalignment='top')
    # Only show tick labels on the top and bottom
    all_but_bottom_row = ([] if num_rows == 1 else [axarr[rdx] for rdx in range(0,num_rows-1)] if num_cols == 1 else
                          [axarr[rdx,cdx] for rdx in range(0,num_rows-1) for cdx in range(0,num_cols)])
    plt.setp([a.get_xticklabels() for a in all_but_bottom_row], visible=False)
    all_but_left_column = (axarr[1:] if num_rows == 1 else [] if num_cols == 1 else
                           [axarr[rdx,cdx] for rdx in range(0,num_rows) for cdx in range(1,num_cols)])
    plt.setp([a.get_yticklabels() for a in all_but_left_column], visible=False)
    # Reset y axis limits
    first_axis = axarr[0] if axarr.ndim == 1 else axarr[0,0]
    first_axis.set_ylim(first_axis.get_ylim()[0], math.ceil(first_axis.get_ylim()[1]))
    # Tighten up layout and save to a PDF file
    plt.tight_layout()
    plotfile = 'wlc_'+str(all_nums_ssDNA_nucleotides).replace(' ','')+'nt_'+str(all_nums_samples).replace(' ','')+'samples.pdf'
    plt.savefig(plotfile, bbox_inches='tight')
    print('Saved plot to '+plotfile)

if __name__ == '__main__':
    all_nums_ssDNA_nucleotides = [5, 6, 8, 10, 15]
    all_nums_samples = [1000, 10000, 100000, 1000000] # Stopping here: 10000000 looks almost identical to 1000000 but takes 10x as long (~10-15 minutes)!
    test(all_nums_ssDNA_nucleotides, all_nums_samples)
