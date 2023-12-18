# googleapi-airflow-project
To use googleapi to fetch youtube data perform preprocessing and then orchestrate the job on Apache Airflow

**AWS Setup**

* Create an EC2 instance and S3 bucket in AWS and then provide mutual read and write access to them.
* ssh into cmd using following command
    ssh -i "sample.pem" user@public_ipv4_dns_name
* install and update necessary libraries and modules
  1 sudo apt install python3-pip3 // to install pip
  2 sudo apt-get update // to update all the packages 
  3 sudo pip install apache-airflow // to install apache airflow using pip
  4 sudo pip install pandas // install pandas library for preprocessing and data manipulation
  5 sudo pip install s3fs // install s3 file system library to conveniently upload files to s3 bucket
  6 sudo pip install google-api-python-client // to import googleapiclient.discovery module to make api calls
* after installing airflow there will be airflow folder autocreated. In this folder create another folder youtube_dag and create 2 new files googleapi.py and youtube_dag.py
* In airflow folder go to airflow.cfg file and edit the dag_folder path to the youtube_dag folder.
* in googleapi.py file provide the api_service_name, version and developer_key from GOOGLE API website.
* Create the object or googleapiclient.discovery module and make a get request giving 2 parameters(part and videoid).
* Capture the response and do the preprocess the data using pandas. Output the data in CSV format or JSON file into s3 bucket.
* The youtube_dag.py file creates the DAG by provding necessary metadata. This file internally refers the youtubeETL function inside googleapi.py file. We create PythonOperator object to run the etl job.
* We run the airflow webserver using either "airflow webserver" / "airflow standalone" . login into it and we'll find our dag in dag list. we can run the dag and schedule them according to out needs.
  
