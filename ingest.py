import csv
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key: str = os.getenv("OPENAI_API_KEY")

def read_from_csv_adapted(csv_path: str) -> list[Document]:
    """
    Reads the adapted CSV file and converts its content into a list of Document objects.

    :param csv_path: The path to the adapted CSV file.
    :return: A list of Document objects.
    """
    documents = []
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            doc = Document(
                page_content=row['Text'],  # Updated column name
                metadata={
                    "page_number": 1,  # Placeholder
                    "chunk": 1,  # Placeholder
                    "source": "processed_embeddings.csv",  # Placeholder
                    # Add other metadata fields if needed
                }
            )
            documents.append(doc)
    return documents

if __name__ == "__main__":
    # Step 1: Read from CSV
    csv_path_adapted = "chunkedtext.csv"  # Updated CSV file path
    document_chunks = read_from_csv_adapted(csv_path_adapted)

    # Step 3 + 4: Generate embeddings and store them in DB
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(
        document_chunks,
        embeddings,
        collection_name="html",
        persist_directory="chroma",
    )

    # Save DB locally
    vector_store.persist()

    # Number of documents in the vector store and DB written 
    print(f"Number of Document Chunks: {len(document_chunks)}")
