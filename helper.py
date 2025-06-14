import os
import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import AzureOpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def split_text_into_chunks(text, chunk_size=1000, overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )
    chunks = splitter.split_text(text)
    return chunks

def create_faiss_index(chunks):
    embeddings = AzureOpenAIEmbeddings(
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZUREOPENAI_API_BASE"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    deployment=os.getenv("Embedding_AZURE_OPENAI_DEPLOYMENT_NAME"),
    chunk_size=1000,
    validate_base_url=False  # ✅ this is the fix
)

    vectorstore = FAISS.from_texts(chunks, embedding=embeddings)
    return vectorstore.as_retriever()

