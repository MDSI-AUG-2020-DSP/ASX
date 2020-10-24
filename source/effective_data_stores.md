# Effective Data Stores
5 Vs of the big data is considered to determine the databased used for the project.

## Variety
The main daily ASX200 share informations are gathered from the Yahoo finance. The other data comes from different sources such as The Australian Securities Exchange (ASX), the Reserve Bank of Australia (RBA) and the Australian Bureau of Statistics (ABS). The datasets are structured and fits into tables or relational databases.  

## Velocity
The data contains historical data to date. While the real-time update is not neccessary, it is expected that the some of the data, daily ASX200 and exchange rate closing for example, will be updated on a daily basis. 

## Veracity
The most of data comes from reliables sources, such as ASX, RBA and ABS. The datasets are clean and pre-processing of the data is not required for most datasets.

 
## Volume
The currently size of the data is less than 500MB. It is expected that the size of the data will grow gradually over time.

## Value 
The project aims to provide insightful analysis of ASX related information. Most of the data, ASX200 closing and exchange rate for example, are updated daily and therefore, the ability to extract up-to-date information is crucial for the database. Combining data from different sources can help provide advanced data analysis for the project.

Based on the review of 5Vs, it is determined that the best way to store data is using the relational database management system (RDBMS) in online analytical processing (OLTP) structure. the transactions will be inserted into tables on a daily basis.

OLTP is designed to report and analyse archived structured data using complex queries. OLAP is appropriate for large volume of data which does not require frequent or real time updates. OLAP uses the traditional relational database with strict schema which provides data integrity and consistency. The tables with the database can be linked based on matching fields. The database will be stored in a data warehouse as read only so that the analysts cannot mistakenly manipulate the data. SQLite is chosen for data storage due to the ease of deployment. However, MYSQL might be a better choice as MYSQL provides multiple access and scalability and better data management with larger data.
 
Based on the review of the data, it is determined that the best way to store data is using the relational database management system (RDBMS) in Online Transactional Processing (OLTP) structure. The tables are normalised in order to improve data integrity and reduce data redundancy. The OLTP is appropriate for small volume of data which requires frequent or real time updates. The OLTP uses the traditional relational database with strict schema which provides data integrity and consistency.

The use of the RDS has advantage over storing data locally. 
Firstly, the RDS can be accessed easily by the members simultaneously. 
Secondly, the RDS is real-time which enables the real-time data analytics by the members. The data is available online and can be accessed by the members at anytime. 
Thirdsly