# 🧠 RAG-based MCQ Generator

Generate Multiple Choice Questions and Short Answer Questions from GenAI-related PDFs using Retrieval-Augmented Generation.

## 🚀 Features

- 📄 Upload any GenAI-related PDF
- 🧩 Extract content and chunk it
- 🧠 Store embeddings in FAISS
- 🤖 Use LangChain + Azure OpenAI to:
  - Generate 5 MCQs (with options and answers)
  - Generate 5 Short Answer Questions
- 🎯 Output everything in a Streamlit interface

## 🔧 Tech Stack

- [LangChain](https://www.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Azure OpenAI](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service/)
- [Streamlit](https://streamlit.io/)

## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rag-mcq-generator.git
   cd rag-mcq-generator


2. Install dependencies:

pip install -r requirements.txt


3. Add your Azure API keys in a .env file:

AZURE_OPENAI_API_KEY=your_key_here
AZUREOPENAI_API_BASE=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_API_VERSION=yourversion

4. Run the app:

streamlit run app.py



📌 Example Output

Q: What is the capital of France?
A) Berlin
B) Madrid
C) Paris ✅
D) Rome


📜 License
This project is licensed under the MIT License — feel free to use, modify, and share.

👩‍💻 Made with ❤️ by Mahek Kaul
