# Chainlit + OpenAI SDK (Async Example)

This example demonstrates how to use **Chainlit** with the **OpenAI SDK** and **Google Gemini** in **asynchronous mode**.

---

## Features
- Simple **chat UI** using Chainlit
- Uses **AsyncOpenAI** with Gemini API
- Maintains **conversation history**

---

## Setup
Install dependencies:
```bash
pip install chainlit openai python-dotenv
```

Set up your `.env`:
```
GEMINI_API_KEY=your_gemini_api_key
```

---

## Run the App
```bash
chainlit run main.py
```

Then open the provided local URL to chat with the assistant.

---

## Key Files
- **main.py**: Contains the Chainlit integration with OpenAI SDK and Gemini.
