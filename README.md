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

## Instructions
Follow these instructions to achieve project goals:

1. **Database Creation**: Create a PostgreSQL database named 'covid_19_data' to store the COVID-19 dataset.

2. **Table Creation**: Within the 'covid_19_data' database, create a table named 'covid_19_data' using the appropriate data types for each column as indicated in the data summary.

3. **Data Type Modification**: Change the data type of the 'ObservationDate' column to 'DATE' within the DataFrame.

4. **Data Extraction and Loading**: Use Python to read the 'Covid_19_data.csv' file and load it into the 'covid_19_data' table in the PostgreSQL database. Utilize the `psycopg2` and `SQLAlchemy` libraries to interact with the database.

5. **SQL Queries**: Use PostgreSQL PGAdmin to create and execute SQL queries. Present all queries within a single SQL file.

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
