# vertexconversationtooling
vertexconversationtooling

This repository shows how to create custom tool to be used in VertexAI Agent Builder. The "tool" here is a cloudrun service, that can be accessed through REST API. In this specific example, the tool expects a "doc_id" and retrieves a "summary" text from a bigquery table. The bigquery table is not provided in this repository, and you can see the query that is run in the cloudrun/main.py file.

## Steps
### 1 Create an Agent using Agent Builder in GCP Vertex AI 

![Creating an agent](https://github.com/pratapram/vertexconversationtooling/blob/main/agent.jpeg)

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

