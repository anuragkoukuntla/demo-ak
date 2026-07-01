import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")

# Display original data
print("Original Raw Data:")
print(df)

# Operations on age column
print("\nAge Operations:")

# Average age
print("Average Age:", df["age"].mean())

# Maximum age
print("Maximum Age:", df["age"].max())

# Minimum age
print("Minimum_Age:", df["age"].min())

# Add 5 years to age
df["age_after_5_years"] = df["age"] + 5

# Categorize ages
df["age_group"] = df["age"].apply(
    lambda x: "Young" if x < 30 else "Adult"
)

print("\nUpdated Data:")
print(df)