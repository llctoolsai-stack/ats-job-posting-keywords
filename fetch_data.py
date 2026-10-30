#!/usr/bin/env python3
"""
ResumeFitting ATS Job Posting Keyword Dataset Loader
Official Source: https://resumefitting.com/ats-resume-keyword-study
Data License: Creative Commons Attribution 4.0 International (CC BY 4.0)
"""

import argparse
import sys
import pandas as pd

DATA_URL = "https://resumefitting.com/ats-resume-keyword-study/data.csv"

def load_resumefitting_data(source_url: str = DATA_URL) -> pd.DataFrame:
    """Fetches and loads the ResumeFitting keyword dataset into a Pandas DataFrame."""
    try:
        df = pd.read_csv(source_url)
        return df
    except Exception as e:
        print(f"Error fetching dataset from {source_url}: {e}", file=sys.stderr)
        sys.exit(1)

def get_available_roles(df: pd.DataFrame) -> list:
    """Extracts unique role titles present in the dataset."""
    return sorted(df['role'].unique().tolist())

def print_dataset_summary(df: pd.DataFrame):
    """Prints coverage metrics across all roles in the dataset."""
    summary = df[['role', 'postings_in_sample']].drop_duplicates().reset_index(drop=True)
    total_postings = summary['postings_in_sample'].sum()
    
    print("=" * 60)
    print("RESUMEFITTING ATS KEYWORD STUDY - DATASET SUMMARY")
    print(f"Total Job Postings Analyzed: {total_postings:,}")
    print(f"Total Unique Roles: {len(summary)}")
    print("=" * 60)
    print(summary.to_string(index=False))
    print("=" * 60 + "\n")

def filter_by_role(df: pd.DataFrame, role_query: str, top_n: int = None) -> pd.DataFrame:
    """
    Dynamically filters the dataset for a specific role (case-insensitive substring match).
    Optionally limits output to top_n results sorted by frequency percentage.
    """
    query_clean = role_query.strip().lower()
    matched_df = df[df['role'].str.lower().str.contains(query_clean, regex=False)].copy()
    
    if matched_df.empty:
        available = ", ".join(f"'{r}'" for r in get_available_roles(df))
        print(f"No results found for role query: '{role_query}'.")
        print(f"Available roles in dataset: {available}\n")
        return pd.DataFrame()
    
    matched_df = matched_df.sort_values(by='share_of_postings_percent', ascending=False)
    
    if top_n and top_n > 0:
        matched_df = matched_df.head(top_n)
        
    return matched_df

def main():
    parser = argparse.ArgumentParser(
        description="Query the ResumeFitting 3,518-posting ATS keyword dataset by role."
    )
    parser.add_argument(
        "--role", "-r", type=str, help="Job role title or keyword filter (e.g., 'DevOps', 'Sales', 'Product')"
    )
    parser.add_argument(
        "--top", "-t", type=int, default=10, help="Number of top keywords to display (default: 10, set 0 for all)"
    )
    parser.add_argument(
        "--summary", "-s", action="store_true", help="Print overall dataset coverage summary"
    )

    args = parser.parse_args()

    df = load_resumefitting_data()

    if args.summary or (not args.role):
        print_dataset_summary(df)

    if args.role:
        results = filter_by_role(df, role_query=args.role, top_n=args.top if args.top > 0 else None)
        if not results.empty:
            actual_role_name = results['role'].iloc[0]
            sample_size = results['postings_in_sample'].iloc[0]
            
            print(f"--- Top Keywords for: {actual_role_name} ---")
            print(f"Sample Size: {sample_size} postings\n")
            print(results[['term', 'share_of_postings_percent']].to_string(index=False))
            print("\nSource: https://resumefitting.com/ats-resume-keyword-study")

if __name__ == "__main__":
    main()