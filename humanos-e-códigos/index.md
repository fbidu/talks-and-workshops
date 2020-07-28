# Humanos e Códigos

#### Para _quem_ a gente escreve?



Aperte a tecla `"s"` para ver as notas de apresentação!



### Oi, eu sou o (Felipe) Bidu!

* [github.com/fbidu](https://github.com/fbidu)
* Instituto de Computação - UNICAMP
* Desenvolvedor na [Ingresse](https://ingresse.com)



# As _maravilhas_ da nossa área

Note:
* Eu vou começar falando sobre algumas características gerais da área de desenvolvimento de software em si.
* Existe um debate se a chamada 'engenharia de software' é ou não uma engenharia
  de verdade e onde ela se encaixa no conjunto de áreas técnicas e científicas
* Seja como for, a nossa área tem uma capacidade que é rara e muito importante


## Introspecção

_A capacidade de resolver problemas de software fazendo *OUTRO* software_

Note:
* A introspecção - a capacidade que nós temos de construirmos softwares que resolvem
  problemas que nós temos no processo de construção de softwares - é um aspecto
  da nossa área que pode passar despercebido por nós mas, quando começamos a
  prestar atenção, ela tá em todo lugar


![](https://media.giphy.com/media/mXuPww8oyFUCP22tXi/giphy.gif)

Note:
* Por exemplo, uma "sprint" nossa por de começar com nós ou algum colega usando
  de softwares como Jira ou Trello para descrever e gerenciar as tarefas que
  precisamos executar dentro do software que estamos autorando


![](https://media.giphy.com/media/cFkiFMDg3iFoI/giphy.gif)
Note:
* Então a gente utiliza outro software como o Git pra organizar nosso código,
  colaborar com outras pessoas, etc


![](https://media.giphy.com/media/CDZwopbecAbIc/giphy.gif)
Note:
* Finalmente vai chegando a hora do deploy! Aí nós temos toda uma nova pilha,
  carinhosamente chamada de "stack", de software para lidar. Containers, servidores
  de CI, servidores de CD, os próprios servidores em produção, paineis de monitoramento
  etc, etc, etc


![](https://media.giphy.com/media/kwEmwFUWO5Ety/giphy.gif)
Note:
* No fim de uma feature, uma única pessoa vai ter contato com uma dezena de softwares
  diferentes - tudo para que consiga desenvolver um único software.
* Das nossas IDEs e editores, passando por nossos linters, testers, sistemas de
  automação e etc o nosso código é processado por uma quantidade gigantesca
  de outros softwares ao longo do caminho de desenvolvimento


![](https://media.giphy.com/media/zrdUjl6N99nLq/giphy.gif)

Isso tudo é ruim?
Note:
* Eu acho essa introspecção, essa capacidade que desenvolvimento de software tem
de olhar para si e usar da própria área de conhecimento para resolver seus problemas,
uma coisa incrível.
* No entanto, essa nossa facilidade em criar softwares novos para resolver problemas
do processo de criação do software pode fazer com que a gente entre num ciclo
vicioso, pensando mais em software sobre software sobre software do que sobre
os outros aspectos do nosso processo criativo como nossos colegas, nosso local de trabalho,
o mercado em que atuamos, as relações éticas cada vez mais complicadas entre
geração e uso de dados pessoais de nossos clientes, entre outras coisas.


![](https://media.giphy.com/media/ftAyb0CG1FNAIZt4SO/giphy.gif)
Note:
* De fato, com a popularização de computadores, celulares e dispositivos IoT,
as relações entre o mundo digital e a vida física das pessoas se torna cada
vez mais complexa.
* Nós não podemos mais falar de segurança da informação, por exemplo, sem pensar
no impacto bastante real que essas decisões terão na vida pessoal de nossos usuários
* Também não podemos mais discutir sobre a sistematização e o escalonamento de 
certos mercados através de uma solução via software sem considerar as relações
sociais e comerciais que já estavam envolvidas naquele mercado e que com
certeza serão aprofundadas e intensificadas por nossos códigos


![](dieselgate.jpg)
[Dieselgate](https://www.ednh.news/vw-dieselgate-fraud-timeline-of-a-scandal/)
Note:
* Em nossa defesa - a nossa área ainda está engatinhando. O primeiro software
comercial foi fabricado no começo da década de 60. Desenvolvimento de software
é praticamente um bebê perto de áreas como a construção civil.
* Por outro lado, essas discussões estão se tornando cada vez mais importantes.
Eu atuo com desenvolvimento de software faz muitos anos, a primeira vez que eu
vi uma discussão séria sobre ética na nossa área foi em 2015, quando descobriram
o Dieselgate da Volkswagen, um software que deturpava testes de emissão de poluentes.
Vocês podem ver mais informações nesse link



![babysteps](https://media.giphy.com/media/HNtm9TDgxGza8/giphy.gif)
Note:
* Tem muita coisa legal e importante para ser discutida entre essas relações
humanos-software mas vamos começar com baby steps.
* Hoje eu quero discutir com vocês particularmente a parte do desenvolvimento de
software que provavelmente é mais próxima do desenvolvedor em si - o código.


![](func.png)
Note:
* Vamos começar considerando a pergunta - o quê ou quem é o principal leitor
do nosso código?
* Pode ser tentador responder que o principal "público-alvo" de um código é
um computador. Afinal, escrevemos código para fazer a máquina trabalhar
por nós!
* Por outro lado, nós sabemos que alguns aspectos de um código como uma escolha
concisa de nomes para funções, classes e variáveis, uma formatação bem feita
e coesa, documentação sobre as APIs expostas pelos nossos códigos e etc são
aspectos importantes.


![](modern-compiler.png)
Note:
* O que vocês estão vendo agora é um diagrama geral de um compilador,
com as etapas que um código passa, desde começar ali em cima no canto esquerdo
até chegar em alguma coisa que um computador vai de fato ler, no canto inferior direito. 
* O nosso código em seu aspecto mais amplo só de fato importa pra esse processo
até mais ou menos o terceiro quadradinho. Depois da quinta etapa - "translate" -
nem mesmo a linguagem de programação que a gente usou importa mais. E a gente
não tá nem na metade do caminho até o computador!
* Então eu volto a perguntar, será que o nosso código é feito para ser lido pelo
computador?



![:scale 50%](josh-calabrese-Ev1XqeVL2wI-unsplash.jpg)
Note:
* Hoje, eu vim aqui para defender que não importa o tanto de software que a
gente usa para escrever software, não importa que um processador esteja
no final da cadeia de execução, códigos são escritos para serem lido
sobretudo por seres humanos.
* A questão central para mim é que software no sentido de um produto digital ou
no sentido comumente usado junto de métodos de engenharia de software, esses softwares não costumam ser pequenas porções de código escritas em um dia por uma pessoa e
jogados fora no outro mas sim são obras colaborativas complexas nas quasi ideias são
materializadas _através_ do código.
* Em softwares assim, o código atua como um meio de comunicação de conceitos
abstratos pensados por um colega, compatilhado para outros e desenvolvido
colaborativamente por muitos.
* Antes de um código cair num pipeline de deploy que vai levâ-lo para um sistema
em produção, ele já passou e repassou por diversos olhos e mãos bastante humanos.
Esquecer ou falhar em prestar atenção de que um dos papeis principais de um
código é servir como meio de comunicação entre nós e nossos colegas pode nos
fazer cometer escolhas erradas na hora de julgar quais processos usar, quais
ferramentas usar, como organizar nosso trabalho, o que avaliar ao revisar
nossos códigos, entre outras coisas. Afinal, se o objetivo principal do código
não é bem compreendido, como que vamos otimizar de maneira correta o processo
de criação dele?


![:scale 50%](bob.png)
Note:
* Você talvez não esteja colocando muita fé no meu argumento central, de que
existe uma relação intrincada entre nosso código e os componentes bastante
humanos do desenvolvimento de software
* Você talvez pense como um certo autor de 'clean livros' sobre 'clean code'
nesse 'clean tweet' que alega "quando você lê código, a raça, religião, visão
política, gênero e oritentação do autor são irrelevantes e invisíveis! A única
coisa que você pode dizer sobre o auto é a sua habilidade de escrever código
bem organizado. Nada mais importa"


![:scale 50%](euvsbob.png)
Note:
* A minha resposta pra essa alegação bem duvidosa do Bob vocês podem ler depois
no meu Twitter, vou deixar fixado lá. Me sigam gente, eu de vez em quando posto
coisas sérias também!
* Como vocês podem ver aqui no começo da minha resposta, eu não sou um grande
fã dessa visão d'O Software como sendo essa entidade limpa, higienizada, livre
dos problemas e vieses da humanidade e etc
* No caso que estamos lidando aqui hoje, existe uma outra observação que eu acho
mais relevante


![:scale 50%](conway.jpg)
Note:
* Essa observação é a chamada Lei de Conway. Ela não é uma lei no sentido científico
do termo, mas ela é uma observação que tem se mostrado válida ao longo de diversos
testes desde a década de 60
* A lei de Conway diz que o software criado por uma organização tende a ter uma
estrutura que é um espelho da forma como a comunicação interna daquela organização
funciona
* Isso é, uma companhia que possui uma estrutura extremamente hierárquica e 
dividida em camadas terá dificuldades em montar uma arquitetura baseada em
microsserviços, uma vez que essa arquitetura demanda uma comunicação mais
livre, baseada em pequenos grupos autônomos
* Nesse ponto nós começamos a notar como a forma de comunicação entre nós, 
desenvolvedores, com o resto da nossa empresa é marcada em nossos softwares
* Se você quer fazer uma reorganização na estrutura do software da sua empresa,
por exemplo migrar de uma arquitetura monolítica em camadas para uma de microsserviços,
como anda na moda, é bem provável que focar só na arquitetura do código em si
sem pensar em como as pessoas se comunicam em geral vai causar uma tensão nessa
estrutura - você vai forçar o software pra um caminho que não encontra espelho
na forma como a empresa se organiza. Nessa situação, podemos usar a lei de
conway a nosso favor e, ao invés de fazermos uma observação passiva de como
estruturas de software seguem estruturas sociais, podemos iniciar uma mudança
no aspecto social para então favorecer uma mudança na estrutura do software.



## Código Comunica Ideias
Note:
* Um ponto importante nessa discussão é a visão de que o código atua como esse
  meio de transmissão de ideias.
* Ao considerarmos o código desse jeito, começamos a observar certos padrões de
  uso


```python
def test_feature_nova():
  """
  E se a gente adicionasse essa flag?
  """

  assert nosso_software.proposta(teste) == "olar!"
```
Note:
* Quem aqui utiliza de TDD ou participa de Code Dojos talvez já esteja mais
  por dentro dessa visão. Quer propor uma coisa nova em um pedaço de código?
  Que tal escrever um teste - que vai falhar - demonstrando o comportamento
  que você espera? Talvez isso ofereça uma visão mais clara do que você 
  pretende.
* Essa é uma estratégia que eu particularmente uso em projetos open source. A
  discussão se inicia com um pull request que implementa um teste falho. Esse
  teste vai funcionar se a ideia for implementada. A partir dele, podemos
  discutir muitas coisas legais


```python
# Soma a com b em x
x = a + b

# Imprime x
print(x)
```
Note:
* Um ponto de debate quando falamos em código são os comentários. Tem muitas
  abordagens possíveis.
* Uma delas que é relativamente famosa é que o seu código deveria ser óbvio
  tão óbvio que ele não precisa de comentários. Eu acho essa abordagem
  interessante na teoria mas nem sempre viável e pode ser na verdade
  contraprodutiva
* Escrever um código cheio de "gotchas" e usos exóticos da linguagem de fato
  é ruim e compromete a legibilidade mas, em alguns momentos, nós precisamos
  lançar mão de estruturas mais complexas. Tentar reescrever essas estruturas
  de forma 'óbvia' faz tanto sentido quanto escrever uma tese de doutorado
  usando apenas as 100 palavras mais comuns da língua portuguesa. Você vai
  acabar com um texto extremamente prolixo e que falha em representar o que
  você quer de forma clara


> Não escreva nos comentários nada que o código em si já não fala
Note:
* Uma sugestão que eu dou é que você olhe bem pro seu código e pense se aquele
  código em si é direto o suficiente. O comportamento dele depende de efeitos
  colaterais ou estados globais que não estão ali naquele trecho? Ele _causa_
  efeitos ou mudanças nesses estados que vão repercutir pelo sistema? Esses
  são exemplos bons de situação em que um comentário é bem-vindo


## Documentação != Comentário
Note:
* Na mesma área sobre comentários existe um outro ponto de debate que são as
  documentações. Basicamente uma pessoa que vai usar de uma função, classe,
  módulo, método, etc, não deveria precisar ler o código em si para utilizar
  suas ideias
* Embora o código-fonte desses elementos seja a implementação da ideia em si,
  uma boa documentação - pensando no escopo do código como uma entidade mais
  ampla - pode auxiliar bastante no esforço colaborativo


> Mas _o quê_ documentar??


```python
def fibonacci(n, cache=None)
    """
    Cálculo de fib. recursivo começando de n=0 e
    percorrendo até o máximo de recursão possível.
    Aceita um dicionário como cache. Se o cache
    for vazio, ele não é usado!
    """
```
Note:
* De novo, muitas escolas de pensamento diferentes, muitos guias diferentes e etc.
  Considere essa função em Python e a sua docstring "Cálculo de fib. recursivo
  começando de n=0 e percorrendo até o máximo de recursão possível. Aceita um
  dicionário como cache. Se o cache for vazio, ele não é usado!"
* Bom, definitivamente é uma docstring recheada! Mas pense na perspectiva de
  quem tá usando a função fibonacci. Essa pessoa não precisa saber de muita
  coisa que está acontecendo aí! O fato da estratégia ser recursiva dificilmente
  é uma informação tão importante para ser colocada no topo, a questão de um
  cache vazio não ser usada é bastante óbvia também
* Enfim, nesse caso, a estratégia que eu gosto de usar é escrever qual o objetivo
  principal daquela função em uma frase ou duas. Então eu descrevo os argumentos
  e talvez algum exemplo de uso. Também é importante documentarmos se o comportamento
  daquela função vai variar de acordo com estados globais ou se ela os altera.
  Detalhes de implementação, sobre como aquela função faz o que ela diz que
  faz são desnecessários na documentação.



> Lembre-se que APIs são INTERFACES
Note:
* APIs são estruturas comuns em uma arquitetura moderna. Mas quando pensamos ou
  discutimos APIs muitas vezes pulamos direto para coisas como REST, verbos
  HTTP e estruturas de JSON
* Vamos dar uma revisitada no conceito de API como sendo uma interface


> inter _feices_ vs inter _faces_
Note:
* O termo em inglês "interfeice" é usual e correto mas eu acho que o termo mais
  aportuguesado "interface" nos permite enxergar melhor uma interface como ela
  realmente é - um ponto de comunicação entre duas ou mais faces, entre duas ou
  mais entidades diferentes, cada uma com suas funcionalidades.
* E de novo estamos no meio de um problema de comunicação. APIs antes de lidarem
  com problemas de código, antes de lidarem com questões de implementação elas
  lidam com uma questão de comunicação entre um lado que oferece um certo recurso
  e outro lado que usa desse recurso
* Um código que implementa perfeitamente uma API mas que não oferece nenhuma forma
  boa dos potenciais clientes descobrirem suas funcionalidades e entender como
  utilizá-las, faz seu trabalho apenas parcialmente.
* Se você trabalha em uma companhia que tem uma equipe de back-end e uma de
  front-end trabalhando juntos, é bem fácil de relembrar o aspecto 'interface'
  de uma API, mas também pode ser bastante tentador comunicar o que um certo
  endpoint faz por meios informais. Mensagem no slack, áudio no whatsapp,
  passar um post-in com a especificação... E os próximos membros da equipe?
* Lembre-se do código como meio de comunicar ideias! Use e abuse de ferramentas
  de documentação automática!


[OpenAPI Initiative](https://www.openapis.org/)

[OpenAPI.Tools](https://openapi.tools/)


# Muito obrigado!

* felipe@felipevr.com
* [github.com/fbidu](https://github.com/fbidu)
* Twitter @fevir0




![so-many-tips](so-many.jpg)

Note:
* É normal a gente sair de conferências se sentido sobrecarregados de dicas
e ferramentas e técnicas novas


* Ter uma ampla carta de opções é fantástico <!-- .element: class="fragment" data-fragment-index="2" -->
* Nos permite fazer muita coisa legal <!-- .element: class="fragment" data-fragment-index="3" -->
* Mas, especialmente numa equipe, consistência é fundamental! <!-- .element: class="fragment" data-fragment-index="4" -->


* Liste as opções, discuta com a sua equipe e defina um padrão<!-- .element: class="fragment" data-fragment-index="2" -->
* Não se preocupe em definir tudo, não se preocupe em acertar de primeira. Defina
algumas linhas gerais<!-- .element: class="fragment" data-fragment-index="3" -->
* Qual analisador vocês vão usar? Com quais configurações? <!-- .element: class="fragment" data-fragment-index="4" -->
* E então recolha feedback da sua equipe quanto ao uso, modifique seus padrões
se necessário<!-- .element: class="fragment" data-fragment-index="5" -->


* Como de fato _usar_ um analisador estático no desenvolvimento?
* Ferramentas instaladas que não são usadas não servem pra nada!
* Minha sugestão: _hooks pre-commit_ e _CI_
Note:
* Uma questão que fica é como usar de fato essas coisas
* Se você abrir o meu computador e o de muito dev por aí, você provavelmente vai
encontrar um monte de ferramenta X que a gente instalou achando que ia ser
a solução dos nossos problemas e que nunca usamos de fato
* No caso de analisadores estáticos em geral, eu gosto de uma abordagem em duas
camadas, hooks pre-commit e scripts no servidor de CI


### Hooks Pre-Commit
* Códigos que o `git` pode invocar _antes_ de arquivos sofrerem commit
* Recomendo o uso do [pre-commit](https://pre-commit.com/) para gerenciar hooks
* Executam na máquina do desenvolvedor
* Evita que código não-conformante vá para o repositório

Note:
* Eu gosto muito da ideia de hooks pre-commit porque eles são executados antes do
código ser submetido e, caso eles falham, o código não passa
* Isso mantém o repositório limpo pois é preventivo. Você não precisa fazer
um outro commit que vai corrigir alguma coisa que uma ferramenta pegou dps
* O problema de hooks pre-commit normais é que eles não são registrados como
arquivos no git, então é difícil mantê-los de forma igual por toda uma equipe
* Eu gosto bastante do projeto pre-commit porque ele te apresenta uma forma
estruturada de colocar seus hooks dentro do projeto
* Você pode colocar uma execução do seu analisado estático favorito aqui e todo
mundo que mexer no projeto vai ter acesso as configurações


### Servidor de CI
* CI é a prática de manter toda uma base de código íntegra<!-- .element: class="fragment" data-fragment-index="2" -->
* Em geral existe um servidor em algum roda tarefas em cima do código novo como testes e
verificações<!-- .element: class="fragment" data-fragment-index="3" -->
* Eu gosto de colocar todos os analisadores estáticos ali também<!-- .element: class="fragment"data-fragment-index="4" -->
* Evita que um dev que não configurou pre-commit ou não está acostumado com a
equipe viole o estilo que foi combinado<!-- .element: class="fragment" data-fragment-index="5" -->


* Erros no servidor de CI são uma ótima forma de disseminar boas práticas!<!-- .element: class="fragment" data-fragment-index="2" -->
* Ao invés de simplesmente colocar um erro cru, coloque alguma referência sobre
a documentação de boas práticas ou até mesmo o contato de alguém mais sênior
que pode ajudar com o problema <!-- .element: class="fragment" data-fragment-index="3" -->
Note:
* Isso é uma coisa que eu gosto bastante mas não vejo muita gente usando
* Erros no servidor de CI podem ser usados para disseminar as boas práticas
da equipe
* Se as mesmas ferramentas são executadas no pre-commit e no CI e o código de
alguém quebrou por conta de alguma coisa no pre-commit, isso indica que a pessoa
não configurou direito o próprio ambiente
* O erro do CI é uma ótima oportunidade de colocar um texto claro sobre o que aconteceu,
sobre as boas práticas e até mesmo colocar o contato de alguém mais sênior que se
disponibilize a ajudar os colegas nessa situação



# Informação, Segurança & Produtividade
Note:
* Nessa parte da minha palestra eu vou tocar por cima de alguns pontos que eu
acho relevantes nessa discussão


* Desenvolver Software é uma tarefa humana
* Software é feito por humanos, muitas vezes para humanos
* Muitos problemas em Engenharia de Software são problemas de comunicação

Note:
* Uma coisa que muitas vezes passa despercebida é como programação e produção
de software é uma tarefa criativa, lotada de fatores humanos

* Por algum tempo - e algumas pessoas até hoje pensam assim - pensava-se que o
software era uma coisa absolutamente objetiva, livre das "impurezas" dos humanos
envolvidos no seu desenvolvimento

* Isso não poderia estar mais longe da verdade. O desenvolvimento de software é
uma tarefa bastante criativa e que sofre bastante influência dos fatores humanos
no processo

* Muitas vezes, equipes de software enroscam e não conseguem atingir sua eficiência
máxima não por conta de razões técnicas, por que algum treinamento ou conhecimento
está faltando ou coisa assim

* Muitas vezes as equipes acabam sofrendo muito com problemas que são relacionados
com a interação entre as pessoas. Com atritos, com problemas de comunicação,
com ego, com problemas em ouvir opiniões diferentes e etc


* Ferramentas estáveis, que tiram do programador pesos desnecessários são bem vindas  <!-- .element: class="fragment" data-fragment-index="2" -->

* Cada minuto economizado deixando de caçar por erros "bobos" pode ser usado para
fazer outra coisa, trabalhar em outra tarefa, descansar, etc <!-- .element: class="fragment" data-fragment-index="3" -->


* Nenhuma ferramenta é perfeita
* Mas quando adotamos práticas e técnicas que nos ajudam a lidar melhor com o
próprio trabalho, todo mundo ganha


* Existe uma série de problemas de segurança que foram causados por erros tecnicamente
pequenos

* Mas que vieram a existir por conta de programadores cansados, sobrecarregados,
etc

* [Heartbleed](http://www.pl-enthusiast.net/2014/07/01/how-did-heartbleed-remain-undiscovered-and-what-should-we-do-about-it/) [foi um ótimo](https://www.schneier.com/blog/archives/2014/04/heartbleed.html) [exemplo](https://www.zdnet.com/article/heartbleed-open-sources-worst-hour/)


* Type Hinting pode nos ajudar com isso <!-- .element: class="fragment" data-fragment-index="2" -->
* Quanto maior a base de código, mais essa técnica pode se tornar útil <!-- .element: class="fragment" data-fragment-index="3" -->
* Nem ela – e nem nada – vai capturar e evitar todos os bugs <!-- .element: class="fragment" data-fragment-index="4" -->
* Mas dando mais informações de uma forma elegante e organizada, podemos capturar
mais bugs e nos ajudar a cometer menos erros <!-- .element: class="fragment" data-fragment-index="5" -->



# Lembre-se dos humanos
"Mind the human" <!-- .element: class="small -->


* Programar em Python é divertido
* O que fez Python ser o que é somos nós, as pessoas


![programming-is-fun-again](xkcd353.png)


> Programming is fun again!

― [xkcd 353](https://xkcd.com/353/)


* Na hora de escolher entre técnicas e ferramentas <!-- .element: class="fragment" data-fragment-index="2" -->
* Na hora de revisar o código de um colega <!-- .element: class="fragment" data-fragment-index="3" -->
* Na hora de contratar alguém novo <!-- .element: class="fragment" data-fragment-index="4" -->


# Lembre-se dos humanos!


* Type Hinting ― ou qualquer outra técnica ― ajudam quando elas ajudam os seres humanos por trás do código


![us](us.jpeg)

Note:
* O legal de uma python brasil é isso - a união da comunidade
* Ontem, por exemplo, eu tive o prazer de me juntar a essas pessoas
fantásticas para jantar e conversar
* E entre tudo o que a gente falou, uma coisa todos nós concordamos que Python é o que é e chegou onde chegou por conta da preocupação com as pessoas
* Isso é uma coisa que todos nós devemos nos lembrar e praticar no
nosso dia-a-dia, na nossa comunidade local, nas nossas empresas, etc
* E eu quero agradecer muito a Carol Willing, Melissa Weber, João
Bueno, Lorena Mesa e Luciano Ramalho por terem também me lembrado
disso
* E eu quero agradecer a todos vocês por estarem aqui e me ouvido nesse tempo. Somos nós quem formamos essa comunidade incrível e somos nós que tornamos tudo isso possível


