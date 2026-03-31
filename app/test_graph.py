from graph_db import GraphDB

graph_db = GraphDB("bolt://localhost:7687", "neo4j", "abcd1234")

result = graph_db.get_related_entities("Vineeta")

print(result)