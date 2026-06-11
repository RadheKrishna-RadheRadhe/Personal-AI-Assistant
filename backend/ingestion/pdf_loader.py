import fitz


def extract_pages(
    pdf_path
):

    document = fitz.open(
        pdf_path
    )

    pages = []

    for page_num in range(
        len(document)
    ):

        page = document[
            page_num
        ]

        pages.append(
            {
                "page": page_num + 1,
                "text": page.get_text()
            }
        )

    document.close()

    return pages