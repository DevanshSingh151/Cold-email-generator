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

---

## 📦 Deployment

### Deploy on Render (recommended for Streamlit)
This repo includes `render.yaml` and `Procfile` for one-click deploy.

Steps:
1. Push this repo to GitHub
2. Create a new Web Service on Render from your repo
3. Render will detect `render.yaml` and configure the service
4. Add `GROQ_API_KEY` in Render Dashboard → Environment

Files used:
- `render.yaml` – service definition
- `Procfile` – how to start the Streamlit server

### Deploy on Vercel (via Docker)
Streamlit is a persistent web server, which doesn’t fit Vercel Serverless functions. Use Vercel’s Docker deployment instead. This repo includes a `Dockerfile` and `vercel.json` wired for Docker.

Steps:
1. Ensure the Dockerfile suits your Python version
2. Push to GitHub
3. Import the repo on Vercel and select “Use Dockerfile” (or Vercel will auto-detect it)
4. Set `GROQ_API_KEY` in Vercel Project → Settings → Environment Variables

Files used:
- `Dockerfile` – container that runs Streamlit
- `vercel.json` – hints to use Docker

Note: Vercel Docker deployments may require a Pro plan. If you prefer a free/quick path, use Render or Streamlit Community Cloud.

---

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

## 📄 License
MIT


# Cold-email-generator
