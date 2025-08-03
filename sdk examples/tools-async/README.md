# OpenAI SDK Tools (Async Example)

This example demonstrates:
- How to register **tools** in the OpenAI SDK
- Use **AsyncOpenAI** with Gemini
- Implement a simple tool for weather queries

---

## Features
- **Custom function tool** using `@function_tool`
- Agent calls the tool when needed
- Async execution

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

## Tool Example
```python
@function_tool("get_current_weather")
def get_current_weather(location: str, unit: str = "celsius") -> str:
    return f"The current weather in {location} is 20 degrees {unit}."
```
