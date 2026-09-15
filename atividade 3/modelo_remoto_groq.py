# requisitos: pip install groq
# chave: https://console.groq.com/keys

from groq import Groq

client = Groq(api_key="Minha chave estava aq")  

modelos = ["qwen/qwen3.6-27b", "openai/gpt-oss-120b"]

prompt = """Considere o seguinte código Java:
public String getUserInitials(String firstName, String lastName) {
    return firstName.substring(0, 1).toUpperCase()
            + lastName.substring(0, 1).toUpperCase();
}
Tem algum bug nesse código? Algo que pode comprometer a funcionalidade dele? Caso sim, me aponte os problemas, e corrija o código por favor.
"""

for modelo in modelos:
    print(f"\n===== {modelo} =====")
    response = client.chat.completions.create(
        model=modelo,
        messages=[{"role": "user", "content": prompt}]
    )
    print(response.choices[0].message.content)