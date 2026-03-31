from neo4j import GraphDatabase

class GraphDB:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def add_relation(self, subject, relation, obj):
        query = """
        MERGE (a:Entity {name: $subject})
        MERGE (b:Entity {name: $object})
        MERGE (a)-[:RELATION {type: $relation}]->(b)
        """
        with self.driver.session() as session:
            session.run(query, subject=subject, object=obj, relation=relation)

    def get_related_entities(self, entity):
        query = """
        MATCH (a {name: $entity})-[r]->(b)
        RETURN a.name AS source, r.type AS relation, b.name AS target
        """
        with self.driver.session() as session:
            result = session.run(query, entity=entity)
            return [dict(record) for record in result]

    def get_by_relation(self, entity, relation):
        query = """
        MATCH (a {name: $entity})-[r]->(b)
        WHERE r.type = $relation
        RETURN b.name AS result
        """
        with self.driver.session() as session:
            result = session.run(query, entity=entity, relation=relation)
            return [record["result"] for record in result]

    def get_skills(self, person="Vineeta"):
        query = """
        MATCH (a {name: $person})-[r]->(b)
        WHERE r.type = "Has_Skill" OR r.type = "Used_Tool"
        RETURN DISTINCT b.name AS skill
        """
        with self.driver.session() as session:
            result = session.run(query, person=person)
            return [record["skill"] for record in result]