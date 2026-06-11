from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


class TextChunker:

    def __init__(
        self,
        chunk_size=1000,
        chunk_overlap=200
    ):

        self.splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                separators=[
                    "\n\n",
                    "\n",
                    ". ",
                    " ",
                    ""
                ]
            )
        )

    def chunk_text(
        self,
        text: str
    ):

        if not text.strip():
            return []

        chunks = (
            self.splitter.split_text(
                text
            )
        )

        return [
            chunk.strip()
            for chunk in chunks
            if chunk.strip()
        ]