import pandas as pd

def load_csv(path):
    return pd.read_csv(path, parse_dates=['timestamp'])

def standardize_columns(df):
    df = df.rename(columns=lambda c: c.strip().lower())
    return df

def add_kpis(df):
    df['sla_breach'] = df['duration_seconds'] > df['sla_target_seconds']
    df['cost_per_second'] = df['cost'] / df['duration_seconds']
    df['cycle_time_min'] = df['duration_seconds'] / 60.0
    return df

def aggregate_by_department(df):
    agg = df.groupby('department').agg(
        transactions=('transaction_id', 'nunique'),
        total_cost=('cost', 'sum'),
        avg_cycle_time_min=('cycle_time_min', 'mean'),
        sla_breach_rate=('sla_breach', 'mean')
    ).reset_index()
    return agg