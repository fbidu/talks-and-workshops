# Tipagem e Segurança

## O Que É Tipagem?

A maioria das linguagens de programação modernas trabalham com os conceitos de
variáveis e tipos. Uma variável é, em resumo, um pedaço nomeado de memória que
pode guardar um valor e o tipo da variável permite que esse valor seja interpretado
corretamente.

Sem um _tipo_, uma variável é simplesmente um conjunto de bits que pode ser lido
como um número inteiro, um caractere, um valor booleano e etc.

**inserir exemplo sobre a representação binária de diferentes letras e números**

Algumas linguagens de programação de nível baixo, que lidam mais diretamente com
o processador, normalmente possuem um conceito mais aberto em relação ao tipo.
Elas usualmente lidam simplesmente com uma _word_, uma palavra de bits em memória
e a interpretação desses bits fica por conta da pessoa desenvolvendo o código.
Se ela gravar na memória uma _word_ se referindo a um caractere, em geral nada
irá impedí-la de recuperar essa palavra como um inteiro, por exemplo, causando
uma quebra na interpretação dessa variável.

Tipos em Python possuem um aspecto bem diferente de tipos em várias outras linguagens,
isso acontece por conta do seu sistema de tipos. Vamos ver esse conceito agora.

## Sistema de Tipos

Um sistema de tipos é a forma como uma linguagem de programação sabe ou calcula
os tipos de suas variáveis. Esse sistema também governa como o tipo de uma variável
pode ou não mudar ao longo do ciclo de vida do seu código.

A primeira característica, como a linguagem sabe o tipo de uma variável, pode
ocorrer de duas formas: explícita ou implícita. Como o nome sugere, numa linguagem
de tipagem explícita, o tipo de uma variável é escrito de alguma forma no código.
Isso é conhecido como "declaração do tipo". Exemplos de linguagens assim são C e
Java.

```c
char linguagem = 'C';
int anoDeSurgimento = 1970;
```

```java
String linguagem = "Java";
int anoDeSurgimento = 1990;
```
Outras linguagens, como Python, PHP e JavaScript tem a sua tipagem implícita. Em
geral, o interpretador dessas linguagens calcula o tipo de uma variável ao longo
da execução do código

```python
linguagem = "Python"
ano_de_surgimento = 1991
```

```php
$linguagem = "PHP";
$anoDeSurgimento = 1995;
```

```javascript
var linguagem = "JavaScript";
var anoDeSurgimento = 1996;
```

_Go tem tipagem mista!_

```go
var linguagem string
linguagem = "Go"

anoDeSurgimento := 2009
```
