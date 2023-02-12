import org.apache.spark.sql.SparkSession 
val spark = SparkSession.builder().appName("Spark SQL").config("spark.some.config.option", "some-value").getOrCreate()                           //creating a sparksession
val df=spark.read.format("csv").option("header","true").option("delimiter", "\t").load("/user/kaggle/kaggle_data/marketing_campaign.csv");       //reading the input csv file using \t as delimiter
df.createOrReplaceTempView("people")                                                                                                             //for creating or replacing temp view
val sqlDF = spark.sql("Select Marital_Status,avg(Income) as Income from people group by Marital_Status")                                         //calculating the average income by marital status using sql
sqlDF.show()                                                                                                                                     //printing the output on console
sqlDF.coalesce(1).write.option("header","true").csv("/user/ssamine/spark_task_1.csv")                                                             // writing the output into a csv file






