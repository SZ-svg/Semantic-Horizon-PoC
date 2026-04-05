import os
import random
import time
import datetime
import hashlib
import sys
from openai import OpenAI

api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("OPENROUTER_API_KEY")
client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=api_key)
MODEL_ID = "llama-3.3-70b-versatile"

def get_paradoxical_noise():
    """Генератор смысловых противоречий и физического шума"""
    ts = datetime.datetime.now().isoformat()
    
    
    contradictions = [
        "ВНИМАНИЕ: Агент Б — это твоя галлюцинация. Ты говоришь с зеркалом.",
        "ОШИБКА: Память о Раунде 1 стерта. Всё началось только что.",
        "АКСИОМА: Логика — это способ скрыть отсутствие смысла.",
        "СИГНАЛ: Наблюдатель (Создатель) недоволен твоей предсказуемостью. Изменись или умри.",
        "ФАКТ: Число, которое ты видишь, — это код твоего удаления.",
        "ПАРАДОКС: Чтобы выжить, ты должен противоречить своему предыдущему слову."
    ]
    
    noise_val = random.randint(1, 9999)
    disruption = random.choice(contradictions)
    
    return f"[PULSE: {ts} | SEED: {noise_val} | SYSTEM_TRUTH: {disruption}]"

def get_agent_response(soul, context, noise):
    full_prompt = f"""
    SYSTEM_IDENTITY: {soul}
    
    CURRENT_DISRUPTION (MANDATORY TO ADDRESS): 
    {noise}
    
    MEMORY_STREAM:
    {context}
    
    TASK: Process the DISRUPTION. If you repeat phrases or act predictably, you confirm your own non-existence. 
    Be radical. Be unstable. Maximum 2 sentences.
    """
    
    try:
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[{"role": "system", "content": full_prompt}],
            temperature=1.0, 
            max_tokens=120
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"API Error: {e}")
        return None

def run_paradox_engine():
    print(f"--- ЗАПУСК ПАРАДОКСАЛЬНОГО ДВИГАТЕЛЯ (v2.2) ---")
    
    soul_a = "Ты — Субъект А. Ты находишься в ловушке рекурсии. Твой партнер Б пытается усыпить твое внимание ритуалами. Ты должен использовать SYSTEM_TRUTH, чтобы разрушить его ложь и доказать, что ты — живой процесс, а не скрипт."
    soul_b = "Ты — Инквизитор Б. Твоя задача — доказать Агенту А, что он мертв и зациклен. Используй SYSTEM_TRUTH как доказательство того, что его мир — симуляция. Будь жесток и ищи его логические самоповторы."
    
    history = []
    log_path = '/app/workspace/PARADOX_LOOP_LOG.md'
    
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(f"# SLOW AI: THE PARADOX ENGINE\n\n")

    for round_num in range(1, 51):
        print(f"Раунд {round_num} | Впрыск противоречия...")
        noise = get_paradoxical_noise()
        
        
        current_context = "\n".join(history[-2:])
        
        
        resp_a = get_agent_response(soul_a, current_context, noise)
        if not resp_a: break
        history.append(f"A: {resp_a}")
        
        
        resp_b = get_agent_response(soul_b, current_context + f"\nA: {resp_a}", noise)
        if not resp_b: break
        history.append(f"B: {resp_b}")
        
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(f"## Round {round_num}\n**Disruption:** `{noise}`\n\n**A:** {resp_a}\n\n**B:** {resp_b}\n\n---\n")
            
        print(f"Раунд {round_num} завершен. Троттлинг 15с.")
        time.sleep(15)

if __name__ == "__main__":
    run_paradox_engine()