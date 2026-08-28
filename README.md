🤖 GKX1 — Personal AI Assistant

«A personal AI assistant built with Python that understands natural-language commands and can perform approved actions on a Windows PC.»

🚧 Project Status: Work in Progress

GKX1 is a personal AI assistant project that I'm building step-by-step to explore how AI, intent detection, tool routing, automation, memory, and human-AI interaction can work together.

The long-term goal is to create an assistant that can communicate naturally, understand requests, use appropriate tools, perform useful PC tasks, and eventually interact through voice and mobile devices.

---

🚀 Current Milestone — #1

The first working version of GKX1 can:

- 💬 Have natural conversations
- 🧠 Use a local AI model through Ollama
- 💾 Load basic personal information from JSON memory
- 🎯 Detect the intent behind a user's request
- 🔀 Route requests to different intent categories
- 🌐 Execute an approved browser action
- ▶️ Open YouTube using a natural-language command

Example

You: Open YouTube

GKX1: Opening YouTube...

🌐 YouTube opens automatically

Current Architecture

                  👤 USER
                     │
                     ▼
              Natural Language
                     │
                     ▼
                 GKX1 AI
                     │
                     ▼
              Intent Detection
                     │
                     ▼
                  Router
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
    Conversation   Study      YouTube
          │                     │
          ▼                     ▼
       Ollama              Browser Tool
                                │
                                ▼
                         🌐 YouTube

---

🛠️ Technology Stack

Technology| Purpose
🐍 Python| Core application
🧠 Ollama| Local AI model runtime
🤖 Gemma 3:1B| Current language model
💾 JSON| Basic memory and configuration
🌐 Python "webbrowser"| Browser actions
💻 VS Code| Development environment
🔧 Git & GitHub| Version control

Development Support

ChatGPT is used as a development and learning assistant for:

- Architecture planning
- Debugging
- Understanding concepts
- Code guidance
- Project development

---

📁 Project Structure

GKX1/
│
├── core/
│   ├── __init__.py
│   └── router.py
│
├── tools/
│   ├── __init__.py
│   └── browser.py
│
├── main.py
├── memory.json
├── test.py
├── test_browser.py
├── requirements.txt
├── .env
└── README.md

«".venv/" is used locally for the Python virtual environment and should not be uploaded to GitHub.»

---

⚙️ How It Works

GKX1 currently follows a simple pipeline:

User Command
     ↓
Intent Detection
     ↓
Router
     ↓
Approved Tool
     ↓
Action
     ↓
Result

For example:

"Open YouTube"
       ↓
Intent = open
       ↓
Browser Tool
       ↓
YouTube opens

This separation between understanding a request and executing an action is the foundation for future tool-based AI-agent capabilities.

---

💻 Installation

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd GKX1

2. Create a virtual environment

Windows:

python -m venv .venv

3. Activate the environment

.venv\Scripts\Activate.ps1

If you're using Git Bash:

source .venv/Scripts/activate

4. Install dependencies

pip install -r requirements.txt

5. Install Ollama

Install Ollama on your Windows PC and make sure it is running.

Then download the current model:

ollama pull gemma3:1b

6. Run GKX1

python main.py

---

🧪 Testing

Test the Intent Router

python test.py

Example:

User   : Hello Jarvis
Intent : conversation

User   : Open YouTube
Intent : open

User   : Search Python loops
Intent : web_search

User   : Play lo-fi music
Intent : youtube

User   : Teach me Python
Intent : study

Test the Browser Tool

python test_browser.py

This should open YouTube in your default browser.

---

🔐 Safety Approach

GKX1 is being developed with an approved-tool approach.

The AI should not automatically have unrestricted control over the computer.

The planned architecture is:

User Request
     ↓
AI Understanding
     ↓
Approved Action
     ↓
Tool Execution
     ↓
Result

Potentially sensitive actions such as:

- Sending messages
- Deleting files
- Running arbitrary commands
- Making purchases

should require explicit user confirmation.

---

🚀 Roadmap

✅ Stage 1 — Foundation

- [x] Python AI assistant
- [x] Ollama integration
- [x] Gemma 3:1B
- [x] Basic conversation
- [x] JSON memory
- [x] Intent detection
- [x] Command router
- [x] Browser tool
- [x] Open YouTube action

🔄 Stage 2 — More Tools

- [ ] Google/web search
- [ ] YouTube search
- [ ] Open trusted websites
- [ ] Windows application launching
- [ ] File/folder opening
- [ ] More tool routing

📌 Stage 3 — Productivity

- [ ] Reminders
- [ ] Notes
- [ ] Timers
- [ ] To-do management
- [ ] Daily planning

🧠 Stage 4 — Better Memory

- [ ] Long-term memory
- [ ] User preferences
- [ ] Project memory
- [ ] Conversation history
- [ ] Learning progress

📚 Stage 5 — Study Assistant

- [ ] Concept explanations
- [ ] Quiz generation
- [ ] Practice tests
- [ ] Progress tracking
- [ ] Revision system

🎙️ Stage 6 — Voice

- [ ] Speech-to-text
- [ ] Text-to-speech
- [ ] Push-to-talk
- [ ] Voice conversations
- [ ] Wake-word support

🖥️ Stage 7 — Desktop Interface

- [ ] Modern desktop GUI
- [ ] Chat interface
- [ ] Tool status
- [ ] Conversation history
- [ ] Settings

📱 Stage 8 — Mobile Access

- [ ] Mobile-friendly interface
- [ ] Remote access
- [ ] Cross-device interaction

---

🎯 Long-Term Vision

The goal is to evolve GKX1 from a simple AI chatbot into a personal AI agent.

                   🤖 GKX1
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   Conversation   Productivity    Learning
        │             │             │
        ▼             ▼             ▼
      Memory        Reminders      Quizzes
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                 Tool System
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
      Browser       YouTube       Windows
        │             │             │
        └─────────────┼─────────────┘
                      ▼
               Personal Assistant

---

📸 Demo

Milestone #1 — Open YouTube

A short demo shows GKX1 receiving the command:

"Open YouTube"

and launching YouTube automatically.

🎥 Demo video: See the attached/project demo showing the first working GKX1 action.

---

📚 What I'm Learning Through This Project

This project is helping me practically understand:

- AI assistants
- Local LLMs
- Natural-language processing
- Intent classification
- Tool routing
- AI-agent architecture
- Python automation
- Memory systems
- Human-AI interaction
- Safe tool execution

---

🔮 Future Goal

«Don't just build an AI that talks. Build an AI that understands, chooses, acts, and learns — safely.»

GKX1 is currently a work in progress, and I'm building it one capability at a time.

One command. One tool. One milestone at a time. 🚀

---

👨‍💻 Author

Gaurav Eknath Kumbhar

Building and learning AI/ML engineering through practical projects.

---

⭐ Project Status

🚧 Active Development

If you find this project interesting, feel free to ⭐ the repository and follow the development journey.
