# 🤖 AI Personal Assistant – Smart Productivity & Automation

An AI-powered personal assistant built using **Streamlit and n8n** that helps users manage their daily activities through a single interface. It integrates web search, Gmail, Google Calendar, expense tracking, note management, and task management to simplify everyday workflows and improve productivity.

## ✨ Features

### 🔍 1. Web Search
- Search the web for information and relevant resources.
- Retrieve information without manually browsing multiple websites.

### 📅 2. Google Calendar Integration
- Access calendar events and schedules.
- Manage daily activities and stay updated with upcoming events.

### 📧 3. Gmail Integration
- Access Gmail data through workflow automation.
- Retrieve and manage email-related information.

### 💰 4. Expense Tracking
- Record and track daily expenses.
- Maintain expense information in an organized manner.
- Monitor spending and manage personal finances.

### 📝 5. Notes Creation
- Create and save notes.
- Organize important information and ideas.

### ✅ 6. Task Management
- Create new tasks.
- Delete existing tasks.
- Manage daily activities and keep track of pending work.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive frontend and user interface |
| n8n | Workflow automation and integration |
| Gmail API / Integration | Email access |
| Google Calendar API / Integration | Calendar access |
| Web Search Integration | Online information retrieval |

## 🏗️ Architecture

The application follows a simple architecture:

**User → Streamlit Interface → n8n Workflow → External Services → Response to Streamlit**

1. The user interacts with the Streamlit application.
2. Streamlit sends the user's request to the configured n8n webhook.
3. n8n processes the request and executes the corresponding workflow.
4. The workflow communicates with the required external services.
5. The processed result is returned to Streamlit and displayed to the user.

## 📂 Project Structure

```text
Personal_Assistant/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .gitignore              # Files excluded from Git
└── README.md               # Project documentation
```

*Update the structure according to your actual project files.*

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10 or above
- n8n (cloud or self-hosted)
- Required API credentials and integrations

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd AI-Personal-Assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory and add the required configuration:

```env
N8N_WEBHOOK_URL=your_n8n_webhook_url
```

Add any additional credentials required by your integrations. Configure API credentials securely inside n8n wherever possible.

### 6. Configure n8n Workflows

- Set up the required n8n workflows.
- Configure the Gmail and Google Calendar integrations.
- Configure the web search and other required services.
- Activate the workflows and ensure the webhook URLs match your Streamlit configuration.

### 7. Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## 🔐 Security

- Keep API keys, webhook URLs, and credentials private.
- Store sensitive configuration in environment variables.
- Never commit `.env` files or OAuth credentials to GitHub.
- Configure appropriate authentication and permissions for connected services.

## 🚀 Future Enhancements

- AI-powered conversational interface.
- Voice-based interaction.
- Smart reminders and notifications.
- Expense analytics and visualization.
- Daily productivity summaries.
- Advanced task scheduling and prioritization.

## 👨‍💻 Author

**Hemant Pande**

Developed as a personal productivity and workflow automation project using Streamlit and n8n.

---

⭐ If you find this project useful, consider giving it a star!