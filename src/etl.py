import argparse
from transformations import load_csv, standardize_columns, add_kpis

def main(input_path, output_path):
    df = load_csv(input_path)
    df = standardize_columns(df)
    df = add_kpis(df)
    df.to_csv(output_path, index=False)
    print(f'Wrote cleaned data to {output_path}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    main(args.input, args.output)