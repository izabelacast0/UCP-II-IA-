# requisitos: 1) pip install ollama
#       2)  ollama run starcode2
from ollama import chat

response = chat(
    model="starcode2",
    messages=[
        {
            "role": "user",
            "content": """Considere o seguinte código Java: 
                         public String getUserInitials(String firstName, String lastName) {
                              return firstName.substring(0, 1).toUpperCase()
                                     + lastName.substring(0, 1).toUpperCase();
                         }
                         Tem algum bug nesse código? Algo que pode comprometer a funcionalidade dele? Caso sim, me aponte os problemas, e corrija o código por favor.
                         """
        }
    ]
)

print(response["message"]["content"])
