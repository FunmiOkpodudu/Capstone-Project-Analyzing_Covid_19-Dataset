#!/usr/bin/env python
# coding: utf-8

# # 

# #   <center>DATA ENGINEERING CAPSTONE PROJECT 1 (ANALYZING COVID 19 DATA)</center>

# ### STEP 1 - Create Database

# ### Creating a Postgres database named covid_19_data in pgAdmin
# 
#     Steps taken:
#         -Open pgAdmin: Launch the pgAdmin application on the computer.
#         -Connect to a Server: Connect to the PostgreSQL server to create the new database. Necessary server connection details provided, such as host, port, username, and password.
#         -Create a New Database: Right-click on the "Databases" node and select "New Database."
#         -Provide Database Details: A dialog box appeared where i provided the details for the new database.
#         -Database: Enter a name for the new database (name is covid_19_data)  
#         -Owner: Choose the owner of the database which is postgres.
#         -Encoding: Choose the character encoding for the database. UTF-8 is a common choice.
# 
# 
# 
# 
# 

# ###  STEP 2 - Executing SQL codes

# ### Loading the SQL extension in a Jupyter Notebook environment. Using sql magic command helps to execute SQL code directly within the notebook cells.

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[2]:


Password_DB = ""


# In[3]:


from urllib.parse import quote
password = quote("")
connection_url = f"postgresql://postgres:{password}@localhost:5432/covid_19_data"


# In[4]:


get_ipython().run_line_magic('sql', '$connection_url')


# ### STEP 3 - Creating a table in the database

# In[6]:


get_ipython().run_cell_magic('sql', '', '\n\nCREATE TABLE covid_19_data (\n    SNo serial,\n    ObservationDate text,\n    Province text,\n    Country text,\n    LastUpdate text,\n    Confirmed int,\n    Deaths int,\n    Recovered int\n    \n)\n')


# ### STEP 4 - Modifying the column "ObservationDate" datatype

# In[9]:


get_ipython().run_cell_magic('sql', '', '\nALTER TABLE covid_19_data\nALTER COLUMN ObservationDate TYPE DATE\nUSING ObservationDate::DATE;\n')


# In[10]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM covid_19_data\n')


# ### STEP 5 - Extraction of .csv File

# In[11]:


import pandas as pd


# In[12]:


covid_19_dataset = pd.read_csv('covid_19_data.csv')


# In[13]:


covid_19_dataset.head()


# ### STEP 6 - Modification of coulmns

# In[14]:


covid_19_dataset.columns = covid_19_dataset.columns.str.lower()


# In[15]:


covid_19_dataset


# ### STEP 6 - Loading the table into a DB
# 
# To load a table into postgres database two python libraries are needed to be installed: (1) psycopg2 is a Python library used to interact with PostgreSQL databases.
# 
# (2) Sqlalchemy is a Python library that provides a high-level, Object-Relational Mapping (ORM) framework for working with relational databases. SQLAlchemy makes it easier to interact with databases by abstracting away many of the low-level details of database operations.
# 
# 

# In[27]:


pip install psycopg2


# In[28]:


pip install sqlalchemy


# In[16]:


from sqlalchemy import create_engine # its a function used to create a connection to a database


# In[17]:


engine = create_engine("postgresql://postgres:pw@localhost:5432/covid_19_data")
connection = engine.connect()
covid_19_dataset.to_sql('covid_19_data', con=engine, if_exists='append',index=False)


# ### STEP 7 - Retrieve data from a table 
# The select function generates a SQL query that retrieves data from a table named covid_19_data

# In[18]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM covid_19_data\n')


# ### TASK 8 - Creation and Execution of SQL queries.

# ### A. Retrieve the cumulative counts of confirmed, deceased, and recovered cases.

# In[19]:


get_ipython().run_cell_magic('sql', '', '\nSELECT SUM(confirmed) AS total_confirmed_cases,\n        SUM(deaths) AS total_deceased_cases,\n        SUM(recovered) AS total_recovered_cases\nFROM\n    covid_19_data\n')


# ### B. Extract the aggregate counts of confirmed, deceased, and recovered cases for the first quarter of each observation year.

# In[20]:


get_ipython().run_cell_magic('sql', '', "\nSELECT DATE_TRUNC('year', observationdate) as observation_year, \n    SUM(confirmed) as total_confirmed_cases,\n    SUM(deaths) as total_deceased_cases,\n    SUM(recovered) as total_recovered_cases from covid_19_data WHERE EXTRACT(QUARTER FROM observationdate) = 1 \n    \n    GROUP BY observation_year ORDER BY observation_year;\n")


# ###  C.Formulate a comprehensive summary encompassing the following for each country: Total confirmed cases Total deaths Total recoveries

# In[21]:


get_ipython().run_cell_magic('sql', '', '\nSELECT country, sum(confirmed) as Total_confirmed_cases_for_each_country, \n        sum(deaths) as Total_deaths_cases_for_each_country, \n        sum(recovered) as Total_recovered_cases_for_each_country\nfrom covid_19_data GROUP BY country ORDER BY country\n')


#  ### D. Determine the percentage increase in the number of death cases from 2019 to 2020.

# In[22]:


get_ipython().run_cell_magic('sql', '', '\nSELECT \n    SUM(deaths) as total_deaths_2019 \nFROM \n    covid_19_data \nWHERE \n    EXTRACT(YEAR FROM observationdate) = 2019;\n')


# In[23]:


get_ipython().run_cell_magic('sql', '', '\nSELECT \n    sum(deaths) as total_deaths_2020 \nfrom covid_19_data \n\nWHERE \n    EXTRACT(YEAR FROM observationdate) = 2020;\n')


# In[24]:


get_ipython().run_cell_magic('sql', '', '\nSELECT \n    ((total_deaths_2020 - total_deaths_2019) / total_deaths_2019) * 100 as percentage_increase\nFROM \n    (SELECT \n        sum(deaths) as total_deaths_2019 \n    FROM \n        covid_19_data \n    WHERE \n        EXTRACT(YEAR FROM observationdate) = 2019) AS deaths_2019,\n    (SELECT \n        sum(deaths) as total_deaths_2020 \n    FROM \n        covid_19_data \n    WHERE \n        EXTRACT(YEAR FROM observationdate) = 2020) AS deaths_2020;\n')


# ### E. Compile data for the top 5 countries with the highest confirmed cases.

# In[25]:


get_ipython().run_cell_magic('sql', '', '\nSELECT country, sum(confirmed) as total_confirmed_cases \n\nfrom covid_19_data \n\nGROUP BY country \n\nORDER BY total_confirmed_cases DESC LIMIT 5;\n')


# ### F.Calculate the net change (increase or decrease) in confirmed cases on a monthly basis over the two-year period.

# In[26]:


get_ipython().run_cell_magic('sql', '', "\nSELECT\n    DATE_TRUNC('month', observationdate) AS month_start,\n    SUM(confirmed) AS total_confirmed_cases,\n    LAG(SUM(confirmed), 1) OVER (ORDER BY DATE_TRUNC('month', observationdate)) AS prev_month_cases,\n    SUM(confirmed) - LAG(SUM(confirmed), 1) OVER (ORDER BY DATE_TRUNC('month', observationdate)) AS net_change\nFROM\n    covid_19_data\nWHERE\n    observationdate BETWEEN '2019-01-01' AND '2020-12-31'\nGROUP BY\n    DATE_TRUNC('month', observationdate)\nORDER BY\n    month_start;\n")


# # <center> THE END </center>

# In[ ]:




