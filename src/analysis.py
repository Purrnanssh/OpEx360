import argparse
import pandas as pd

def compute_summary(df):
    total_cost = df['cost'].sum()
    total_tx = df['transaction_id'].nunique()
    sla_rate = 1 - df['sla_breach'].mean()
    avg_cycle = df['cycle_time_min'].mean()
    return {
        'total_cost': total_cost,
        'total_transactions': total_tx,
        'sla_compliance_rate': sla_rate,
        'avg_cycle_time_min': avg_cycle
    }

def main(input_path, output_path):
    df = pd.read_csv(input_path, parse_dates=['timestamp'])
    summary = compute_summary(df)
    out = pd.DataFrame([summary])
    out.to_csv(output_path, index=False)
    print(f'Summary saved to {output_path}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    main(args.input, args.output)