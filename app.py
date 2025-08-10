import gradio as gr
from browser_search import bing_search as google_search
from summarizer import summarize_results

def search_and_summarize(query, max_results=5):
    results = google_search(query, max_results=max_results)

    if not results:
        return "<p style='color:red;'>No results found.</p>", ""

    # Create clickable HTML list of results
    results_html = "<ol>"
    for title, url in results:
        results_html += f"<li><a href='{url}' target='_blank'>{title}</a></li>"
    results_html += "</ol>"

    # Get summary
    summary = summarize_results(results)

    return results_html, summary


# Gradio UI
iface = gr.Interface(
    fn=search_and_summarize,
    inputs=[
        gr.Textbox(label="Search Query", placeholder="Type your query here"),
        gr.Slider(minimum=1, maximum=10, step=1, value=5, label="Max Results")
    ],
    outputs=[
        gr.HTML(label="Top Search Results"),
        gr.Textbox(label="Summary")
    ],
    title="Web Search & Summarizer",
    description="Enter a search query and get top Bing results summarized by OpenAI."
)

if __name__ == "__main__":
    iface.launch()
