# Exercício 2 — Detecção de duplicação de lógica com CodeBERT e all-MiniLM-L6-v2

## Contexto

Durante uma revisão de código, um desenvolvedor suspeita que uma regra de negócio pode ter sido implementada em mais de um lugar do sistema.

## Trechos de código comparados

**Exemplo 1**

```java
public boolean canEnroll(Student student) {
    return student.isActive()
            && student.getCompletedCredits() >= 120;
}
```

**Exemplo 2**

```java
public boolean canGraduate(Student student) {
    if (student.isActive() && student.getCompletedCredits() >= 120) {
        return true;
    }
    return false;
}
```

## Metodologia

Cada trecho de código foi convertido em um vetor de embedding por dois modelos diferentes, e a similaridade entre os dois vetores foi calculada usando **similaridade de cosseno** (valor entre 0 e 1 — quanto mais próximo de 1, mais semanticamente parecidos os dois trechos são).

Os scripts utilizados:
- `codeBert.py` — usa o modelo `microsoft/codebert-base` (biblioteca `transformers`)
- `sentence_transformer.py` — usa o modelo `all-MiniLM-L6-v2` (biblioteca `sentence-transformers`)

## Resultados

| Modelo | Similaridade calculada |
|---|---|
| CodeBERT | 0.9743 |
| all-MiniLM-L6-v2 | 0.8376 |

## Existe duplicação de lógica?

**Sim.** Ambos os modelos indicaram um alto grau de similaridade semântica entre os dois métodos — o CodeBERT apontou 0.9743 e o all-MiniLM-L6-v2 apontou 0.8376, ambos bem acima do que costuma ser considerado um limiar de forte semelhança (~0.85).

Isso confirma a suspeita do desenvolvedor: os métodos `canEnroll` e `canGraduate` implementam exatamente a **mesma regra de negócio** — verificar se o estudante está ativo (`isActive()`) e possui pelo menos 120 créditos concluídos (`getCompletedCredits() >= 120`) — apenas com sintaxes diferentes (uma expressão booleana direta versus um bloco `if/else`). Trata-se de um caso claro de duplicação de lógica, que idealmente deveria ser extraída para um único método reutilizável (por exemplo, `meetsCreditRequirement(Student student)`), evitando inconsistências caso a regra precise ser alterada no futuro.
