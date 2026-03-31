from ingestion import ingest
from graph_db import GraphDB
from vector_db import VectorDB

# Initialize DBs
graph_db = GraphDB("bolt://localhost:7687", "neo4j", "abcd1234")
vector_db = VectorDB()

texts = [
    "I am working on an Entity Resolution project using PySpark",
    "I am learning Apache Airflow for orchestration",
    "My goal is to become a Senior Data Architect/Manager",
    "I am currently a Senior Data Engineer at Ford",
    "I am learning about AI agents and LLMs",
    "I want to improve my leadership and stakeholder management skills",
    "I am working with BigQuery and PySpark for large datasets",
    "I am enrolled in IIM Senior Management Program",
]

for text in texts:
    ingest(text, graph_db, vector_db)

print("✅ Ingestion complete")