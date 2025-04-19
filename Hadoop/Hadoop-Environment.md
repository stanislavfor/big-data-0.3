# Set up Enviroment
Even though we have already finished install the hadoop images, there are still a lot of work to set up our environment in order to get the necessary software and packages for future running.
## 3. Update Image 

* 3.1 Connect the Image

	```
	$docker run -ti --name hadoop kiwenlau/hadoop:1.0
	//command to run the kiwenlau images
	```
	Due to the Hadoop image is out of date, we need to do some update to set up the environment for our project.
	
* 3.2 Update Image

	3.2.1 Install apt-get
	
	The Advanced Package Tool, or APT, is a free software user interface that works with core libraries to handle the installation and removal of software on Debian and other Linux distributions
	
	Reference: https://en.wikipedia.org/wiki/APT_(Debian)
	```
	#apt-get update
 	//command to update the apt-get
	```
	
	3.2.2 Install Vim

	Vim is the editor for Linux System. 
	```
	#apt-get install vim
	//command to install vim
 	```
	Press `Y` in keyboard when command line display
	```
	Do you want to continue? [Y/n]
	```

	3.2.3 Install Python3
	
	Python is the programming language for our project.
   	```
   	#apt install  python3
   	//command to download Python package
   	```
	
	3.2.4 Install pip
	
	pip is a package management system used to install and manage software packages written in Python. 
	
	Reference https://en.wikipedia.org/wiki/Pip_(package_manager)
	```
	#wget https://bootstrap.pypa.io/get-pip.py
	//command to download get-pip.py file
	#python get-pip.py
	//command to install get-pip.py
	```
	
	3.2.5 Install Numpy
	
	NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
	
	Reference https://en.wikipedia.org/wiki/NumPy
	```
	#pip install numpy
	//command to install numpy
	```
	
	3.2.6 Install Pandas
	
	Pandas is a software library written for the Python programming language for data manipulation and analysis.
	
	Reference https://en.wikipedia.org/wiki/Pandas_(software)
	```
	#pip install pandas
	//command to install pandas
	```
	
	3.2.7 Install Sklearn
	
	Scikit-learn is a free software machine learning library for the Python programming language.
	
	Reference https://en.wikipedia.org/wiki/Scikit-learn
	```
	#pip install Sklearn
	//command to install sklearn
	```
	
	3.2.8 Install Scipy
	
	SciPy is an open source Python library used for scientific computing and technical computing.
	
	Reference https://en.wikipedia.org/wiki/SciPy
	```
	#pip install Scipy
	//command to install scipy
	```
	
	3.2.9 Install vader.sentiment
	
	VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. 
	
	Reference https://github.com/cjhutto/vaderSentiment
	```
	#pip install vaderSentiment
	//command to install vaderSentiment
	```
	3.2.10 Install jupyter
	
	```
	#apt-get install build-essential python-dev
	//required function
	```
	
	And then install the jupyter
	```
	#pip install jupyter
	//command to install scipy
	```
	

## 4. Create new Hadoop Image

* 4.1 Creat new Hadoop Image

	```
	#exit
	//command to get out of bash 
	```
	```
	$docker commit hadoop hadoop:python
	//command to create docker image based on hadoop he used
	```
	
* 4.2 Restart Hadoop container

	```
	$cd hadoop
	//command to find the hadoop file which we download from github
	$cd CODE
	//command to get CODE file
	$ vi start-container.sh
	//command to check code
	```
	If the start-container.sh is empty, copy the file named start-container.sh in the github
	```
	$chmod u+x start-container.sh
	//command to give the permission to run 
	$./start-container.sh
	//command to run the image and create the container
	```

* 4.3 Start Hadoop

	After type command `./start-container.sh`, you already in the linux system
	```
	#./start-hadoop.sh
	//command to run hadoop
	```
	
* 4.4 Word-count in Hadoop

	Thanks to kiwenlau. He has already given us a test code for testing the hadoop environment
	```
	#./run-wordcount.sh
	//command to run wordcount
	```
	Your result should be the same with the result listed below:
	```
	input file1.txt:
	Hello Hadoop

	input file2.txt:
	Hello Docker

	wordcount output:
	Docker	1
	Hadoop	1
	Hello	2
	```
