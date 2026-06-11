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
        query,
        top_k=3
    ):

        query_embedding = (
            self.embedder
            .generate_embeddings([query])[0]
        )

        _, indices = (
            self.vector_store.search(
                query_embedding,
                top_k
            )
        )

        results = []

        for idx in indices[0]:

            if idx < len(self.chunks):

                results.append(
                    self.chunks[idx]
                )

        return results