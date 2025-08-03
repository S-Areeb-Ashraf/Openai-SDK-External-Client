# CLI + Streaming with OpenAI SDK

This example demonstrates how to:
- Use **OpenAI SDK** in the terminal
- Stream tokens in real-time
- Work with **AsyncOpenAI** and Gemini

---

## Setup
Install dependencies:
```bash
pip install openai python-dotenv
```

Set `.env`:
```
GEMINI_API_KEY=your_gemini_api_key
```

---

## Run
```bash
python main.py
```

---

## Key Streaming Logic
```python
result = Runner.run_streamed(agent, input="Your question")
async for event in result.stream_events():
    print(event.data.delta, end="", flush=True)
```
