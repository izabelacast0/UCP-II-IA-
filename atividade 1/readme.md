# Atividade 1 — Inteligência Artificial Aplicada à Engenharia de Software

Esta pasta contém os exercícios da **Atividade 1**, desenvolvidos utilizando diferentes modelos de Inteligência Artificial para análise, correção, comparação, geração de testes e documentação de código.

##  Organização

```text
atividade-1/
├── exercicio-1/
│   ├── ...
│   └── README.md
│
├── exercicio-2/
│   ├── ...
│   └── README.md
│
└── exercicio-3/
    ├── ...
    └── README.md
```

Cada pasta contém os scripts utilizados no exercício e um `README.md` com as respostas produzidas pelos modelos.

---

##  Exercício 1 — Análise e correção de código

Foi utilizado o seguinte código Java:

```java
public String getUserInitials(String firstName, String lastName) {
    return firstName.substring(0, 1).toUpperCase()
            + lastName.substring(0, 1).toUpperCase();
}
```

### Objetivos

Utilizar os modelos **DeepSeek Coder, StarCoder e Qwen Coder** para:

* Identificar possíveis problemas no código;
* Solicitar aos modelos uma correção para os problemas encontrados;
* Registrar as respostas produzidas pelos modelos.

**Sugestão:** utilização de um modelo local por meio do **Ollama**.

---

##  Exercício 2 — Similaridade entre códigos

Foram considerados dois trechos de código que implementam uma regra de negócio semelhante:

### Exemplo 1

```java
public boolean canEnroll(Student student) {
    return student.isActive()
            && student.getCompletedCredits() >= 120;
}
```

### Exemplo 2

```java
public boolean canGraduate(Student student) {
    if (student.isActive() && student.getCompletedCredits() >= 120) {
        return true;
    }
    return false;
}
```

### Objetivo

Utilizar os modelos **CodeBERT** e **all-MiniLM-L6-v2** para calcular a similaridade entre os dois trechos de código e responder se existe **duplicação de lógica**.

---

##  Exercício 3 — Testes e documentação

Foi utilizado o seguinte método Java:

```java
public double calculateAverage(List<Integer> grades) {
    int sum = 0;
    for (Integer grade : grades) {
        sum += grade;
    }
    return sum / grades.size();
}
```

### Objetivos

Utilizar os modelos **DeepSeek Coder, StarCoder e Qwen Coder** para:

**3.1)** Gerar testes automatizados;

**3.2)** Gerar documentação para o método.

**Sugestão:** utilização de um modelo local por meio do **Ollama**.

---

##  Modelos utilizados

| Exercício   | Modelos                                |
| ----------- | -------------------------------------- |
| Exercício 1 | DeepSeek Coder, StarCoder e Qwen Coder |
| Exercício 2 | CodeBERT e all-MiniLM-L6-v2            |
| Exercício 3 | DeepSeek Coder, StarCoder e Qwen Coder |

---

## 📌 Observação

As respostas apresentadas nos arquivos `README.md` de cada exercício correspondem às respostas produzidas pelos respectivos modelos utilizados na atividade.
