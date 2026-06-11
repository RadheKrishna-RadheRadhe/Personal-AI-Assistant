class Retriever:

    def __init__(
        self,
        vector_store,
        chunks,
        embedder
    ):

        self.vector_store = vector_store
        self.chunks = chunks
        self.embedder = embedder

    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ):

        query_embedding = (
            self.embedder.generate_query_embedding(
                query
            )
        )

        distances, indices = (
            self.vector_store.search(
                query_embedding,
                top_k
            )
        )

        results = []

        for score, idx in zip(
            distances[0],
            indices[0]
        ):

            if (
                idx >= 0
                and idx < len(self.chunks)
            ):

                chunk = self.chunks[idx]

                results.append(
                    {
                        "text": chunk["text"],
                        "source": chunk["source"],
                        "page": chunk["page"],
                        "chunk_id": chunk["chunk_id"],
                        "score": float(score)
                    }
                )

        return results