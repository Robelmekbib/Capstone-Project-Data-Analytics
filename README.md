# Data Analytics Capstone Project: Effects of COVID-19 on Trade

## Project Overview

This project analyzes the impact of COVID-19 on trade data from various countries, focusing on trade values over time, modalities, and commodities involved. The analysis includes data loading, cleaning, exploratory data analysis (EDA), statistical modeling, and the development of an interactive dashboard.

## Table of Contents

- [1. Introduction](#1-introduction)
- [2. Data Collection and Cleaning](#2-data-collection-and-cleaning)
- [3. Exploratory Data Analysis (EDA)](#3-exploratory-data-analysis-eda)
- [4. Modeling](#4-modeling)
- [5. Dashboard Development](#5-dashboard-development)
- [6. Conclusion](#6-conclusion)
- [7. Acknowledgments](#7-acknowledgments)

## 1. Introduction

This project aims to explore the effects of COVID-19 on trade using a dataset obtained from the Office for National Statistics (ONS). The dataset contains information on trade values, countries, commodities, and transport modes.
## 2. Data Collection and Cleaning

The dataset used for this analysis is `effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv`, which includes trade data from various countries around the world affected by the COVID-19 pandemic.

### Steps for Data Cleaning
- Loaded the dataset using Pandas.
- Checked for missing values and handled them.
- Cleaned the 'Value' column to remove dollar signs and commas, converting it into a numerical format.
- Converted the 'Date' column into proper datetime format for analysis.

## 3. Exploratory Data Analysis (EDA)

In this section, i performed various analyses to glean insights from the data, including:
- Summary statistics for understanding the data distribution.
- Bar plots and histograms to visualize cumulative trade values and trade value distributions.
- Box plots to identify outliers in trade values by country.

### Visualizations
- **Cumulative Trade Values by Country**
- **Distribution of Trade Values**
- **Top 10 Countries by Trade Value**
- **Box Plot of Trade Values by Country**

## 4. Modeling

### A. Forecasting

An ARIMA model was implemented to forecast future trade values based on historical data. The model fitting yielded the following results:

- **RMSE**: 794,014.31 (indicating the model's accuracy).

### B. Classification

Using a Random Forest Classifier, the project aimed to classify trading directions, achieving an accuracy of 91% as demonstrated by the confusion matrix and classification report.

## 5. Dashboard Development

An interactive dashboard was developed using Dash and Plotly to allow users to explore trade values over time per country. Users can select a country from a dropdown to visualize its trade values through a line chart.

### Features:
- Interactive country selection.
- Dynamic updates for trade value visualizations.

## 6. Conclusion

This project effectively demonstrates the significant impacts of COVID-19 on trade through comprehensive analysis and modeling techniques. The developed dashboard acts as a user-friendly interface to explore trade trends and foster informed decision-making.

## 7. Acknowledgments

- Thank you to Menore Tekeba 
- Special thanks to AAiT for providing us with this opportunity 
