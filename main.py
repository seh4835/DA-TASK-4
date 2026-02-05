import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
DATA_PATH = "C:\\Users\\Seher\\Desktop\\DA-TASK-4\\data\\sales_data.csv"
VIS_PATH = "visualizations"

os.makedirs(VIS_PATH, exist_ok=True)

# Load Data
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError("Dataset not found in data folder")

df = pd.read_csv(DATA_PATH)

# Data Cleaning-
df.dropna(inplace=True)

# Print Columns (for debugging)
print("Columns in dataset:", df.columns.tolist())

CATEGORY_COL = "Product"
SALES_COL = "Total_Sales"
QTY_COL = "Quantity"

# BASIC ANALYSIS
print("\nSummary Statistics:\n", df.describe())

# ANALYSIS 1: E-COMMERCE SALES ANALYSIS

# Chart 1: Category Distribution (Bar Chart)
plt.figure(figsize=(8, 5))
df[CATEGORY_COL].value_counts().plot(kind='bar')
plt.title("Product Count by Category")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig(f"{VIS_PATH}/analysis1_category_distribution.png")
plt.close()

# Chart 2: Total Sales by Category (Line Chart)
plt.figure(figsize=(8, 5))
df.groupby(CATEGORY_COL)[SALES_COL].sum().plot(kind='line', marker='o')
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(f"{VIS_PATH}/analysis1_sales_by_category.png")
plt.close()

print("✅ Analysis 1 (E-commerce Sales) completed.")

# ANALYSIS 2: PRODUCT PERFORMANCE ANALYSIS

# Chart 3: Top 10 Products by Sales (Bar Chart)
top_products = df.groupby("Product")[SALES_COL].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(9, 5))
top_products.plot(kind='bar')
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f"{VIS_PATH}/analysis2_top_products_by_sales.png")
plt.close()

# Chart 4: Sales vs Quantity (Scatter Plot)
plt.figure(figsize=(7, 5))
plt.scatter(df[QTY_COL], df[SALES_COL])
plt.title("Sales vs Quantity Sold")
plt.xlabel("Quantity Sold")
plt.ylabel("Sales Amount")
plt.tight_layout()
plt.savefig(f"{VIS_PATH}/analysis2_sales_vs_quantity.png")
plt.close()

print("✅ Analysis 2 (Product Performance) completed.")

print("\n All visualizations saved in the 'visualizations/' folder.")
print("Two different analyses completed using the same dataset.")
