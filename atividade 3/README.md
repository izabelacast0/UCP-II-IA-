# Lista de Exercícios 1 — Respostas dos Modelos (Groq)

Modelos utilizados: `qwen/qwen3.6-27b` e `openai/gpt-oss-120b`, via API do Groq (https://console.groq.com/keys).

---

## Exercício 1

Código analisado:

```java
public String getUserInitials(String firstName, String lastName) {
    return firstName.substring(0, 1).toUpperCase()
            + lastName.substring(0, 1).toUpperCase();
}
```

### Resposta — qwen/qwen3.6-27b

## Análise de Bugs

Sim, há **três problemas** que podem comprometer a funcionalidade:

### 1. `NullPointerException`
Se `firstName` ou `lastName` forem `null`, a chamada a `.substring()` ou `.toUpperCase()` lança uma `NullPointerException`.

```java
getUserInitials(null, "Silva"); // 💥 NPE
```

### 2. `StringIndexOutOfBoundsException`
Se qualquer um dos parâmetros for uma string **vazia** (`""`), o `substring(0, 1)` falha porque não existe caractere no índice 0.

```java
getUserInitials("", "Silva"); // 💥 IndexOutOfBounds
```

### 3. Espaços em branco em extremidades
Se o nome tiver espaço no início (ex.: `"  João"`), o `substring(0, 1)` retorna `" "` (um espaço) e o resultado final fica `" J"` em vez de `"JS"`.

```java
getUserInitials("  João", "Silva"); // retorna " J" em vez de "JS"
```

---

## Código Corrigido

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

### O que mudou e por quê

| Proteção | Motivo |
|---|---|
| Verificação de `null` | Evita `NullPointerException` |
| `.trim()` | Remove espaços em branco nas bordas antes de extrair a inicial |
| `.isEmpty()` após o trim | Evita `StringIndexOutOfBoundsException` quando a string é vazia ou contém apenas espaços |
| Retorno `""` em casos inválidos | Comportamento previsível; você pode ajustar para `null`, `null-safe` default, ou lançar uma `IllegalArgumentException` conforme a política do projeto |

### Observação adicional

Se o seu domínio permite **apenas um sobrenome** (ou vários, como "da Silva"), o código acima já lida com o primeiro caractere do último nome. Se quiser a inicial de **cada parte** do nome completo (ex.: "da Silva" → "DS"), a lógica mudaria um pouco. Mas para o contrato atual (`firstName` + `lastName`), o código corrigido cobre os casos de falha de forma segura.

**Comentário:** resposta direta e enxuta, cobrindo os 3 bugs centrais (null, string vazia, espaços) sem se estender além do que foi pedido.

---

### Resposta — openai/gpt-oss-120b

### Problemas do código original

```java
public String getUserInitials(String firstName, String lastName) {
    return firstName.substring(0, 1).toUpperCase()
            + lastName.substring(0, 1).toUpperCase();
}
```

1. **`NullPointerException`** – se `firstName` ou `lastName` for `null` o método lança a exceção antes de chegar ao `return`.

2. **`StringIndexOutOfBoundsException`** – quando o nome ou o sobrenome está **vazio** (`""`) ou contém apenas espaços, a chamada `substring(0, 1)` tenta acessar um índice que não existe.

3. **Espaços em branco antes ou depois do nome** – `"  Ana"` ou `"Silva "` resultariam nas iniciais "` A`" (espaço) e "`S`". O comportamento esperado normalmente é ignorar esses espaços.

4. **`toUpperCase()` sem especificar `Locale`** – a conversão para maiúsculas depende da *locale* padrão da JVM. Em algumas línguas (ex.: turco) o resultado pode ser inesperado (`i` → `İ`). Para garantir comportamento consistente devemos usar `Locale.ROOT` (ou a locale do usuário, se houver).

5. **Concatenação com `+`** – funciona, mas cria objetos `String` intermediários. Não é um bug, porém usar `StringBuilder` deixa a intenção mais clara e evita a criação de objetos extras.

---

### Código corrigido e mais robusto

```java
import java.util.Locale;
import java.util.Objects;

/**
 * Utility class for handling user names.
 */
public final class NameUtils {

    private NameUtils() {
        // classe utilitária – impede instanciação
    }

    /**
     * Retorna as iniciais do usuário (primeira letra do primeiro nome
     * e primeira letra do sobrenome), sempre em maiúsculas.
     *
     * <p>São lançadas {@link IllegalArgumentException} se algum dos
     * parâmetros for {@code null}, vazio ou composto apenas de espaços.</p>
     *
     * @param firstName nome próprio (não pode ser {@code null} nem vazio)
     * @param lastName  sobrenome (não pode ser {@code null} nem vazio)
     * @return as duas iniciais em maiúsculas, ex.: "JS"
     */
    public static String getUserInitials(String firstName, String lastName) {
        // 1️⃣ Validação de nulidade
        Objects.requireNonNull(firstName, "firstName não pode ser null");
        Objects.requireNonNull(lastName, "lastName não pode ser null");

        // 2️⃣ Remover espaços em branco nas extremidades
        String f = firstName.trim();
        String l = lastName.trim();

        // 3️⃣ Garantir que ainda haja ao menos um caractere
        if (f.isEmpty()) {
            throw new IllegalArgumentException("firstName não pode ser vazio ou apenas espaços");
        }
        if (l.isEmpty()) {
            throw new IllegalArgumentException("lastName não pode ser vazio ou apenas espaços");
        }

        // 4️⃣ Obter o código do primeiro caractere (suporta Unicode completo)
        int firstCodePoint = f.codePointAt(0);
        int lastCodePoint  = l.codePointAt(0);

        // 5️⃣ Converter para maiúsculas de forma independente da Locale
        int firstUpper = Character.toUpperCase(firstCodePoint);
        int lastUpper  = Character.toUpperCase(lastCodePoint);

        // 6️⃣ Construir a string final (usando StringBuilder apenas por clareza)
        return new StringBuilder(2)
                .appendCodePoint(firstUpper)
                .appendCodePoint(lastUpper)
                .toString();
    }
}
```

#### Explicação passo‑a‑passo

| Passo | O que faz | Por que é importante |
|------|-----------|----------------------|
| **1️⃣** | `Objects.requireNonNull` | Garante falha rápida e clara caso algum argumento seja `null`. |
| **2️⃣** | `trim()` | Elimina espaços antes/depois do nome, evitando que a inicial seja um espaço. |
| **3️⃣** | Checagem `isEmpty()` | Evita `StringIndexOutOfBoundsException` quando o nome fica vazio após o `trim()`. |
| **4️⃣** | `codePointAt(0)` | Lida corretamente com caracteres Unicode que ocupam mais de um `char` (ex.: emojis, letras acentuadas fora do BMP). |
| **5️⃣** | `Character.toUpperCase(..., Locale.ROOT)` (via `Character.toUpperCase(int)`) | Converte de forma previsível, independente da configuração regional da JVM. |
| **6️⃣** | `StringBuilder.appendCodePoint` | Monta a string final sem criar objetos intermediários desnecessários. |

---

### Como usar

```java
public class Demo {
    public static void main(String[] args) {
        System.out.println(NameUtils.getUserInitials("Ana", "Silva"));   // → "AS"
        System.out.println(NameUtils.getUserInitials("  João", "  Souza ")); // → "JS"
        System.out.println(NameUtils.getUserInitials("élise", "d'Ávila")); // → "ÉD"
    }
}
```

---

### Testes rápidos (JUnit 5)

```java
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class NameUtilsTest {

    @Test
    void normalNames() {
        assertEquals("AS", NameUtils.getUserInitials("Ana", "Silva"));
        assertEquals("JS", NameUtils.getUserInitials("João", "Souza"));
    }

    @Test
    void comEspacos() {
        assertEquals("AB", NameUtils.getUserInitials("  Alice ", "  Bob "));
    }

    @Test
    void unicode() {
        assertEquals("ÉD", NameUtils.getUserInitials("élise", "d'Ávila"));
    }

    @Test
    void nullArguments() {
        assertThrows(NullPointerException.class,
                () -> NameUtils.getUserInitials(null, "Silva"));
        assertThrows(NullPointerException.class,
                () -> NameUtils.getUserInitials("Ana", null));
    }

    @Test
    void vazios() {
        assertThrows(IllegalArgumentException.class,
                () -> NameUtils.getUserInitials("", "Silva"));
        assertThrows(IllegalArgumentException.class,
                () -> NameUtils.getUserInitials("Ana", "   "));
    }
}
```

Esses testes confirmam que a implementação:

* trata `null` e strings vazias adequadamente,
* ignora espaços em branco indesejados,
* funciona com caracteres Unicode,
* produz sempre as duas iniciais em maiúsculas, independentemente da *locale*.

#### Resumindo
O código original funciona apenas em condições ideais (nomes não‑nulos, não‑vazios e sem espaços). Ao adicionar validações, tratamento de whitespace, uso de `Locale.ROOT` e manipulação segura de Unicode, eliminamos os principais pontos de falha que poderiam "comprometer a funcionalidade" em produção.

**Comentário:** resposta bem mais completa que a do Qwen — foi além do pedido, trazendo Locale, suporte a Unicode/codePoints e testes JUnit já inclusos, sem que isso tivesse sido solicitado.

---

## Exercício 3

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

### Resposta — qwen/qwen3.6-27b (Testes automatizados)

```java
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.extension.ExtendWith;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import org.junit.jupiter.params.provider.CsvSource;
import static org.junit.jupiter.api.Assertions.*;

import java.util.*;

@ExtendWith(org.junit.jupiter.api.extension.ExtensionRegister.class)
class CalculateAverageTest {

    // --- Casos normais ---

    @Test
    @DisplayName("Média de múltiplos valores inteiros -> resultado exato")
    void average_multipleIntegers_exactResult() {
        List<Integer> grades = List.of(80, 90, 70, 100);
        assertEquals(85.0, new GradeCalc().calculateAverage(grades), 1e-9);
    }

    @Test
    @DisplayName("Média de lista com um único elemento")
    void average_singleElement() {
        List<Integer> grades = List.of(42);
        assertEquals(42.0, new GradeCalc().calculateAverage(grades), 1e-9);
    }

    @Test
    @DisplayName("Média de valores iguais")
    void average_allSameValues() {
        List<Integer> grades = List.of(7, 7, 7, 7, 7);
        assertEquals(7.0, new GradeCalc().calculateAverage(grades), 1e-9);
    }

    @Test
    @DisplayName("Média com valores negativos")
    void average_negativeValues() {
        List<Integer> grades = List.of(-10, -20, -30);
        assertEquals(-20.0, new GradeCalc().calculateAverage(grades), 1e-9);
    }

    @Test
    @DisplayName("Média com valores mistos (
```
*(resposta interrompida pelo modelo neste ponto)*

**Comentário:** a resposta foi cortada no meio do último teste. Isso aconteceu porque esse modelo gasta uma quantidade grande de tokens "pensando" antes de responder (bloco `<think>...</think>` retornado antes do código), e o limite de tokens de saída configurado na chamada da API (`max_tokens=800`) não foi suficiente para ele concluir. Também vale registrar que, antes de ajustarmos o script, essa mesma chamada chegou a falhar com `groq.RateLimitError: Error code: 429` (limite de tokens de saída por minuto da conta gratuita do Groq excedido). Adicionar `max_tokens` e uma pausa (`time.sleep`) entre as chamadas resolveu o erro 429, mas não evitou o corte da resposta — para isso seria necessário aumentar ainda mais o `max_tokens`.

---

### Resposta — qwen/qwen3.6-27b (Documentação)

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
public double calculateAverage(List<Integer> grades) {
    int sum = 0;
    for (Integer grade : grades) {
        sum += grade;
    }
    return sum / grades.size();
}
```

**Comentário:** documentação concluída sem cortes (resposta bem mais curta que a dos testes). Vale notar que o `@throws IllegalArgumentException` documentado não corresponde ao comportamento real do código-fonte apresentado (que lançaria `NullPointerException` para lista nula, não `IllegalArgumentException`) — o modelo documentou o comportamento que *deveria* existir após uma validação, não o comportamento exato do código mostrado.

---

### Resposta — openai/gpt-oss-120b (Testes automatizados)

**JUnit 5 test class**

```java
package com.example;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

/**
 * Tests for {@link CalculateAverage#calculateAverage(List)}.
 */
class CalculateAverageTest {

    private final CalculateAverage sut = new CalculateAverage();

    @Test
    @DisplayName("Average of a normal list of positive grades")
    void testNormalCase() {
        List<Integer> grades = Arrays.asList(8, 7, 9, 6, 10);
        // sum = 40, size = 5 -> 40/5 = 8 (int division, then cast to double)
        double result = sut.calculateAverage(grades);
        assertEquals(8.0, result);
    }

    @Test
    @DisplayName("Average with a single element list")
    void testSingleElement() {
        List<Integer> grades = Collections.singletonList(5);
        double result = sut.calculateAverage(grades);
        assertEquals(5.0, result);
    }

    @Test
    @DisplayName("Average with negative grades")
    void testNegativeGrades() {
        List<Integer> grades = Arrays.asList(-3, -7, -2);
        // sum = -12, size = 3 -> -12/3 = -4
        double result = sut.calculateAverage(grades);
        assertEquals(-4.0, result);
    }

    @Test
    @DisplayName("Average with a mixture of positive and negative values")
    void testMixedGrades() {
        List<Integer> grades = Arrays.asList(-5, 0, 5);
        // sum = 0, size = 3 -> 0/3 = 0
        double result = sut.calculateAverage(grades);
        assertEquals(0.0, result);
    }

    @Test
    @DisplayName("Empty list should throw ArithmeticException (division by zero)")
    void testEmptyListThrows() {
        List<Integer> grades = Collections.emptyList();
        assertThrows(ArithmeticException.class, () -> sut.calculateAverage(grades));
    }

    @Test
    @DisplayName("Null argument should throw NullPointerException")
    void testNullListThrows() {
        assertThrows(NullPointerException.class, () -> sut.calculateAverage(null));
    }

    @Test
    @DisplayName("Large values causing int overflow")
    void testOverflow() {
        // Integer.MAX_VALUE = 2_147_483_647
        List<Integer
```
*(resposta interrompida pelo modelo neste ponto)*

**Comentário:** essa resposta também foi cortada, mas bem mais tarde que a do Qwen — chegou a completar 6 dos 7 testes planejados (só o teste de overflow ficou incompleto). O `gpt-oss-120b` parece ter usado seu orçamento de tokens de forma mais eficiente que o Qwen para essa tarefa, já que não expõe um bloco de raciocínio explícito antes da resposta.

---

### Resposta — openai/gpt-oss-120b (Documentação)

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

**Comentário:** diferente do Qwen, esse modelo não documentou apenas o código original — ele reescreveu o método aplicando a correção do bug de divisão inteira (`(double) sum / grades.size()`) e adicionando a validação de entrada (`if (grades == null || grades.isEmpty())`), tornando a documentação (`@throws IllegalArgumentException`) coerente com o comportamento do código que ele mesmo entregou.
