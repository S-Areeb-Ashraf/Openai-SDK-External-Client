# Chainlit + Streaming Responses

This example adds **streaming responses** to the previous Chainlit implementation.

---

## Features
- Real-time token streaming in the Chainlit UI
- Maintains conversation history
- Uses **OpenAI SDK** with **Gemini**

---

## Setup
Same as in chainlit Basic.

---

## Run
```bash
chainlit run main.py
```

---

## Key Difference
Uses:
```python
result = Runner.run_streamed(...)
async for event in result.stream_events():
    await msg.stream_token(event.data.delta)
```
to **stream tokens** instead of waiting for the entire response.
