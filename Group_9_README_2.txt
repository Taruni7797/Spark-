BDM Group_9__Program_2:

Steps to Run a spark Application written in Python: 
1. Login with your CSX username and password 
2. Run the python file using spark-submit command: 
Command:  spark-submit  pathtoPythonFile/pythonFile.py 
Ex: spark-submit Group_9__Program_2.py 
3. Output will be printed on the console and written into file as well
4. Checking the output file
Command: hdfs dfs -ls outputpath/outputfilename/part-r-00000
Ex: hdfs dfs -ls /user/vgollap/Group_9_Program_2_output.csv/part-00000-370cc613-7053-4fef-92cc-0cbf782ec4c9-c000.csv 
5. Checking the output 
Command: hdfs dfs -cat outputpath/outputfilename/part-r-00000 
Ex: hdfs dfs -cat /user/vgollap/Group_9_Program_2_output.csv/part-00000-370cc613-7053-4fef-92cc-0cbf782ec4c9-c000.csv 