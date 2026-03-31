from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

class VectorDB:
    def __init__(self, path="vector_store"):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.path = path
        self.index = None
        self.texts = []

        if os.path.exists(path):
            self.load()

    def add(self, text):
        emb = self.model.encode([text])

        if self.index is None:
            self.index = faiss.IndexFlatL2(len(emb[0]))

        self.index.add(np.array(emb))
        self.texts.append(text)

        self.save()

    def search(self, query, k=3):
        if self.index is None:
            return []

        q_emb = self.model.encode([query])
        D, I = self.index.search(np.array(q_emb), k)
        return [self.texts[i] for i in I[0]]

    def save(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        faiss.write_index(self.index, f"{self.path}/index.faiss")

        with open(f"{self.path}/texts.pkl", "wb") as f:
            pickle.dump(self.texts, f)

    def load(self):
        self.index = faiss.read_index(f"{self.path}/index.faiss")

        with open(f"{self.path}/texts.pkl", "rb") as f:
            self.texts = pickle.load(f)