from ingestion.document_loader import (
    load_documents
)

from ingestion.document_processor import (
    DocumentProcessor
)

from embeddings.embedder import (
    EmbeddingGenerator
)

from vector_store.faiss_store import (
    FAISSStore
)

from retrieval.retriever import (
    Retriever
)

from llm.generator import (
    AnswerGenerator
)


DOCUMENT_FOLDER = "documents"


def main():

    print("\nLoading Documents...\n")

    # Load all PDFs
    pages = load_documents(
        DOCUMENT_FOLDER
    )

    print(
        f"Total Pages Loaded: {len(pages)}"
    )

    # Process pages into chunks
    processor = DocumentProcessor()

    chunks = processor.process_pages(
        pages
    )

    print(
        f"Total Chunks: {len(chunks)}"
    )

    print(
        "\nGenerating embeddings..."
    )

    # Generate embeddings
    embedder = EmbeddingGenerator()

    embeddings = (
        embedder.generate_embeddings(
            chunks
        )
    )

    # Create vector store
    dimension = len(
        embeddings[0]
    )

    vector_store = FAISSStore(
        dimension
    )

    vector_store.add_embeddings(
        embeddings
    )

    print(
        "Vector database ready."
    )

    # Retriever
    retriever = Retriever(
        vector_store,
        chunks,
        embedder
    )

    # LLM
    generator = AnswerGenerator()

    print(
        "\nPersonal AI Knowledge Assistant Ready."
    )

    print(
        "Type 'exit' to quit."
    )

    while True:

        query = input(
            "\nAsk Question: "
        ).strip()

        if not query:
            continue

        if query.lower() == "exit":
            break

        # Retrieve
        results = retriever.retrieve(
            query,
            top_k=3
        )

        # Generate answer
        answer = (
            generator.generate_answer(
                query,
                results
            )
        )

        print("\n" + "=" * 80)
        print("ANSWER")
        print("=" * 80)

        print(answer)

        print("\n" + "=" * 80)
        print("SOURCES")
        print("=" * 80)

        for i, result in enumerate(
            results,
            start=1
        ):

            print(
                f"\n[{i}] "
                f"{result['source']}"
            )

            print(
                f"Page: {result['page']}"
            )

            print(
                f"Similarity Score: "
                f"{result['score']:.4f}"
            )

            preview = (
                result["text"]
                .replace("\n", " ")
                [:150]
            )

            print(
                f"Preview: {preview}..."
            )

        # Debug mode
        debug = False

        if debug:

            print("\n" + "=" * 80)
            print("RETRIEVED CHUNKS")
            print("=" * 80)

            for i, result in enumerate(
                results,
                start=1
            ):

                print(
                    f"\nResult {i}"
                )

                print(
                    "-" * 50
                )

                print(
                    f"Source: {result['source']}"
                )

                print(
                    f"Page: {result['page']}"
                )

                print(
                    f"Chunk ID: {result['chunk_id']}"
                )

                print(
                    f"Score: {result['score']:.4f}"
                )

                print("\nText:\n")

                print(
                    result["text"]
                )


if __name__ == "__main__":
    main()