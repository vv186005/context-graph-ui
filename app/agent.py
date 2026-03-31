from openai import OpenAI
from retrieval import retrieve_context

client = OpenAI(api_key="key")

def agent_answer(query, vector_db, graph_db):
    context = retrieve_context(query, vector_db, graph_db)

    print("\n📊 GRAPH DATA:", context["graph"])
    print("\n📄 VECTOR DOCS:", context["docs"])

    prompt = f"""
    Answer using the context below.

    Graph Data:
    {context['graph']}

    Documents:
    {context['docs']}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content