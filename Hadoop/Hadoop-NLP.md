# Nature Language Processing on Amazon Review

#### In this part, we want to predict the rating value (overall) based on the new review coming into our dataset.

## 8. Download Amazon Review 

* 8.1 Review Amazon Review Website  

   This dataset contains product reviews and metadata from Amazon, including 142.8 million reviews spanning May 1996 - July 2014.
   
   Website: http://jmcauley.ucsd.edu/data/amazon/
    
   The link for amazon review file
   
   http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/ 'filename' .json.gz
    
   File name is the file you want to download
   
   For example:
   
   Review Kindle store:
   http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Kindle_Store_5.json.gz
   
* 8.2 Download Amazon Review file 
    
   Make sure you are in Hadoop-Master bash
   
   ```
   #cd ~
   //command to go back home directory
   #mkdir NLP
   //command to create new directory for Nature Language Process
   #cd NLP
   //command to change directory
   ``` 
   For this project, we will use Health_and_Personal_Care_5.json as our dataset.
   ```
   #wget http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Health_and_Personal_Care_5.json.gz
   //command to download the file
   ```
   
* 8.3 Extract the file

	```
	#gzip -d reviews_Health_and_Personal_Care_5.json.gz 
	//command to extract the file
	```
	
## 9. Edit the Map Function and Reduce Function

* 9.1 Edit Map Function

	```
	#vi map_NLP.py
	//command to open the map file
	```
	```
	type i to insert the command
	copy the code in the map_NLP.py
	type command ESC then :wq save the file and quit the vim file.
	```
	
* 9.2 Edit Reduce Function

	```
	#vi reduce_NLP.py
	//command to open the reduce file
	```
	```
	type i to insert the command
	copy the code in the reduce_NLP.py
	type command ESC then :wq to save the file and quit the vim file.
	```	
	
* 9.3 Give the permission to running the python file
	
	```
	#chmod u+x map_NLP.py reduce_NLP.py
	//command to give the permission to running the file
	```
	```
	#ls
 	//command to display all the file 
	```
	If the file has permission, it should be in green color
	
* 9.4 Test the code in Master Container Linux

	```
	#head -n 15000 reviews_Health_and_Personal_Care_5.json | ./map_NLP.py | sort | ./reduce_NLP.py
	//command to show the first 50 element in file and use mapper and reducer to get the result
	```
	Check the `n value` in reduce_NLP.py.
	
	In order to run the test code, the command head -n `number` the number should be bigger than the n value in the reduce_NLP.py 
	
	
## 10. Running MapReduce_NLP in Hadoop

After doing the test, we need to replace the `n value` in the reduce_NLP.py back to the default value.

* 10.1 Check the location

	```
	cd ~/NLP
	//command to change the directory
	```
	
* 10.2 Upload the test file to Hadoop
	
	`hadoop fs -` is the basic command for Hadoop system
	```
	#hadoop fs -put reviews_Health_and_Personal_Care_5.json input
	//command to input the file to hadoop 
  	```
	
* 10.3 Upload the map and reduce to Hadoop
	```
	#cd ~/NLP
	//command to open the NLP directory
	```
	```
	#hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -mapper map_NLP.py -reducer reduce_NLP.py -file map_NLP.py -file reduce_NLP.py -input input/reviews_Health_and_Personal_Care_5.json -output NLP_Result
	//command to do MapReduce in hadoop
	```
* 10.4 Check the result
	```
	#hadoop fs -ls
	//command to display directory in Hadoop system
  	```
  	```
	#hadoop fs -ls NLP_Result
	//command to display NLP_Result directory in Hadoop system
  	```
  	```
	#hadoop fs -cat NLP_Result/part-00000
	//command to check result for MapReduce
	```
	
	
## 11. Running MapReduce_NLP_2 in Hadoop

We provide another solution to do the sentiment analysis, which could get higher accuracy but longer running time.

* 11.1 Split the traning set from your whole data set

	```
	#cd ~/NLP
	head -n 50000 reviews_Health_and_Personal_Care_5.json > train
	//command to take first 50000 rows as training data
	```
	
* 11.2 Copy our CODE/map_NLP_2.py and  reduce_NLP_2.py to your testing(current) directory
       Just similar what you did in step 9.1 and 9.2

	
* 11.3 Upload the map and reduce to Hadoop
	```
	#cd ~/NLP
	//command to open the NLP directory
	```
	```
	#hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -mapper map_NLP_2.py -reducer reduce_NLP_2.py -file map_NLP_2.py -file reduce_NLP_2.py -file train -input input/reviews_Health_and_Personal_Care_5.json -output NLP2_Result
	//command to do MapReduce in hadoop
	```
* 11.4 Check the result

  	```
	#hadoop fs -cat NLP2_Result/part-00000
	//command to check result for MapReduce
	```


