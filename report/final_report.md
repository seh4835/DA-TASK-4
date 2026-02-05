# Final Data Analysis Report

# Project Title: Multi-Dimensional Analysis of E-commerce Sales Dataset

## 1. Introduction

This project focuses on performing a complete data analysis pipeline on a real-world e-commerce sales dataset. The objective of the analysis is to extract meaningful insights by examining the data from two different analytical perspectives using the same dataset. The first analysis concentrates on category-level sales performance, while the second analysis evaluates product-level performance and the relationship between quantity sold and revenue. This approach demonstrates how a single dataset can be explored from multiple dimensions to support data-driven decision-making in a business context.

## 2. Dataset Description

The dataset used in this project contains transactional records from an e-commerce platform. It includes attributes such as product name, product category, quantity sold, and sales revenue. Each record represents an individual order item. The dataset was loaded from a CSV file and validated before analysis. Missing values were removed to ensure data quality and consistency during computation and visualization.

## 3. Data Cleaning and Preprocessing

Before analysis, the dataset was cleaned to handle missing or incomplete records. Rows containing null values were removed to avoid errors during aggregation and visualization. Basic validation checks were performed to ensure that numerical fields such as sales revenue and quantity sold were in the correct format. Summary statistics were generated to understand the distribution, range, and central tendency of the numeric variables.

## 4. Analysis 1: Category-Level Sales Analysis

The first analysis focused on understanding performance across different product categories.

Visualization 1: Category Distribution (Bar Chart)
A bar chart was used to visualize the distribution of products across different categories. This helped in identifying which categories had the highest number of products or transactions. Categories with higher counts indicate areas of greater business activity and customer demand.

Visualization 2: Total Sales by Category (Line Chart)
A line chart was created to show the total sales revenue aggregated by product category. This visualization highlights which categories contribute the most to overall revenue. Categories with high sales values represent key revenue drivers for the business, while low-performing categories indicate potential areas for improvement or strategic intervention.

### Key Insights from Analysis 1:

Certain product categories dominate both in volume and revenue contribution.

Revenue distribution is not uniform across categories, indicating a skewed sales pattern.

High-performing categories can be prioritized for marketing, inventory expansion, and promotional campaigns.

## 5. Analysis 2: Product-Level Performance Analysis

The second analysis examined individual product performance and the relationship between quantity sold and sales revenue.

Visualization 3: Top 10 Products by Sales (Bar Chart)
A bar chart was used to display the top 10 products ranked by total sales revenue. This identifies the best-selling products and highlights key contributors to business revenue. These products can be considered flagship offerings and can be leveraged for cross-selling and promotions.

Visualization 4: Sales vs Quantity Sold (Scatter Plot)
A scatter plot was created to analyze the relationship between quantity sold and sales revenue. This visualization helps in understanding whether higher sales values are driven by higher quantities sold or by higher-priced products. It also highlights potential outliers such as products with high revenue despite low quantity, indicating premium pricing.

### Key Insights from Analysis 2:

A small subset of products contributes disproportionately to total revenue.

There is a positive relationship between quantity sold and sales revenue, though the relationship is not perfectly linear.

Some products generate high revenue even with lower quantities sold, indicating high-value or premium products.

## 6. Overall Findings and Business Implications

By analyzing the dataset from both category-level and product-level perspectives, the project demonstrates how different analytical viewpoints can yield complementary insights from the same data. Category-level analysis helps in strategic planning at a macro level, while product-level analysis supports operational decisions such as inventory management, pricing strategy, and promotional planning. Together, these analyses provide a comprehensive understanding of sales performance and business dynamics.

## 7. Conclusion

This project successfully implemented an end-to-end data analysis workflow, including data loading, cleaning, exploratory analysis, visualization, and insight generation. Two distinct analyses were conducted on the same e-commerce dataset to showcase multi-dimensional analytical thinking. The visualizations and insights derived from this study can assist stakeholders in making informed, data-driven business decisions related to product strategy, category management, and revenue optimization.

## 8. Tools and Technologies Used

Python

Pandas (data loading and preprocessing)

Matplotlib (data visualization)

## 9. Limitations and Future Scope

The analysis was limited to the available attributes in the dataset. I also had trouble because in the options it was mentioned to do Student performance analysis but the data was on sales so i had to change it to Product performance analysis. Future work could include incorporating time-based analysis (e.g., monthly or seasonal sales trends), customer segmentation, and predictive modeling to forecast future sales. Integrating additional data sources such as customer demographics and marketing campaigns would further enhance the depth of insights.
