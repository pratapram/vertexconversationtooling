# vertexconversationtooling
vertexconversationtooling

This repository shows how to create custom tools using cloudrun.

## Steps
### 1 Create an Agent using Agent Builder in GCP Vertex AI 
### 2 Create a cloudrun service
Cloudrun is a serverless fully managed platform to host your web application. In this case we will create a REST endpoint. To do this

2.1 Clone this repository in your workspace

2.2 "cd cloudrun"

2.3 Modify the main.py to your projectid

2.4 This cloudrun service runs a query on bigquery and returns the result. So modify the bigquery query to suit your needs. (The dataset is not provided here)

2.5 run "gcloud run deploy" . This will take package the code into a container and deploy it. You need to have cloudrun permissions to deploy this code as a service. Once successful, you can hit the url provided by cloudrun to test if it works


### 3 Create a new tool

3.1 Go to the Agent in Agent Buidler

3.2 Create a new tool 

3.3 Copy the swagger.json provided from this repository into the tool. Modify it as necessary to suit your needs. Click save

3.4 Use the tool in the Agent prompt.







