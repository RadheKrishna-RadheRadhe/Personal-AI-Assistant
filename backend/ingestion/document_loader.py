import os

from ingestion.pdf_loader import (
    extract_pages
)


def load_documents(
    documents_folder
):

    all_pages = []

    pdf_files = [
        file
        for file in os.listdir(
            documents_folder
        )
        if file.endswith(".pdf")
    ]

    for pdf_file in pdf_files:

        pdf_path = os.path.join(
            documents_folder,
            pdf_file
        )

        pages = extract_pages(
            pdf_path
        )

        for page in pages:

            page["source"] = pdf_file

            all_pages.append(
                page
            )

    return all_pages