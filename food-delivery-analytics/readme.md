# Steps to activate virtual envronment inside this project
Goto /Users/archanasubramaniyam/Documents/Workspace/AneganArts/GUVI_DS_PRACTICES/Project1/EarthquakeAnalysisProject
python3 -m venv env
source env/bin/activate

To execute requrement.txt follow the command : pip install -r requirements.txt

# 🍔 Online Food Delivery Analytics Dashboard

A complete **Data Analytics and Business Intelligence project** that analyzes online food delivery data to uncover insights related to customer behavior, delivery performance, restaurant performance, and revenue trends.

The project demonstrates **end-to-end data analytics workflow** including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Database Storage (MySQL)
- Interactive Dashboard using Streamlit

---

# 📊 Project Overview

Online food delivery platforms generate large amounts of transactional and behavioral data.  
This project analyzes **100,000 food delivery orders** to extract meaningful insights that can help businesses improve operations and decision-making.

Key analysis areas include:

- Customer ordering behavior
- Restaurant performance
- Delivery efficiency
- Revenue and profitability
- Operational insights

---

# 🎯 Business Objectives

The project aims to help food delivery companies:

- Optimize delivery time and logistics
- Identify high-performing restaurants
- Understand customer ordering patterns
- Reduce cancellations and delays
- Track key performance indicators (KPIs)
- Improve profitability through data-driven insights

---

# 🗂 Dataset

The dataset contains **100,000 online food delivery orders** with **25 features** covering:

### Customer Details
- Customer ID
- Age
- Gender
- City
- Area

### Order Information
- Order ID
- Order Value
- Discount Applied
- Final Amount
- Payment Mode
- Order Status

### Restaurant Attributes
- Restaurant ID
- Restaurant Name
- Cuisine Type

### Delivery Performance
- Delivery Time
- Distance
- Delivery Partner ID
- Delivery Rating

### Operational Data
- Cancellation Reason
- Order Date
- Order Time

---

# 🔧 Project Workflow

## 1️⃣ Data Collection
Dataset containing **100,000 orders** collected and imported for analysis.

---

## 2️⃣ Data Understanding
Exploration of dataset structure:

- Data types
- Missing values
- Feature distributions
- Categorical variables

---

## 3️⃣ Data Cleaning & Preprocessing

Key preprocessing steps included:

- Handling missing values
- Removing outliers
- Standardizing categorical values
- Correcting invalid values
- Ensuring logical consistency in the dataset

---

## 4️⃣ Exploratory Data Analysis (EDA)

EDA was performed to uncover hidden patterns:

- Order value distribution
- Delivery time analysis
- City-wise order patterns
- Weekend vs weekday demand
- Distance vs delivery time
- Cancellation analysis
- Correlation analysis

---

## 5️⃣ Feature Engineering

Additional features were created for deeper analysis:

- Order Day Type (Weekend / Weekday)
- Peak Hour Indicator
- Profit Margin Percentage
- Delivery Performance Category
- Customer Age Groups

---

## 6️⃣ Data Storage

Cleaned dataset was stored in **MySQL** for scalable querying and reporting.

Tools used:
- SQLAlchemy
- MySQL

---

# 📊 Streamlit Dashboard

An interactive **Streamlit dashboard** was built to visualize key business metrics and insights.

### Key KPIs Displayed

- Total Orders
- Total Revenue
- Average Order Value
- Average Delivery Time
- Cancellation Rate
- Average Delivery Rating
- Profit Margin %

### Dashboard Features

- Interactive **City and Cuisine filters**
- Revenue analysis by city
- Cuisine order distribution
- Delivery performance visualization
- Distance vs delivery time analysis
- Data preview section

---

# 🖥 Dashboard Preview

![Dashboard Screenshot](dashboard.png)

---

# 🛠 Technologies Used

| Tool | Purpose |
|-----|------|
| Python | Data analysis |
| Pandas | Data manipulation |
| NumPy | Numerical processing |
| Matplotlib / Seaborn | Exploratory data analysis |
| MySQL | Data storage |
| SQLAlchemy | Database connection |
| Streamlit | Dashboard creation |
| Plotly | Interactive visualizations |

---

# 🚀 How to Run the Project

## 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/food-delivery-analytics.git
cd food-delivery-analytics


2️⃣ Install required packages
pip install -r requirements.txt
3️⃣ Setup MySQL Database
Create a database:
FoodDelivery
Import the cleaned dataset into table:
onlinefoods
4️⃣ Run the Streamlit Dashboard
streamlit run app.py
Open browser:
http://localhost:8501
📈 Key Insights from Analysis
Some insights discovered during analysis:
Weekend orders are significantly higher than weekdays
Certain cuisines generate more revenue than others
Longer delivery distance leads to increased delivery time
High discounts can reduce profit margins
Some cities show higher cancellation rates
📁 Project Structure
food-delivery-analytics
│
├── data
│   └── ONINE_FOOD_DELIVERY_ANALYSIS.csv
│
├── notebooks
│   └── EDA_analysis.ipynb
│
├── dashboard
│   └── app.py
│
├── images
│   └── dashboard.png
│
├── README.md
└── requirements.txt
🌟 Future Improvements
Possible enhancements:
Machine Learning for delivery time prediction
Customer segmentation analysis
Restaurant recommendation system
Advanced BI dashboard features
Real-time data integration