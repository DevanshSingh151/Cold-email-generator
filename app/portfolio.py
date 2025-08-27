
import pandas as pd
import chromadb
import uuid
import os


class Portfolio:
    def __init__(self, file_path="app/resource/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        # Initialize ChromaDB with fallback to handle corrupted configs
        self.vector_path = 'vectorstore'
        self.chroma_client = chromadb.PersistentClient(self.vector_path)
        try:
            self.collection = self.chroma_client.get_or_create_collection(name="portfolio")
        except Exception:
            # Fallback client and unique collection to avoid corrupted state
            fallback_path = 'vectorstore_fallback'
            self.chroma_client = chromadb.PersistentClient(fallback_path)
            self.collection = self.chroma_client.get_or_create_collection(name=f"portfolio_{uuid.uuid4().hex[:6]}")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                documents = [str(row["Techstack"])]
                metadatas = [{"links": str(row["Links"])}]
                ids = [str(uuid.uuid4())]
                self.collection.add(documents=documents, metadatas=metadatas, ids=ids)

    def query_links(self, skills):
        if not skills:
            return []
        query_texts = [skills] if isinstance(skills, str) else list(skills)
        try:
            result = self.collection.query(query_texts=query_texts, n_results=2)
            return result.get('metadatas', [])
        except Exception:
            return []
