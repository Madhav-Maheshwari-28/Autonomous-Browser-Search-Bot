---

# 🖥️ Autonomous Browser Search Bot

An AI-powered bot that searches the web, filters results, and summarizes useful information for you — without endless tab-switching.
Built during my **internship at IIT Jammu** to make online research smarter, faster, and easier.

---

## 🚀 Why This Project?

Research shouldn’t feel like a full-time job.
This bot automates:

* 🌐 Opening a real browser
* 🔍 Searching queries online
* 📝 Extracting top search results with descriptions
* 🤖 Summarizing content for quick reading

---

## 🛠️ Tools & Technologies Used

* 🐍 **Python** – Core programming
* 🤖 **OpenAI API** – Natural language understanding & summarization
* 🌐 **Playwright** – Browser automation
* 🏷️ **BeautifulSoup** – HTML parsing
* 📡 **Requests** – Web data fetching

---

## 📂 Project Structure

```
📦 autonomous-browser-search-bot
 ┣ 📜 main.py           # Entry point to run the bot
 ┣ 📜 search.py         # Search & data extraction logic
 ┣ 📜 summarize.py      # AI summarization functions
 ┣ 📜 requirements.txt  # Dependencies
 ┗ 📜 README.md         # Project documentation
```

---

## ⚡ How It Works

1. **User enters a search query**
2. **Playwright** launches a browser and searches Google
3. Extracts **titles + descriptions** from the results
4. **OpenAI API** summarizes the top findings
5. Displays clean, concise output

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/autonomous-browser-search-bot.git
cd autonomous-browser-search-bot

# Install dependencies
pip install -r requirements.txt

# Run the bot
python main.py
```

---

## 🔑 Configuration

Add your **OpenAI API Key** in an `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## 🎯 Features

* 🌍 Automated Google search
* 📄 Snippet extraction with descriptions
* 🧠 AI-powered summarization
* 💡 Saves time & boosts productivity

---

## 🙌 Acknowledgments

Special thanks to **Pramveer Sir** for his mentorship and guidance during my internship.

---

Do you want me to make a **GitHub-friendly cover image** for this README so it looks eye-catching at the top of your repo?
