import argparse
from .score_calculator import calcular_hubs

def main():
    parser = argparse.ArgumentParser(description="Find hub genes from a network CSV file.")
    parser.add_argument("input_file", type=str, help="Path to input CSV file")
    parser.add_argument("percentile", type=float, help="Percentile threshold for hub selection")

    args = parser.parse_args()
    calcular_hubs(args.input_file, args.percentile)

if __name__ == "__main__":
    main()
