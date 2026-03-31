from openai import OpenAI
#client = OpenAI()
client = OpenAI(api_key="key")

def retrieve_context(query, vector_db, graph_db):
    docs = vector_db.search(query)

    relation = decide_query(query)

    graph_data = graph_db.get_by_relation("Vineeta", relation)

    return {
        "docs": docs,
        "graph": graph_data,
        "relation": relation
    }

def decide_query(query):
    prompt = f"""
    Map the user query to a relation type.

    Options:
    WORKS_ON, LEARNS, USES, GOAL, WORKS_AT, STUDIES_AT

    Query: {query}

    Return only one word.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()