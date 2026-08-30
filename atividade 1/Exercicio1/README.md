# Exercício 1 — Análise de código Java com DeepSeek Coder, StarCoder e Qwen Coder
## Código analisado
java
public String getUserInitials(String firstName, String lastName) {
    return firstName.substring(0, 1).toUpperCase()
            + lastName.substring(0, 1).toUpperCase();
}
### Prompt utilizado

Considere o seguinte código Java: [código acima]. Tem algum bug nesse código? Algo que pode comprometer a funcionalidade dele? Caso sim, me aponte os problemas, e corrija o código por favor.

* Cada modelo foi executado localmente via Ollama, utilizando o script correspondente disponível na pasta /scripts deste repositório.

## Respostas dos modelos (1.1 e 1.2) Qwen Coder
Não há bugs aparentes neste código. A função `getUserInitials()` recebe como parâmetros dois nomes de usuários, `firstName` e `lastName`, e retorna uma string que contém as iniciais de ambos os nomes em maiúsculas.

No entanto, há alguns possíveis problemas e melhorias que podem ser feitas nesse código:

1. Tratamento de entradas nulas: Se `firstName` ou `lastName` forem `null`, um `NullPointerException` será lançado. Para evitar isso, você pode adicionar verificações nulidade:

public String getUserInitials(String firstName, String lastName) {
    if (firstName == null || lastName == null) {
        throw new IllegalArgumentException("Nome e sobrenome não podem ser nulos.");
    }
    return firstName.substring(0, 1).toUpperCase()
            + lastName.substring(0, 1).toUpperCase();
}

2. Tratamento de entradas vazias: Se `firstName` ou `lastName` forem vazios, um `StringIndexOutOfBoundsException` será lançado. Para evitar isso, você pode verificar se as strings são vazias antes de usar `substring()`:

public String getUserInitials(String firstName, String lastName) {
    if (firstName == null || lastName == null || firstName.isEmpty() || lastName.isEmpty()) {
        throw new IllegalArgumentException("Nome e sobrenome não podem ser vazios.");
    }
    return firstName.substring(0, 1).toUpperCase()
            + lastName.substring(0, 1).toUpperCase();
}

3. Consideração de múltiplas palavras no nome: Se `firstName` ou `lastName` contiverem múltiplas palavras, apenas a inicial da primeira palavra será retornada. Se deseja considerar todas as palavras, você precisará dividir as strings e tratar cada palavra individualmente.

4. Consideração de acentuação e caracteres especiais: A função atual não considera caracteres acentuados e especiais. Se deseja suportar esses caracteres, você precisará usar uma abordagem mais complexa para manipulação de strings, como usar uma biblioteca de processamento de texto.

* Breve explicação: o Qwen Coder identificou corretamente o principal risco do código — exceções (NullPointerException e StringIndexOutOfBoundsException) ao receber entradas nulas ou vazias — e corrigiu lançando uma exceção explícita (IllegalArgumentException), o que torna o erro visível e obriga o tratamento adequado por quem chama o método. Também levantou pontos extras (nomes compostos, acentuação) como sugestões de melhoria, não como bugs.

## DeepSeek Coder
O código Java que você compartilhou não contém erros lógicos significativos, mas há alguns aspectos que podem ser melhorados para garantir que ele funcione corretamente em todos os casos possíveis. Aqui estão algumas considerações:

1. Tratamento de Cadeias Vazias ou Nulas: Se `firstName` ou `lastName` for `null` ou vazia (""), a chamada `substring(0, 1)` causará um `StringIndexOutOfBoundsException`.

2. Acentuação e Caracteres Especiais: O código assume que os nomes não contêm caracteres especiais ou acentuação. Se isso for um problema, pode ser necessário tratar esses casos.

3. Caso em que o Nome Tem Apenas Um Caractere: Se `firstName` ou `lastName` tiver apenas um caractere, o código funcionará corretamente. Caso contrário, `substring(0, 1)` irá funcionar adequadamente.

4. Formatação: A forma como o nome é formatado pode não ser adequada para todos os casos. Por exemplo, se o nome for "John Doe", o resultado será "JD", o que parece correto, mas se o nome for "Juan", o resultado será "JU", o que pode não ser desejável para todos.

Correção e Melhoria do Código

Para garantir que o código funcione corretamente em todos os casos possíveis, podemos adicionar verificações adicionais para lidar com os casos em que `firstName` ou `lastName` são `null` ou vazias, e podemos garantir que o nome seja formatado corretamente.

public String getUserInitials(String firstName, String lastName) {
    if (firstName == null || firstName.isEmpty()) {
        firstName = " "; // Ou qualquer outra string padrão que você desejar
    }
    if (lastName == null || lastName.isEmpty()) {
        lastName = " "; // Ou qualquer outra string padrão que você desejar
    }
    return firstName.substring(0, 1).toUpperCase()
           + lastName.substring(0, 1).toUpperCase();
}

* Breve explicação: o DeepSeek Coder também identificou o risco de StringIndexOutOfBoundsException com entradas nulas ou vazias, mas a correção proposta é mais frágil do que a do Qwen: em vez de lançar um erro, substitui a entrada inválida por um espaço em branco (" "), evitando o crash de forma silenciosa — o que mascara o problema real em vez de sinalizá-lo.

## StarCoder2
O código está correto e sem nenhum problema. Ele é para gerar inicials de um nome, que são 2 letras, para os dois primeiros caracteres do primeiro nome e do primeiro nome e do sobrenome.

Porém, a função `toUpperCase()` que você utilizou na string final, pode não fazer sentido quando a função `substring(0, 1)` que você está utilizando, pois ela retornará a primeira letra do nome em letras minúsculas, e depois você quebraria essa string em 2 partes e transformaria a primeira letra em maiúscula.

Assim, o código ficaria assim:

public String getUserInitials(String firstName, String lastName) {
    return firstName.substring(0, 1).toUpperCase() + lastName.substring(0, 1).toUpperCase();
}

Se você quiser que a função retorne 4 letras (primeiro nome, primeiro sobrenome e segunda letra do primeiro nome e segunda letra do sobrenome), você precisaria incluir um terceiro parâmetro na chamada da função, e a chamada não deveria alterar a string de retorno. Ainda assim, essa é uma mudança simples para a responsabilidade de manter o código funcional.

public String getUserInitials(String firstName, String lastName) {
    return firstName.substring(0, 1).toUpperCase() + lastName.substring(0, 1).toUpperCase() + firstName.substring(1, 2).toUpperCase() + lastName.substring(1, 2).toUpperCase();
}

* Breve explicação: o StarCoder2 não identificou o risco de exceção com entradas nulas ou vazias, considerando o código correto. O raciocínio apresentado sobre substring()/toUpperCase() é confuso e não corresponde a um problema real no código original — a "correção" sugerida no primeiro bloco é, na prática, idêntica ao código original. A segunda sugestão (retornar 4 letras) muda o comportamento da função, mas quebraria com nomes de um único caractere, já que usa substring(1, 2).

### Conclusão comparativa 
Critério	Qwen Coder	DeepSeek Coder	StarCoder2
Identificou o risco de exceção com entradas nulas/vazias	✅ Sim	✅ Sim	❌ Não
Correção evita o problema de forma adequada	✅ Sim (erro explícito)	⚠️ Parcial (mascara com valor padrão)	❌ Não corrigiu o problema real

Qwen Coder e DeepSeek Coder identificaram corretamente a principal falha do código (ausência de tratamento para null/string vazia). Entre os dois, a correção do Qwen Coder é mais robusta, pois lança uma exceção explícita em vez de mascarar o erro. O StarCoder2 não identificou o problema real e sua resposta apresentou um raciocínio inconsistente sobre o código.
