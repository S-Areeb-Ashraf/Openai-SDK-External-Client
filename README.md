# OpenAI SDK Testing with External Clients (Gemini)

This repository demonstrates how to use the OpenAI SDK with external clients such as **Google Gemini**. It includes multiple examples covering:

- **Chainlit-based Chat UI** (Synchronous & Asynchronous)
- **Streaming Responses**
- **Using Tools with Async Mode**
- **Command-Line Interface (CLI) Demonstrations**

All examples use `AsyncOpenAI` from the OpenAI Python SDK with Gemini as the backend model (`gemini-1.5-flash`).

---

## Prerequisites

- Python 3.9+
- An active **Google Gemini API Key**
- Installed dependencies:
  ```bash
  pip install openai chainlit python-dotenv
  ```

- Add your API key in a `.env` file:
  ```
  GEMINI_API_KEY=your_gemini_api_key_here
  ```

---

## Project Structure

```
.
├── README.md                # Main documentation (this file)
├── 1-chainlit-basic/        # Chainlit example (async)
│   └── README.md
├── 2-chainlit-streaming/    # Chainlit example with streaming
│   └── README.md
├── 3-tools-async/           # Tools integration example
│   └── README.md
└── 4-cli-streaming/         # CLI-based streaming example
    └── README.md
```

---

## Examples

### 1. **Chainlit Basic Chat**
- **Path:** `1-chainlit-basic/`
- Demonstrates a basic Chainlit UI with OpenAI SDK using Gemini.

### 2. **Chainlit Streaming**
- **Path:** `2-chainlit-streaming/`
- Adds **streaming responses** to Chainlit.

### 3. **Tools with Async Mode**
- **Path:** `3-tools-async/`
- Shows how to register and use tools with async OpenAI SDK.

### 4. **CLI with Streaming**
- **Path:** `4-cli-streaming/`
- Streams responses in the terminal without any UI.

---

## Key Concepts Covered
- Setting up **AsyncOpenAI** with Gemini
- Running **Agents and Runners**
- **Streaming responses**
- **Tool usage in Agents**
- CLI vs UI-based implementations

---

## How to Run Each Example
Navigate to the respective folder and run:

```bash
python main.py
```

For Chainlit examples:
```bash
chainlit run main.py
```

---

## Author
Developed by Syed Areeb Ashraf
