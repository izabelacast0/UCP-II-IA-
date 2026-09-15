# Lista de Exercícios 1 — Análise de Código Java com LLMs (Groq)

Scripts em Python que utilizam a API do Groq (https://console.groq.com/keys) para consultar dois modelos remotos:

- `qwen/qwen3.6-27b`
- `openai/gpt-oss-120b`

## Arquivos

- `modelo_remoto_groq.py` — Exercício 1 (análise e correção de código)
- `testes_documentacao_groq.py` — Exercício 3 (geração de testes e documentação)

## Como rodar

```
pip install groq
```

Coloque sua chave da API do Groq na variável `api_key` de cada script (gerada em https://console.groq.com/keys), depois execute:

```
python modelo_remoto_groq.py
python testes_documentacao_groq.py
```

---

## Exercício 1 — Análise do método `getUserInitials`

Código analisado:

```java
public String getUserInitials(String firstName, String lastName) {
    return firstName.substring(0, 1).toUpperCase()
            + lastName.substring(0, 1).toUpperCase();
}
```

### 1.1) Problemas encontrados

Os dois modelos identificaram os mesmos problemas centrais:

| Problema | Descrição |
|---|---|
| `NullPointerException` | Se `firstName` ou `lastName` forem `null` |
| `StringIndexOutOfBoundsException` | Se `firstName` ou `lastName` forem string vazia (`""`) |
| Espaços em branco | Nomes com espaço no início (ex: `"  João"`) geram inicial errada (um espaço) |

O `openai/gpt-oss-120b` foi além e também apontou:
- Uso de `toUpperCase()` sem `Locale` explícito (pode se comportar de forma inesperada em locales como o turco)
- Suporte incompleto a caracteres Unicode fora do BMP (ex: emojis, certos acentos) ao usar `substring` em vez de `codePointAt`

### 1.2) Correções propostas

**`qwen/qwen3.6-27b`** — correção enxuta, tratando null/vazio/espaços:

```java
public String getUserInitials(String firstName, String lastName) {
    if (firstName == null || lastName == null) {
        return "";
    }

    String trimmedFirst = firstName.trim();
    String trimmedLast  = lastName.trim();

    if (trimmedFirst.isEmpty() || trimmedLast.isEmpty()) {
        return "";
    }

    return trimmedFirst.substring(0, 1).toUpperCase()
            + trimmedLast.substring(0, 1).toUpperCase();
}
```

**`openai/gpt-oss-120b`** — correção mais robusta, com validação explícita, suporte a Unicode e testes JUnit inclusos:

```java
public static String getUserInitials(String firstName, String lastName) {
    Objects.requireNonNull(firstName, "firstName não pode ser null");
    Objects.requireNonNull(lastName, "lastName não pode ser null");

    String f = firstName.trim();
    String l = lastName.trim();

    if (f.isEmpty()) {
        throw new IllegalArgumentException("firstName não pode ser vazio ou apenas espaços");
    }
    if (l.isEmpty()) {
        throw new IllegalArgumentException("lastName não pode ser vazio ou apenas espaços");
    }

    int firstUpper = Character.toUpperCase(f.codePointAt(0));
    int lastUpper  = Character.toUpperCase(l.codePointAt(0));

    return new StringBuilder(2)
            .appendCodePoint(firstUpper)
            .appendCodePoint(lastUpper)
            .toString();
}
```

### Comparação entre os modelos

| | `qwen/qwen3.6-27b` | `openai/gpt-oss-120b` |
|---|---|---|
| Estilo da resposta | Direto e enxuto | Detalhado, com tabela explicativa |
| Tratamento de erro | Retorna `""` em caso inválido | Lança exceções (`NullPointerException`, `IllegalArgumentException`) |
| Cobertura extra | Não | Locale, Unicode/codePoints, testes JUnit |

---

## Exercício 3 — Testes e documentação para `calculateAverage`

Código analisado:

```java
public double calculateAverage(List<Integer> grades) {
    int sum = 0;
    for (Integer grade : grades) {
        sum += grade;
    }
    return sum / grades.size();
}
```

Bug identificado por ambos os modelos: `sum / grades.size()` é uma **divisão inteira** (int / int), então o resultado perde a parte decimal antes de ser convertido para `double`. Além disso, lista vazia causa `ArithmeticException` e lista `null` causa `NullPointerException`.

### 3.1) Testes automatizados (JUnit)

**`qwen/qwen3.6-27b`** cobriu:
- Médias exatas (múltiplos valores, valor único, valores iguais)
- Valores negativos
- (resposta interrompida pelo limite de tokens antes de cobrir todos os edge cases)

**`openai/gpt-oss-120b`** cobriu:
- Caso normal, elemento único, valores negativos, mistura de positivos/negativos
- Lista vazia → `ArithmeticException`
- Lista `null` → `NullPointerException`
- Overflow de `int` com valores grandes

```java
class CalculateAverageTest {

    private final CalculateAverage sut = new CalculateAverage();

    @Test
    void testNormalCase() {
        List<Integer> grades = Arrays.asList(8, 7, 9, 6, 10);
        assertEquals(8.0, sut.calculateAverage(grades));
    }

    @Test
    void testSingleElement() {
        assertEquals(5.0, sut.calculateAverage(Collections.singletonList(5)));
    }

    @Test
    void testNegativeGrades() {
        assertEquals(-4.0, sut.calculateAverage(Arrays.asList(-3, -7, -2)));
    }

    @Test
    void testMixedGrades() {
        assertEquals(0.0, sut.calculateAverage(Arrays.asList(-5, 0, 5)));
    }

    @Test
    void testEmptyListThrows() {
        assertThrows(ArithmeticException.class,
                () -> sut.calculateAverage(Collections.emptyList()));
    }

    @Test
    void testNullListThrows() {
        assertThrows(NullPointerException.class, () -> sut.calculateAverage(null));
    }
}
```

### 3.2) Documentação (Javadoc)

**`qwen/qwen3.6-27b`**:

```java
/**
 * Calcula a média aritmética de uma lista de notas.
 *
 * @param grades lista de notas inteiras a serem consideradas.
 *               Não pode ser {@code null} nem vazia.
 *
 * @return a média aritmética das notas fornecidas.
 *
 * @throws IllegalArgumentException se {@code grades} for {@code null}.
 * @throws ArithmeticException      se {@code grades} for vazia (divisão por zero).
 *
 * @see java.util.List
 */
```

**`openai/gpt-oss-120b`** — além da documentação, propôs a correção do bug de divisão inteira e da validação de entrada diretamente no código:

```java
/**
 * Calculates the arithmetic mean of a list of integer grades.
 *
 * <p>This method iterates over the supplied {@code grades}, sums the values,
 * and divides the total by the number of elements to obtain the average.
 * The result is returned as a {@code double} to preserve any fractional part.</p>
 *
 * @param grades a {@link List} of {@link Integer} values representing the grades;
 *               must not be {@code null} and must contain at least one element
 * @return the average of the grades as a {@code double}
 * @throws IllegalArgumentException if {@code grades} is {@code null} or empty
 */
public double calculateAverage(List<Integer> grades) {
    if (grades == null || grades.isEmpty()) {
        throw new IllegalArgumentException("The grades list must not be null or empty.");
    }
    int sum = 0;
    for (Integer grade : grades) {
        sum += grade;
    }
    return (double) sum / grades.size();
}
```

### Comparação entre os modelos

| | `qwen/qwen3.6-27b` | `openai/gpt-oss-120b` |
|---|---|---|
| Testes gerados | Parciais (cortados pelo limite de tokens) | Completos, incluindo overflow |
| Documentação | Javadoc simples com `@throws` | Javadoc completo + correção do bug de divisão inteira aplicada ao código |
| Observação | Também identificou o bug de divisão inteira na análise, mas não o corrigiu no código de documentação | Corrigiu o bug diretamente (`(double) sum / grades.size()`) |

---

## Observações gerais

- Ambos os modelos identificaram corretamente os principais bugs em ambos os exercícios.
- `openai/gpt-oss-120b` tende a fornecer respostas mais completas e robustas, indo além do que foi pedido (ex: Locale, Unicode, correção proativa de bugs).
- `qwen/qwen3.6-27b` é mais direto, mas em respostas mais longas (Exercício 3) esbarrou no limite de tokens de saída da conta gratuita do Groq, cortando parte do resultado.
