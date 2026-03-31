from graph_db import GraphDB

graph_db = GraphDB("bolt://localhost:7687", "neo4j", "abcd1234")

skills = graph_db.get_skills()

print("💡 Skills:", skills)