from ingestion.text_chunker import (
    TextChunker
)


class DocumentProcessor:

    def __init__(self):

        self.chunker = (
            TextChunker()
        )

    def process_pages(
        self,
        pages
    ):

        chunks = []

        chunk_id = 0

        for page_data in pages:

            page_num = (
                page_data["page"]
            )

            source = (
                page_data["source"]
            )

            page_text = (
                page_data["text"]
            )

            split_chunks = (
                self.chunker.chunk_text(
                    page_text
                )
            )

            for chunk in split_chunks:

                chunks.append(
                    {
                        "text": chunk,
                        "source": source,
                        "page": page_num,
                        "chunk_id": chunk_id
                    }
                )

                chunk_id += 1

        return chunks