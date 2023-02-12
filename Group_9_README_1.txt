BDM Group_9__Program_1:

Task 1: Steps to Run Spark SQL using scala: 
1. Login to the cluster with credentials (CSX username and password)
2. Run the command to start spark session. It will open up the shell
Command:  spark-shell 
3. Compile and execute the .scala file using the command:
Command: load filepath
Ex: load /home/ssamine/Group_9__Program_1.scala
4. Output will be printed on the console and written into file as well 
Note: Output filename should be changed everytime.
5. Exit the scala screen( ctrl+Z) and it will go back to hadoop.
6.Checking the output file
Command: hdfs dfs -ls outputpath/outputfilename/part-r-00000
Ex:  hdfs dfs -ls /user/ssamine/sparksql_task_1.csv/part-00000-408205aa-ff4c-4fdc-922c-52e0e9d38285-c000.csv 
7. For viewing output
hdfs dfs -cat outputpath/outputfilename/part-r-00000 
Ex: hdfs dfs -cat /user/ssamine/sparksql_task_1.csv/part-00000-408205aa-ff4c-4fdc-922c-52e0e9d3828-c000.csv