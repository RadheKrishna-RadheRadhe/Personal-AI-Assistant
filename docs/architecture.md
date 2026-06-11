# System Architecture

## High-Level Flow

User Documents
    ↓
Document Ingestion
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Retriever
    ↓
LLM
    ↓
Cited Response

## Components

### Ingestion Layer

Responsible for:

- PDF processing
- TXT processing
- DOCX processing (future)

### Processing Layer

Responsible for:

- Cleaning text
- Chunking
- Metadata extraction

### Embedding Layer

Converts text into vector representations.

Model:

BAAI/bge-small-en-v1.5

### Storage Layer

Vector Database:

FAISS

Metadata Database:

SQLite

### Retrieval Layer

Performs semantic search.

### Generation Layer

Uses local LLM through Ollama.

### User Interface

Streamlit chat application.
