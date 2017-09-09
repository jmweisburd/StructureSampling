import argparse

parser = argparse.ArgumentParser(description='Simulate DNA structures')

parser.add_argument("-w", "--worm", help="turns on worm-like chain disistribution for single stranded DNA domains.", action="store_true")
parser.add_argument("-n", "--nicked", help="turns on nicked angle distribution for the angle between double stranded DNA domains.", action="store_true")
