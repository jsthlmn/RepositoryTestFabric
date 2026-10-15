# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "7147a381-03cc-4014-a52e-fa1383788a29",
# META       "default_lakehouse_name": "DEV_LH_Hilman",
# META       "default_lakehouse_workspace_id": "0541636a-e0e1-4ebb-968c-bfd0455d44a3",
# META       "known_lakehouses": [
# META         {
# META           "id": "bc08fcca-d850-4094-87c5-26becf044b72"
# META         },
# META         {
# META           "id": "7147a381-03cc-4014-a52e-fa1383788a29"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

spark.sparkContext.addPyFile("/lakehouse/default/Files/Library/library_test.py") # Read python file

from library_test import *

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import current_timestamp, from_utc_timestamp

# Create dummy Pandas DataFrame
df = pd.DataFrame({
    "EmployeeID": [1, 2, 3, 4, 5],
    "EmployeeName": ["Andi", "Budi", "Citra", "Dewi", "Eko"],
    "Department": ["IT", "Finance", "HR", "IT", "Data"],
    "Salary": [8000000, 7500000, 6500000, 9000000, 8500000]
})

# Convert Pandas DataFrame to Spark DataFrame
spark_df = spark.createDataFrame(df)

# Add load timestamp in Jakarta time (GMT+7)
spark_df = spark_df.withColumn(
    "LoadTimeStamp",
    from_utc_timestamp(current_timestamp(), "Asia/Jakarta")
)

# Write to Fabric Lakehouse table
spark_df.write.format("delta").mode("overwrite").saveAsTable(
    "test_schema.DimEmployee"
)

# Verify the result
spark.sql("SELECT * FROM test_schema.DimEmployee").show(truncate=False)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# test

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# test 2

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# test3

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# test4

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
