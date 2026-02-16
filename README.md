# 🧠 AI Fact Checker Agent (OpenAI SDK + Agents)

A simple AI Agent built using the OpenAI Agents SDK that verifies the factual accuracy of statements.

This project demonstrates:

* Environment variable management
* Agent creation with custom instructions
* Asynchronous execution
* Structured prompt design
* Clean Python project setup

---

## 🚀 Project Overview

This program creates a **Fact Checker Agent** that:
* Accepts a statement as input
* Evaluates its factual accuracy
* Responds with:
  * ✅ TRUE + explanation
  * ❌ FALSE + explanation

Example:

```
Input:
"The Great Wall of China is visible from space with the naked eye."

Output:
❌ FALSE: It is a myth; the Great Wall is generally not visible to the naked eye from space without aid.
```

---

## 🏗️ Tech Stack

* Python 3.12+
* OpenAI Agents SDK
* dotenv (for environment variable management)
* asyncio (for async execution)

---

## 📂 Project Structure

```
ai-fact-checker/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/iyash1/factchecker.git
cd ai-fact-checker
```

### 2️⃣ Create a Conda Environment
```bash
conda create -n ai-fact-checker python=3.11
```
Activate it:
```bash
conda activate ai-fact-checker
```
### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, create one:

```
openai-agents==0.2.2
python-dotenv
langchain-openai==0.2.1
pydantic
```

---

## 🔑 Environment Setup

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```

⚠️ Never commit your `.env` file to GitHub.

Add this to `.gitignore`:

```
.env
venv/
```

---

## ▶️ Running the Program

```bash
python app.py --fact "<RANDOM STATEMENT THAT NEEDS VERFICATION>"
```

You should see:

```
 -----------------------------------
 ✅ Environment successfully loaded.
 ✅ Agent 'Fact Checker' created successfully!
 -----------------------------------
 🔍 Asking the Fact Checker to verify:: '...'

--- 🤖 AGENT'S RESPONSE ---

❌ FALSE: ...

--- 🤖 END OF AGENT'S RESPONSE ---
```

---

## 🧩 How It Works

1. Loads the OpenAI API key from `.env`
2. Creates a Fact Checker Agent with defined behavioral instructions
3. Runs the agent asynchronously using `Runner.run()`
4. Prints the final structured output

---

## 🔜 Future Improvements

Planned upgrades:

* JSON structured output
* Tool integration (web search for real fact verification)
* Batch statement processing
* Logging system
* Configurable model and temperature
* CLI argument input
* Unit tests

---

## 📜 License

This project is for educational purposes.
