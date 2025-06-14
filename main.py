import os
import streamlit as st
from dotenv import load_dotenv
from helper import extract_text_from_pdf, split_text_into_chunks, create_faiss_index
from langchain.chains import RetrievalQA
from langchain.chat_models import AzureChatOpenAI

# Load environment variables
load_dotenv()

st.title("🧠 RAG-Based MCQ Generator")

uploaded_file = st.file_uploader("📄 Upload a GenAI-related PDF", type="pdf")

if uploaded_file:
    # Save the file to disk
    file_path = os.path.join("uploaded", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("✅ PDF uploaded successfully!")

    # Extract, chunk and index
    with st.spinner("🔍 Processing PDF..."):
        raw_text = extract_text_from_pdf(file_path)
        chunks = split_text_into_chunks(raw_text)
        retriever = create_faiss_index(chunks)

        # Set up Azure OpenAI model
        llm = AzureChatOpenAI(
            azure_endpoint=os.getenv("AZUREOPENAI_API_BASE"),  # changed line
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            model_name="gpt-4o",
            temperature=0.5,
            validate_base_url=False  # same fix as embeddings
    )


        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

        # Generate MCQs
        mcq_prompt = """
        Based on this content, generate 5 multiple choice questions about Generative AI.
        Each question should have 4 options and mention the correct answer.
        """
        mcq_output = qa_chain.run(mcq_prompt)

        # Generate Short Answer Questions
        short_prompt = """
        Generate 5 short answer questions related to Generative AI based on this content.
        Each question should be clear and answerable in 2–3 lines.
        """
        short_output = qa_chain.run(short_prompt)

    st.header("📘 Multiple Choice Questions")
    st.write(mcq_output)

    st.header("✍️ Short Answer Questions")
    st.write(short_output)
