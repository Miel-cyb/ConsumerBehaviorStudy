import pandas as pd

def load_and_clean_data(filepath):
    """Load and clean Google Form survey responses."""

 
    data = pd.read_excel(filepath)
    print(f"\nLoaded dataset with {data.shape[0]} rows and {data.shape[1]} columns.")

    
    if "Timestamp" in data.columns:
        data.drop(columns=["Timestamp"], inplace=True)
        print(" Dropped column: Timestamp")

    # Drop rows with all missing values
    data.dropna(how='all', inplace=True)

    # Fill missing text responses with 'No Response'
    cat_cols = data.select_dtypes(include='object').columns
    data[cat_cols] = data[cat_cols].fillna('No Response')

    # Encode categorical responses into numeric values for correlation or modeling
    data_encoded = pd.get_dummies(data, drop_first=True)

    # Save cleaned files
    data.to_csv("outputs/cleaned_data_raw.csv", index=False)
    data_encoded.to_csv("outputs/cleaned_data_encoded.csv", index=False)

    print(f" Cleaned data saved to 'outputs/cleaned_data_raw.csv' and encoded version to 'outputs/cleaned_data_encoded.csv'.")
    print(f" Final encoded shape: {data_encoded.shape}")

    return data, data_encoded


if __name__ == "__main__":
    raw, encoded = load_and_clean_data("data/Consumer Purchase & Stock Prediction Study (Responses).xlsx")
