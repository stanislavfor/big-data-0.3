	
# MapReduce on Test Data set

## 5. Download Test Data

* 5.1 Download the Test Data File from Internet

	```
	#cd ~                   
	//command to go back to the home directory
	#mkdir test             
	//command to create new directory name test 
	#cd test                
	//command to open the test directory
	```
	```
	#wget http://content.udacity-data.com/courses/ud617/purchases.txt.gz    
	//command to download the file from Internet
 	```
	
* 5.2 Extract the Data File

	```
	#gzip -d purchases.txt.gz
	//command to extract the file
 	```
	
* 5.3 Check the Data File
        
	```
	#head -10 purchases.txt
	//command to display the first 10 lines in file
	```
	The result is 
	```
	2012-01-01	09:00	San Jose	Men's Clothing	214.05	Amex
	2012-01-01	09:00	Fort Worth	Women's Clothing	153.57	Visa
	2012-01-01	09:00	San Diego	Music	66.08	Cash
	2012-01-01	09:00	Pittsburgh	Pet Supplies	493.51	Discover
	2012-01-01	09:00	Omaha	Children's Clothing	235.63	MasterCard
	2012-01-01	09:00	Stockton	Men's Clothing	247.18	MasterCard
	2012-01-01	09:00	Austin	Cameras	379.6	Visa
	2012-01-01	09:00	New York	Consumer Electronics	296.8	Cash
	2012-01-01	09:00	Corpus Christi	Toys	25.38	Discover
	2012-01-01	09:00	Fort Worth	Toys	213.88	Visa
	```
	
## 6. Edit the Map Function and Reduce Function

* 6.1 Edit Map Function
	
	```
	#vi map.py
	//command to open the map file
	```	
 	```
	type i to insert the command
	copy the code in the map.py
	type command ESC then :wq to save the file and quit the vim file.
	```
	
	
* 6.2 Edit Reduce Function

	```
	#vi reduce.py
	//command to open the reduce file
	```
	```
	type i to insert the command
	copy the code in the reduce.py
	type command ESC then :wq to save the file and quit the vim file.
	```
	
	
* 6.3 Give the permission to running the python file
	
	```
	#chmod u+x map.py reduce.py
	//command to give the permission to running the file
	```
	```
	#ls
 	//command to display all the file 
	```
	If the file has permission, it should be in green color
	
* 6.4 Test the code in Master Container Linux

	```
	#head -10 purchases.txt | ./map.py | sort | ./reduce.py
	//command to show the first 50 element in file and use mapper and reducer to get the result
	```
	The result is 
	```
	Austin 	379.6
	Corpus Christi 	25.38
	Fort Worth 	367.45
	New York 	296.8
	Omaha 	235.63
	Pittsburgh 	493.51
	San Diego 	66.08
	San Jose 	214.05
	Stockton 	247.18
	```
	
## 7. Running MapReduce in Hadoop

* 7.1 Check the location

	```
	#cd ~
	//command go back home directory
	```
	```
	#cd test
	//command open the test directory
	```
  
* 7.2 Upload the test file to Hadoop
	
	`hadoop fs -` is the basic command for Hadoop system
  	```
	#hadoop fs -put purchases.txt input/purchases
	//command put the file to hadoop
  	```
* 7.3 Run the map and reduce to Hadoop

	```
	#hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -mapper map.py -reducer reduce.py -file map.py -file reduce.py -input input/purchases -output outputtest
	//command to do MapReduce in hadoop
	```
	
* 7.4 Check the result
	```
	#hadoop fs -ls
	//command to display directory in Hadoop system
  	```
  	```
	#hadoop fs -ls outputtest
	//command to display outputtest directory in Hadoop system
  	```
  	```
	#hadoop fs -cat outputtest/part-00000
	//command to check result for MapReduce
	```
  

	
