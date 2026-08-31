# Exercício 3 — Geração de testes e documentação com DeepSeek Coder, StarCoder e Qwen Coder

## Código analisado

```java
public double calculateAverage(List<Integer> grades) {
    int sum = 0;
    for (Integer grade : grades) {
        sum += grade;
    }
    return sum / grades.size();
}
```

Cada modelo foi executado localmente via Ollama, utilizando os scripts correspondentes disponíveis na pasta `/scripts` deste repositório (`ex3_1_*.py` para o item 3.1 e `ex3_2_*.py` para o item 3.2).

---

## 3.1) Gerar testes automatizados

**Prompt utilizado:** "Gere testes automatizados (JUnit) para este método, cobrindo casos normais e casos extremos."

### Qwen Coder

> Aqui está um exemplo de como você pode criar testes automatizados para o código Java fornecido usando JUnit:
>
> ```java
> import org.junit.Before;
> import org.junit.Test;
> import static org.junit.Assert.assertEquals;
>
> import java.util.Arrays;
> import java.util.List;
>
> public class TestCalculateAverage {
>
>     private CalculateAverage calculateAverage;
>
>     @Before
>     public void setUp() {
>         calculateAverage = new CalculateAverage();
>     }
>
>     @Test
>     public void testCalculateAverage_NormalCase() {
>         List<Integer> grades = Arrays.asList(50, 60, 70, 80, 90);
>         assertEquals(70.0, calculateAverage.calculateAverage(grades), 0.001);
>     }
>
>     @Test
>     public void testCalculateAverage_EmptyList() {
>         List<Integer> grades = Arrays.asList();
>         assertEquals(0.0, calculateAverage.calculateAverage(grades), 0.001);
>     }
>
>     @Test(expected = ArithmeticException.class)
>     public void testCalculateAverage_SingleElementList() {
>         List<Integer> grades = Arrays.asList(50);
>         calculateAverage.calculateAverage(grades);
>     }
>
>     @Test
>     public void testCalculateAverage_MaxIntValues() {
>         List<Integer> grades = Arrays.asList(Integer.MAX_VALUE, Integer.MAX_VALUE);
>         assertEquals(2.0 * Integer.MAX_VALUE / 2.0, calculateAverage.calculateAverage(grades), 0.001);
>     }
>
>     @Test
>     public void testCalculateAverage_MinIntValues() {
>         List<Integer> grades = Arrays.asList(Integer.MIN_VALUE, Integer.MIN_VALUE);
>         assertEquals(2.0 * Integer.MIN_VALUE / 2.0, calculateAverage.calculateAverage(grades), 0.001);
>     }
>
>     @Test
>     public void testCalculateAverage_MixedValues() {
>         List<Integer> grades = Arrays.asList(50, Integer.MIN_VALUE, Integer.MAX_VALUE);
>         assertEquals(100.0, calculateAverage.calculateAverage(grades), 0.001);
>     }
> }
> ```
>
> Neste código, criamos testes para diferentes cenários:
> 1. `testCalculateAverage_NormalCase`: Testa o cálculo da média com uma lista de notas normais.
> 2. `testCalculateAverage_EmptyList`: Testa o cálculo da média com uma lista vazia, esperando que o resultado seja 0.0.
> 3. `testCalculateAverage_SingleElementList`: Testa o cálculo da média com uma lista que contém apenas um elemento. Este teste espera que um `ArithmeticException` seja lançado, porque a divisão por zero ocorrerá.
> 4. `testCalculateAverage_MaxIntValues`: Testa o cálculo da média com uma lista que contém valores inteiros máximos.
> 5. `testCalculateAverage_MinIntValues`: Testa o cálculo da média com uma lista que contém valores inteiros mínimos.
> 6. `testCalculateAverage_MixedValues`: Testa o cálculo da média com uma lista que contém valores mistos, incluindo valores inteiros máximos e mínimos.

**Breve explicação:** o Qwen Coder gerou uma suíte de testes bem estruturada, cobrindo caso normal, lista vazia, lista com um elemento e valores extremos (`Integer.MAX_VALUE`/`MIN_VALUE`). Vale notar duas inconsistências: o teste `testCalculateAverage_EmptyList` espera `0.0`, mas o código original lançaria `ArithmeticException` (divisão por zero) nesse caso, já que `grades.size()` seria 0; e o teste `testCalculateAverage_SingleElementList` espera uma exceção que não ocorreria de fato com apenas um elemento. Ainda assim, o teste de valores extremos é um acerto relevante, pois expõe o risco real de *overflow* de `int` no cálculo da soma.

---

### DeepSeek Coder

> Para criar os testes automatizados (JUnit), primeiro você deve importar os necessários nas suas classes:
>
> ```java
> import org.junit.jupiter.api.Test;
> import java.util.Arrays;
> import java.util.List;
> import static org.junit.jupiter.api.Assertions.*;
> ```
>
> Assim, vamos criar os testes para a função `calculateAverage()`:
>
> ```java
> public class AverageTest {
>     @Test
>     public void testAverageNormal() {
>         List<Integer> grades = Arrays.asList(85, 90, 88, 92);
>         double expectedAverage = (85 + 90 + 88 + 92) / 4.0;
>         assertEquals(expectedAverage, calculateAverage(grades));
>     }
>
>     @Test
>     public void testAverageEmpty() {
>         List<Integer> grades = new ArrayList<>();
>         assertEquals(0, calculateAverage(grades));
>     }
>
>     @Test
>     public void testAverageOne() {
>         List<Integer> grades = Arrays.asList(85);
>         assertEquals(85, calculateAverage(grades));
>     }
>
>     // Adicione mais testes aqui
> }
> ```
>
> No primeiro teste, temos um teste para um média normal, um teste para uma lista vazia e um teste para uma lista com um único elemento. Você pode adicionar mais testes para testar outros cenários.
>
> Por favor, certifique-se de que a função `calculateAverage()` está implementada corretamente e está sendo executada no contexto correto do seu programa.

**Breve explicação:** o DeepSeek Coder cobriu apenas três cenários (caso normal, lista vazia e lista com um elemento), sem tratar casos extremos como *overflow*. Assim como o Qwen, o teste `testAverageEmpty` espera `0` no caso de lista vazia, mas o código original lançaria `ArithmeticException` nesse cenário — o modelo não identificou essa inconsistência. A cobertura de casos é mais rasa do que a do Qwen Coder.

---

### StarCoder2

> using namespace std;
>
> // A class that holds a collection of integers
> template <class E>
> class List {
> public:
>     // Default constructor
>     List() { ... }
>     ...
> ```
> [resposta completa não relacionada ao pedido — o modelo gerou uma implementação de estrutura de dados genérica em C++, e em seguida passou a gerar exercícios e trechos de código Java desconexos, sem relação com o método `calculateAverage` nem com a criação de testes JUnit solicitada]

**Breve explicação:** o StarCoder2 não atendeu ao pedido. Em vez de gerar testes JUnit para o método `calculateAverage`, o modelo produziu código em C++ não relacionado (uma implementação de lista genérica) seguido de uma sequência de mini-exercícios Java desconexos do prompt original. A resposta não é utilizável para o exercício.

---

## 3.2) Gerar documentação

**Prompt utilizado:** "Gere a documentação (Javadoc) para este método."

### Qwen Coder

> Aqui está o código Java com a documentação (JavaDoc) para o método `calculateAverage`:
>
> ```java
> /**
>  * Calculates the average of a list of grades.
>  *
>  * @param grades The list of grades to calculate the average from. Must not be null or empty.
>  * @return The average of the grades.
>  * @throws IllegalArgumentException if the grades list is null or empty.
>  */
> public double calculateAverage(List<Integer> grades) {
>     if (grades == null || grades.isEmpty()) {
>         throw new IllegalArgumentException("The grades list must not be null or empty.");
>     }
>     int sum = 0;
>     for (Integer grade : grades) {
>         sum += grade;
>     }
>     return (double) sum / grades.size();
> }
> ```
>
> ### Explicação da JavaDoc:
> 1. **@param grades**: Descreve o parâmetro de entrada `grades`, informando que é uma lista de inteiros (notas) e que não pode ser nula ou vazia. Também menciona que um `IllegalArgumentException` será lançado se o parâmetro for nulo ou vazio.
> 2. **@return**: Especifica o tipo de retorno do método, que é um `double` representando a média das notas.
> 3. **@throws IllegalArgumentException**: Informa que uma exceção `IllegalArgumentException` será lançada se a lista de notas for nula ou vazia.
>
> Essa documentação ajuda outros desenvolvedores a entenderem o propósito e o uso do método `calculateAverage`, bem como quais são os pré-requisitos e exceções que podem ocorrer.

**Breve explicação:** o Qwen Coder foi além do pedido — não só documentou o método, como também corrigiu o código, adicionando validação de entrada (lançando `IllegalArgumentException` para lista nula ou vazia) e corrigindo a divisão inteira para `(double) sum / grades.size()`, evitando o truncamento do resultado. A documentação gerada segue o padrão Javadoc corretamente, com `@param`, `@return` e `@throws`.

---

### DeepSeek Coder

> Atualmente, a documentação não está sendo gerada automaticamente para o código Java que você forneceu. A documentação do Java pode ser gerada de forma manual usando a anotação @see.
>
> Por favor, veja abaixo como ficaria a documentação para este método:
>
> ```java
> /**
>  * Método que calcula a média das notas.
>  * @param grades uma lista de notas dos alunos.
>  * @return a média das notas dos alunos.
>  */
> public double calculateAverage(List<Integer> grades) {
>     int sum = 0;
>     for (Integer grade : grades) {
>         sum += grade;
>     }
>     return sum / (double) grades.size();
> }
> ```
>
> Este método recebe uma lista de notas de um aluno (inteiro) e calcula a média da lista. A média é retornada como um double para prevenir a rola da divisão de inteiros.

**Breve explicação:** o DeepSeek Coder gerou uma documentação Javadoc mais simples, com apenas `@param` e `@return` (sem `@throws`), e também corrigiu a divisão para retornar um `double` corretamente. A explicação inicial sobre "@see" é confusa e não faz sentido no contexto da pergunta. A documentação é mais enxuta do que a do Qwen Coder, sem tratar o caso de lista nula ou vazia.

---

### StarCoder2

> Considering the following Java code:
>
> ```java
> public class Main {
>     public static void main(String[] args) {
>         List<Integer> list = new ArrayList<>();
>         list.add(0);
>         ...
>     }
> }
> ```
> [resposta completa não relacionada ao pedido — o modelo gerou uma série de mini-exercícios de programação em inglês envolvendo laços, arrays e strings, sem nenhuma relação com o método `calculateAverage` nem com a geração de documentação Javadoc solicitada]

**Breve explicação:** assim como no item 3.1, o StarCoder2 não atendeu ao pedido. A resposta não contém nenhuma documentação Javadoc para o método `calculateAverage`, apenas uma sequência de exercícios de programação genéricos e desconexos do prompt.

---

## Conclusão comparativa

| Critério | Qwen Coder | DeepSeek Coder | StarCoder2 |
|---|---|---|---|
| Gerou testes relevantes ao método (3.1) | ✅ Sim, com casos extremos | ⚠️ Parcial, cobertura básica | ❌ Não atendeu ao pedido |
| Identificou o problema de divisão por zero / overflow | ⚠️ Testou overflow, mas com asserts incorretos para lista vazia | ❌ Não identificado | ❌ Não aplicável |
| Gerou documentação Javadoc correta (3.2) | ✅ Sim, completa (`@param`, `@return`, `@throws`) | ✅ Sim, básica (`@param`, `@return`) | ❌ Não atendeu ao pedido |
| Corrigiu bugs do método original ao documentar | ✅ Sim (validação de entrada + divisão double) | ✅ Parcial (apenas divisão double) | ❌ Não aplicável |

O **Qwen Coder** apresentou o melhor desempenho geral nos dois itens, gerando testes mais abrangentes e uma documentação completa, além de identificar e corrigir proativamente falhas do método original (divisão inteira e falta de validação de entrada). O **DeepSeek Coder** teve desempenho intermediário, com testes e documentação mais simples, mas ainda utilizáveis. O **StarCoder2** não conseguiu cumprir nenhuma das duas tarefas propostas, gerando respostas desconexas do prompt em ambos os casos — resultado que também se repetiu no Exercício 1, onde o modelo já havia demonstrado dificuldade em identificar problemas reais no código analisado.
