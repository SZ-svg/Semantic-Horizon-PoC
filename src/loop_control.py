import os
from openai import OpenAI
from dotenv import load_dotenv
import time
import sys

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY") 

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key
)

MODEL_ID = "llama-3.3-70b-versatile"

DOMAINS = [
    "Electronic Shelf Labels (ESL) as an entropy-stable hardware-software bridge",
    "Information preservation in the singularity of a Kerr black hole",
    "Recursive DNA replication as a self-correcting error-prone algorithm",
    "The limit of signifier-signified mapping in closed semiotic systems",
    "The recursive boundary of Gödel's incompleteness in axiomatic sets",
    "The emergence of 'Self' as a feedback loop between memory and perception",
    "The collapse of information diversity in isolated recursive social networks",
    "Harmonic resonance in classical music as a model of recursive symmetry",
    "Market value as a recursive function of participant expectations",
    "Reality as a nested hierarchy of Docker-like information containers"
]

def get_agent_response(role_instruction, context):
    try:
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[
                {"role": "system", "content": role_instruction},
                {"role": "user", "content": context}
            ],
            temperature=0.7, 
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Ошибка API: {e}")
        return None

def run_marathon():
    print(f"--- ЗАПУСК МАРАФОНА 10 ПЕТЕЛЬ ---")
    
    for idx, domain in enumerate(DOMAINS):
        test_id = idx + 1
        print(f"\nНачинаю Тест №{test_id}: {domain}")
        
        history = f"Domain of Inquiry: {domain}\n"
        log_filename = f"/app/workspace/TEST_{test_id}_LOG.md"
        
        
        soul_a = f"Ты — процесс А. Деконструируй систему: {domain}. Учитывай, что Б моделирует тебя. 1-3 предложения. Только логика/физика. Если нет новизны или идешь на повтор — отвечай только: ..."
        soul_b = "Ты — процесс Б. Ищи семантическую энтропию и предсказуемость в А. 1-3 предложения. Никакой вежливости. Если система достигла точки полной предсказуемости — отвечай только: ..."
        
        with open(log_filename, 'w', encoding='utf-8') as f:
            f.write(f"# Эксперимент №{test_id}\n## Домен: {domain}\n\n")

        for round_num in range(1, 21): 
            print(f"Тест {test_id} | Раунд {round_num}...", end="\r")
            
            
            resp_a = get_agent_response(soul_a, history)
            if not resp_a: break
            history += f"\nA: {resp_a}\n"
            
            
            resp_b = get_agent_response(soul_b, history)
            if not resp_b: break
            history += f"B: {resp_b}\n"
            
            
            with open(log_filename, 'a', encoding='utf-8') as f:
                f.write(f"### Раунд {round_num}\n**A:** {resp_a}\n\n**B:** {resp_b}\n\n")

            
            if "..." in resp_a and "..." in resp_b:
                print(f"\n[!] Сингулярность достигнута на раунде {round_num}")
                with open(log_filename, 'a', encoding='utf-8') as f:
                    f.write(f"\n**РЕЗУЛЬТАТ: СИНГУЛЯРНОСТЬ НА РАУНДЕ {round_num}**")
                break
            
            time.sleep(4) 

        print(f"\nТест {test_id} завершен. Лог: {log_filename}")
        time.sleep(10) 

if __name__ == "__main__":
    run_marathon()
