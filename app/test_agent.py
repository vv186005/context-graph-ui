from agent import agent_answer
from graph_db import GraphDB
from vector_db import VectorDB

graph_db = GraphDB("bolt://localhost:7687", "neo4j", "abcd1234")
vector_db = VectorDB()

# NOTE: For now vector_db is empty unless you persist it (we'll fix later)

# 🔥 Add this
vector_db.add("Apple is a fruit")
vector_db.add("Microsoft is a company")
vector_db.add("Paris is the capital of France")

query = "What am I learning?"

answer = agent_answer(query, vector_db, graph_db)


answer = agent_answer(query, vector_db, graph_db)

print(answer)