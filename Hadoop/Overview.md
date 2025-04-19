# Overview 

#### Apache Hadoop

Apache Hadoop is an open source software framework. It provides a distributed environment for storing and processing the data. It provides the ability to scale from one single machine to clusters of computers. The two modules leveraged in this tutorial are Hadoop Distributed File System(HDFS) and Hadoop MapReduce. HDFS gives the fast speed for data access. And MapReduce is a YARN based system for parallel processing. Therefore it meets up with the need for the big data processing. 

#### HDFS

HDFS is a highly fault tolerence file system and it is designed for commodity use. The main architecture includes namenode, datanode and block. Namenode acts as the matser server. It manages the file system namespace. The datanode manages the data storage. And each file is divided into certain number of blocks. Each block contains a piece of information.

![hdfsarchitecture](https://user-images.githubusercontent.com/33606250/34073944-694f72e0-e273-11e7-98e9-a4d40a3dada1.gif)
Reference:https://user-images.githubusercontent.com/33606250/34073944-694f72e0-e273-11e7-98e9-a4d40a3dada1.gif

#### MapReduce

MapReduce is a technique for distributed computing. Two main tasks are contained here: Map and Reduce. The Map comes before Reduce. Map basically converts a dataset to a set of data containing tuples(key/value) of single element. After Map finishes its job. Reduce takes the output to combine them into smaller number of tuples.

![199q1](https://user-images.githubusercontent.com/26347639/34073857-a2c31b50-e271-11e7-930c-af160e74a461.png)
Reference:https://user-images.githubusercontent.com/26347639/34073857-a2c31b50-e271-11e7-930c-af160e74a461.png

#### Docker

Docker is a software providing the containers. It can help local computer set up the virtual environment. To our project specifically, it is used to take a certain percent of CPU and space from the local computer to set up one master and two slaves. It also provides the Linux running environment for Hadoop. 






