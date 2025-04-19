# Appendix

## Operation in Docker

* 1 Close and reconnect the Dokcer
	
	1.1 Close the Docker
	
	Every time you finish the job in Hadoop and want to close the docker. 
	Try the command:
	```
	#stop-all.sh
	//command to stop-all work in hadoop-master container
	#exit
	//command to back your local machine system
	```
	1.2 Reconnect the Docker
	
	```
	$docker exec -ti hadoop-master bash
	//command to connect hadoop-master container
	```
	After connect to the master container, you can follow the instruction in MapReduce and NLP to do the following step list in the section.
	
* 2 Check Container Status

	hadoop-master is the name for the container, you can check it by command 
	```
	$docker ps –a
	//command to list all container in your docker
	```
	How to know the which container is master or slave, check the port columns, it will give the information
	
	Check the status for each contianer
	
	If the status said: 
	
	' Exited (137) xx minutes(hours) ago' means the container is stop, you need to restart the container
	
	```
	$docker start hadoop-master
	//command to start the contianer
	```
	
* 3 Stop Container
	```
	$docker stop hadoop-master
	//command to stop for the master
	```
	```
	$docker stop hadoop-slave1
	//command to stop for the slave1
	```
	```
	$docker stop hadoop-slave2
	//command to stop for the slave2
	```

* 4 Start Container
	```
	$docker start hadoop-master
	//command to start for the msater
	```
	```
	$docker start hadoop-slave1
	//command to start for the slave1
	```
	```
	$docker start hadoop-slave2
	//command to start for the slave2
	```
	
* 5 Connect Container

	```
	$docker exec -ti hadoop-master bash
	//command to connect bash system for the master
	```
	```
	$docker exec -ti hadoop-slave1 bash
	//command to connect bash system for the slave1
	```
	```
	$docker exec -ti hadoop-slave2 bash
	//command to connect bash system for the slave2
	```
  
