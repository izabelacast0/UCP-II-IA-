import time
from groq import Groq

client = Groq(api_key="minha chave tava aq")  

modelos = ["qwen/qwen3.6-27b", "openai/gpt-oss-120b"]

codigo = """public double calculateAverage(List<Integer> grades) {
    int sum = 0;
    for (Integer grade : grades) {
        sum += grade;
    }
    return sum / grades.size();
}"""

prompt_testes = f"""Considere o seguinte método Java:
{codigo}

Gere testes automatizados (JUnit) para esse método, cobrindo casos normais e casos extremos (edge cases). Seja direto, sem explicações longas antes do código."""

prompt_docs = f"""Considere o seguinte método Java:
{codigo}

Gere a documentação (Javadoc) completa para esse método. Seja direto, sem explicações longas antes do resultado."""

for modelo in modelos:
    print(f"\n========== {modelo} ==========")

    print("\n--- Testes automatizados ---")
    resp1 = client.chat.completions.create(
        model=modelo,
        messages=[{"role": "user", "content": prompt_testes}],
        max_tokens=800
    )
    print(resp1.choices[0].message.content)

    print("\nAguardando para evitar limite de requisições...")
    time.sleep(20)

    print("\n--- Documentação ---")
    resp2 = client.chat.completions.create(
        model=modelo,
        messages=[{"role": "user", "content": prompt_docs}],
        max_tokens=800
    )
    print(resp2.choices[0].message.content)

    print("\nAguardando para evitar limite de requisições...")
    time.sleep(20)

print("\nConcluído!")