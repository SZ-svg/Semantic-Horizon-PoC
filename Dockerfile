FROM python:3.11-slim

WORKDIR /app

# Устанавливаем библиотеку OpenAI (она работает с OpenRouter)
RUN pip install --no-cache-dir openai python-dotenv

RUN mkdir -p /app/workspace/agent_A /app/workspace/agent_B /app/workspace/observer_C

COPY loop_control.py .

CMD ["python", "loop_control.py"]