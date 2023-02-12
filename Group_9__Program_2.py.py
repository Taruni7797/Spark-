import sys
from pyspark import SparkContext, SparkConf
from pyspark.sql.session import SparkSession
if __name__ == "__main__":
    conf = SparkConf().setAppName("BDM")                                                                                #Configuring the spark application
    sc = SparkContext(conf=conf)                                                                                        #creating a connection to spark cluster
    spark = SparkSession.builder.appName("BDMPyspark").getOrCreate()							#Creating a SparkSession
    df = spark.read.csv('/user/kaggle/kaggle_data/marketing_campaign.csv', sep='\t', inferSchema=True, header=True)	#Reading file into a dataframe	
    res = df.groupBy("Marital_Status").avg("Income")									#Calculating the average income by marital status
    res.show()														#Printing the output
    res.coalesce(1).write.option("header","true").csv("/user/vgollap/Group_9_Program_2_output.csv")			#Writing the output into a csv file