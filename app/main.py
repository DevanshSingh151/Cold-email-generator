
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
	# Custom styles
	st.markdown(
		"""
		<style>
			/* Page background */
			.stApp {
				background: linear-gradient(135deg, #5634d1 0%, #6a5acd 50%, #7a5cff 100%);
			}

			/* Global high-contrast text on violet background */
			.stApp, .stApp * { color: #ffffff !important; }

			/* Sidebar transparent so it inherits background */
			section[data-testid="stSidebar"] { background: transparent !important; }

			/* Inputs high-contrast */
			.stTextInput input, textarea, select {
				background: rgba(255,255,255,0.12) !important;
				border: 1px solid rgba(255,255,255,0.35) !important;
				color: #ffffff !important;
			}
			.stTextInput input::placeholder, textarea::placeholder { color: rgba(255,255,255,0.75) !important; }

			/* Hero card */
			.hero {
				border: 1px solid rgba(255,255,255,0.35);
				background: rgba(255,255,255,0.08);
				border-radius: 16px;
				padding: 24px 24px 16px 24px;
				box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
				margin-bottom: 8px;
			}

			.hero h1 {
				font-size: 28px;
				margin: 0 0 8px 0;
				color: #ffffff;
				font-weight: 800;
			}

			.subtle {
				color: #f8fafc;
				font-size: 14px;
			}

			/* Button */
			.stButton>button {
				background: #ffffff;
				color: #2a2367;
				border: 0;
				padding: 10px 18px;
				border-radius: 10px;
				box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
				transition: transform 0.05s ease;
			}
			.stButton>button:hover { transform: translateY(-1px); }

			/* Chips */
			.chips { display: flex; flex-wrap: wrap; gap: 8px; }
			.chip {
				background: rgba(255,255,255,0.18);
				border: 1px solid rgba(255,255,255,0.45);
				color: #ffffff;
				padding: 4px 10px;
				border-radius: 999px;
				font-size: 12px;
				font-weight: 600;
			}

			/* Expander header text */
			[data-testid="stExpander"] summary {
				color: #ffffff;
				font-weight: 700;
			}
			[data-testid="stExpander"] details {
				background: rgba(255,255,255,0.08);
				border: 1px solid rgba(255,255,255,0.25);
				border-radius: 12px;
			}

			/* Code blocks */
			pre, code, .stCode {
				background: rgba(0,0,0,0.55) !important;
				color: #f8fafc !important;
			}

			/* Footer */
			.footer {
				position: fixed;
				left: 0; right: 0; bottom: 0;
				padding: 10px 12px;
				text-align: center;
				background: rgba(255,255,255,0.08);
				backdrop-filter: blur(6px);
				border-top: 1px solid rgba(255,255,255,0.25);
				font-size: 12px;
				color: #ffffff;
			}
		</style>
		""",
		unsafe_allow_html=True,
	)

	# Sidebar
	with st.sidebar:
		st.header("⚙️ Options")
		st.write("Paste a careers or job post URL and generate tailored cold emails.")
		st.caption("Tip: Prefer detailed job pages for best results.")

	# Hero
	st.markdown(
		"""
		<div class="hero">
			<h1>📧 Cold Email Generator</h1>
			<p class="subtle">Turn job descriptions into polished, personalized cold emails with portfolio links.</p>
		</div>
		""",
		unsafe_allow_html=True,
	)

	# Input and action row
	col1, col2 = st.columns([4, 1])
	with col1:
		url_input = st.text_input("Job or careers page URL", value="https://jobs.nike.com/job/R-33460", placeholder="https://example.com/careers/software-engineer")
	with col2:
		submit_button = st.button("Generate ✨", use_container_width=True)

	if submit_button:
		try:
			with st.spinner("Fetching page and analyzing role details..."):
				loader = WebBaseLoader([url_input])
				data = clean_text(loader.load().pop().page_content)
				portfolio.load_portfolio()
				jobs = llm.extract_jobs(data)

			st.success(f"Found {len(jobs)} job profile(s). Crafting emails...")

			for idx, job in enumerate(jobs, start=1):
				role_name = job.get('role', f'Role #{idx}')
				skills = job.get('skills', [])
				links = portfolio.query_links(skills)
				email = llm.write_mail(job, links)

				with st.expander(f"✉️ Email for {role_name}", expanded=True if len(jobs) == 1 else False):
					if skills:
						st.markdown("**Matched skills**")
						st.markdown("<div class='chips'>" + "".join([f"<span class='chip'>{s}</span>" for s in skills]) + "</div>", unsafe_allow_html=True)

					if links:
						st.markdown("**Suggested portfolio links**")
						for row in links:
							if isinstance(row, list):
								for meta in row:
									link_text = meta.get('links', '') if isinstance(meta, dict) else str(meta)
									if link_text:
										st.markdown(f"- {link_text}")

					st.markdown("**Generated email**")
					st.code(email, language='markdown')
		except Exception as e:
			st.error(f"An Error Occurred: {e}")

	# Footer
	st.markdown('<div class="footer">Made by Devansh</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)
