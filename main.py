from bigquery_helper import create_bigquery_agent
import vertexai

VERTEX_PROJECT_ID = "hacking-dec-7-2024"
BIGQUERY_PROJECT_ID = "trim-field-444020-g8"
REGION = "us-west1"
DATASET_ID = "todo_demo"
TABLE_ID = "tasks"
MODEL_NAME = "gemini-1.5-flash-002"

# Initialize Vertex AI with the gcp_project_id and location
vertexai.init(project="hacking-dec-7-2024", location="us-west1")

todo_agent = create_bigquery_agent(
    bigquery_project_id=BIGQUERY_PROJECT_ID,
    dataset_id=DATASET_ID,
    table_id=TABLE_ID,
    model_name=MODEL_NAME
)

# Interact with the agent
response = todo_agent.send_message(
    "Show me all todos from the database"
)[0]

print(response)
