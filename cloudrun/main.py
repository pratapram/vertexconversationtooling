# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
from google.cloud import bigquery


app = Flask(__name__)

PROJECT_ID = os.getenv("myprojectid")
DATASET_ID = "MyDATASETID" 
TABLE_ID = "documents" 

client = bigquery.Client(project=PROJECT_ID)
table_ref = client.dataset(DATASET_ID).table(TABLE_ID)
table = client.get_table(table_ref)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"


@app.route('/summarize', methods=['POST'])
def get_summary():
    try:
        data = request.get_json()
        if 'document_id' not in data:
            raise BadRequest('Missing document_id')

        document_id = data['document_id']

        query = f"SELECT summary_paragraph FROM `{DATASET_ID}.{TABLE_ID}` WHERE document_id={document_id}"
        print (query)
        query_job = client.query(query)
        results = ["".join(row) for row in query_job]
        #results = query_job['summary_paragraph']

        summary = f" {results}"
        if summary:
            return jsonify({"summary": summary})
        else:
            return jsonify({"error": "Document not found or could not be summarized"}), 404

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Log the error for debugging
        print(f"Error summarizing document: {e}") 
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
