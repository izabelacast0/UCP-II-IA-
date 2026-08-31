# requisitos: 1) pip install ollama
#       2)  ollama run qwen2.5-coder
from ollama import chat

response = chat(
    model="qwen2.5-coder",
    messages=[
        {
            "role": "user",
            "content": """Considere o seguinte código Java: 
                         ppublic double calculateAverage(List<Integer> grades) {
    int sum = 0;
    for (Integer grade : grades) {
        sum += grade;
    }
    return sum / grades.size();
}
                         Gere a documentação (JavaDoc) para esse método, por favor.
                         """
        }
    ]
)

print(response["message"]["content"])