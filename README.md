# Laptop-price-prediction-
DEPI Graduation project "Laptop price prediction" at Microsoft Data Engineering, AI and Data Science track. Round 1. 2024
# Project Overview:
- This project aims to develop a machine learning model capable of accurately predicting laptop prices based on various features such as processor, RAM, storage, GPU, and brand. The model is trained on a dataset of laptop specifications and their corresponding prices, which are extracted from various online retailers using web scraping techniques.

# Technologies Used:
- Web Scraping: BeautifulSoup, Selenium
- Data Warehousing: SQL Server Integration Services (SSIS)
- Machine Learning: Python, scikit-learn
- Web Application: Flask
- Visualization: Power BI

# Data Pipeline:
- Web Scraping:
Use BeautifulSoup and Selenium to extract data from online retailers like Noon, 2B, Vodafone, Aman, and Jumia.
Extract relevant features like brand, processor, RAM, storage, GPU, and price.

- Data Cleaning and Preprocessing:
Clean the extracted data to handle missing values, inconsistencies, and outliers.
Preprocess the data, including feature engineering and normalization.

- Data Warehousing:
Use SSIS to load the cleaned data into a SQL Server data warehouse.
Transform and aggregate the data for analysis and modeling.
 
# Machine Learning Model:
- Train a machine learning model, such as Gradient Boosting, on the prepared dataset.
Evaluate the model's performance using metrics like accuracy, MSE, and R-squared.

# Web Application:
- Develop a Flask-based web application to provide a user-friendly interface.
- Allow users to input laptop specifications.
- Utilize the trained model to predict the price based on the input.
- Display the predicted price to the user.

# Future Enhancements:
- Geographic Pricing: Incorporate location-based pricing variations.
- Time Series Analysis: Analyze historical price data to predict future trends.
- User Feedback Integration: Allow users to provide feedback on predicted prices to improve model accuracy.
- Mobile App Development: Develop a mobile app for on-the-go price predictions.
