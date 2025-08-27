## 📧 Cold Email Generation Tool

Generate tailored cold emails from job postings with portfolio links, powered by LangChain + Groq and a ChromaDB-backed portfolio index. Built with Streamlit.

### ✨ Features
- Extracts roles, experience, skills, and description from a job/careers URL
- Generates a polished, personalized email using Groq `llama-3.1-8b-instant`
- Matches your portfolio links from a local ChromaDB vector store
- Clean, interactive UI with a dark blue‑violet theme

### 🧰 Tech Stack
- Python, Streamlit
- LangChain, `langchain-groq`
- ChromaDB (local persistent vector store)
- pandas, dotenv

---

## 🚀 Getting Started

### 1) Clone the repo
```bash
git clone https://github.com/<your-username>/cold-email-generation-tool.git
cd cold-email-generation-tool
```

### 2) Python version
- Python 3.10 or 3.11 is recommended

### 3) Create and activate a virtual environment
```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 4) Install dependencies
```bash
pip install -r requirements.txt
```

### 5) Configure environment
Create a `.env` based on `.env.example`:
```
GROQ_API_KEY=your_groq_api_key
```

### 6) Run the app
```bash
streamlit run app/main.py
```

Open your browser at the shown URL. Paste a job/careers URL and click Generate.

---

## 📁 Project Structure
```
app/
  main.py          # Streamlit UI entry
  chains.py        # LangChain prompts + Groq chat wrapper
  portfolio.py     # ChromaDB client + simple query layer
  utils.py         # Text cleanup
  resource/
    my_portfolio.csv  # Your portfolio links + tech stack mapping
vectorstore/       # ChromaDB persistence (auto-created)
```

`my_portfolio.csv` columns expected:
- `Techstack`: string with keywords, e.g. "Python, Streamlit, LLM, RAG"
- `Links`: URL(s) to relevant work (comma-separated or a single link)

---

## 🔑 Environment Variables
- `GROQ_API_KEY` – required to call Groq models

Steps:
1. Push this repo to GitHub
2. Add `GROQ_API_KEY` in Render Dashboard → Environment

## 🧪 Local Tips
- If ChromaDB directory doesn’t exist, it will be initialized on first run
- If extraction fails for very large pages, try a more specific job URL

---

## 🛠 Development
Format: follow Python best practices; keep function names clear and descriptive.

Run Streamlit with a custom port:
```bash
streamlit run app/main.py --server.port 8501 --server.address 0.0.0.0
```

---



# Cold-email-generator
