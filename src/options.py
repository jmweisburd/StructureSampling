import argparse

parser = argparse.ArgumentParser(description='Simulate DNA structures')

parser.add_argument("-w", "--worm", help="turns on worm-like chain disistribution for single stranded DNA simulation.", action="store_true")
