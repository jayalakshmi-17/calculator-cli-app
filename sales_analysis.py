```python
# Task 5 : Data Analysis on CSV Files
# Objective: Analyze sales data using Pandas in IDLE

import pandas as pd
import matplotlib.pyplot as plt

# --- Step 1: Load CSV File ---
# Replace with your actual CSV file name (keep it in the same folder as this script)
df = pd.read_csv("sales_data.csv")

# --- Step 2: Explore the Dataset ---
print("First 5 rows of data:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# --- Step 3: GroupBy Analysis ---
# Example 1: Sales by Product
if "Product" in df.columns and "Sales" in df.columns:
    sales_by_product = df.groupby("Product")["Sales"].sum()
    print("\nTotal Sales by Product:")
    print(sales_by_product)

# Example 2: Sales by Region
if "Region" in df.columns and "Sales" in df.columns:
    sales_by_region = df.groupby("Region")["Sales"].sum()
    print("\nTotal Sales by Region:")
    print(sales_by_region)

# Example 3: Sales Trend Over Time (if Date column exists)
if "Date" in df.columns and "Sales" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    sales_over_time = df.groupby("Date")["Sales"].sum()
    print("\nSales Trend Over Time (first few entries):")
    print(sales_over_time.head())

# --- Step 4: Visualizations ---
if "Product" in df.columns and "Sales" in df.columns:
    sales_by_product.plot(kind="bar", figsize=(8,5), title="Sales by Product", color="skyblue")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.show()

if "Region" in df.columns and "Sales" in df.columns:
    sales_by_region.plot(kind="pie", autopct="%1.1f%%", figsize=(6,6), title="Sales by Region")
    plt.ylabel("")
    plt.show()

if "Date" in df.columns and "Sales" in df.columns:
    sales_over_time.plot(kind="line", figsize=(10,5), title="Sales Over Time", marker="o")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.show()

# --- Step 5: Key Insights ---
if "Sales" in df.columns:
    print("\n🔑 Insights:")
    print(f"Total Sales: {df['Sales'].sum()}")

if "Product" in df.columns and "Sales" in df.columns:
    print(f"Top-Selling Product: {sales_by_product.idxmax()} ({sales_by_product.max()})")

if "Region" in df.columns and "Sales" in df.columns:
    print(f"Top-Performing Region: {sales_by_region.idxmax()} ({sales_by_region.max()})")
```
