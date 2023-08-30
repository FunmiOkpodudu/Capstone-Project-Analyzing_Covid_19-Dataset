
![image](https://github.com/FunmiOkpodudu/Capstone-Project-Analyzing_Covid_19-Dataset/assets/134555960/339fda48-5dde-464f-a335-8a371056cdaa)










# Data Engineering Capstone Project 1 (Analyzing COVID-19 Data)

## Table of Contents
- [Introduction/Project Overview](#introductionproject-overview)
- [Objective](#objective)
- [Data Summary](#data-summary)
- [Instructions](#instructions)
- [How It Works](#how-it-works)
- [Loading the Data](#loading-the-data)
- [Requirements](#requirements)
- [Conclusion](#conclusion)
- [Contribution/Feedback](#contributionfeedback)

## Introduction/Project Overview
Welcome to Data Engineering Capstone Project 1 – Analyzing COVID-19 Data. In this project, we delve into the analysis of sample data related to COVID-19 cases recorded between January 2019 and December 2020. The dataset, provided in CSV format, enables us to gain insights into the pandemic's impact.

## Objective
The primary objective of this project is to analyze and gain insights from COVID-19 data. This includes creating a dedicated database and table within it to house the dataset, converting data types, and performing Extraction and Load (EL) techniques to load the data into the database.

## Data Summary
Fetch the summary of the table datatypes for each column.

Certainly, here's the revised "Instructions" section based on your provided content:

## Instructions
Ensure that PostgreSQL is used as the designated database tool for this project. Follow these steps to successfully complete the project:

1. **Database and Table Creation**: Start by establishing a database named 'covid_19_data'. Within this database, create a table named 'covid_19_data' specifically designed to accommodate the dataset.

2. **Data Type Modification**: Modify the data type of the 'ObservationDate' column within the 'covid_19_data' table. Change it from its initial 'String' representation to the more appropriate 'DATE' data type.

3. **Data Extraction and Loading**: Utilize a Python script to procure the 'Covid_19_data.csv' file. Once obtained, load the data from this file into the 'covid_19_data' table within the PostgreSQL database. Ensure that data integrity is maintained during this process.

4. **SQL Queries Using PostgreSQL PGAdmin**: Leverage PostgreSQL PGAdmin, a powerful database management tool, for both creating and executing SQL queries. Use this platform to gain insights from the dataset and answer relevant questions.

5. **Consolidated SQL File**: Document your SQL queries within a singular SQL file. This consolidated file should include all the SQL queries you create during the project. Organize the file for clarity and readability.

By following these instructions, you will systematically utilize PostgreSQL for establishing the database, loading the data, and conducting SQL queries. The provided steps will enable you to effectively analyze the COVID-19 dataset and draw meaningful conclusions.

Feel free to adapt these instructions based on your project's requirements and the tools you're using.

## How It Works
1. **Database Creation**: Use PgAdmin to create a new PostgreSQL database named 'covid_19_data'.

2. **Table Creation**: Within the 'covid_19_data' database, create a table named 'covid_19_data' using the data summary's column names and data types.

3. **Data Type Modification**: Change the data type of the 'ObservationDate' column to 'DATE' within the DataFrame.

4. **Data Extraction and Loading**: Read the 'Covid_19_data.csv' file using Pandas. Use the `psycopg2` and `SQLAlchemy` libraries to connect to the PostgreSQL database and load the data into the 'covid_19_data' table.

## Loading the Data
The data loading process involves using Python and the `psycopg2` and `SQLAlchemy` libraries to extract the COVID-19 data from the CSV file and load it into the PostgreSQL database.

## Requirements
Ensure the following requirements are met:
- Python 3.x
- Pandas library
- SQLAlchemy library
- PostgreSQL database

## Conclusion
In conclusion, this project involved the analysis of COVID-19 data using PostgreSQL as the chosen database tool. The dataset was transformed and loaded into the 'covid_19_data' database table using Python, Pandas, `psycopg2`, and `SQLAlchemy`. The project's SQL queries were executed using PostgreSQL PGAdmin for deeper insights.

## Contribution/Feedback
Contributions to enhance and extend this project are highly appreciated. Feel free to contribute through pull requests, report issues, or provide feedback. Your input will help improve the project for the benefit of the community.
