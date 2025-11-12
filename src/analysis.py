import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_behavior(clean_data_path):
    """Analyze consumer decision behavior and visualize key patterns."""

    
    data = pd.read_csv(clean_data_path)
    print("\n Loaded cleaned encoded data for analysis.")
    print(f"Data shape: {data.shape}\n")

    # --- Example 1: Shopping mode preference ---
    # Count distribution of responses to "Which shopping mode do you prefer most often?"
    raw_data = pd.read_csv("outputs/cleaned_data_raw.csv")
    pref_col = "Which shopping mode do you prefer most often?_Online(Ecommerce)"
    if pref_col in raw_data.columns:
        pref_counts = raw_data[pref_col].value_counts()
        print("\nShopping mode preferences:\n", pref_counts, "\n")

        plt.figure(figsize=(7, 4))
        sns.barplot(x=pref_counts.index, y=pref_counts.values, palette="crest")
        plt.title("Preferred Shopping Mode")
        plt.ylabel("Number of Respondents")
        plt.xlabel("Shopping Mode")
        plt.xticks(rotation=15)
        plt.tight_layout()
        plt.savefig("outputs/shopping_mode_preference.png")
        print("Saved: outputs/shopping_mode_preference.png")
    else:
        print(f"⚠️ Column '{pref_col}' not found in raw data. Available columns:\n{list(raw_data.columns)}")


    # --- Example 2: Correlation analysis ---
    corr = data.corr(numeric_only=True)
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, cmap="coolwarm", center=0)
    plt.title("Correlation Heatmap of Survey Features")
    plt.tight_layout()
    plt.savefig("outputs/correlation_heatmap.png")
    print("Saved: outputs/correlation_heatmap.png")

    corr.to_csv("outputs/correlation_matrix.csv")
    print("Correlation matrix saved as outputs/correlation_matrix.csv")

    return corr


if __name__ == "__main__":
    correlation_results = analyze_behavior("outputs/cleaned_data_encoded.csv")
