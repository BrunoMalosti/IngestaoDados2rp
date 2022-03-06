# Desafio Ingestão de Dados

- ## Decisões de Arquitetura
A arquitetura foi definida conforme o [Modelo Entidade-Relacionamento](https://github.com/BrunoMalosti/IngestaoDados2rp/blob/master/Modelagem.pdf)


- ## Implementação 

Para tentar organizar de forma acessível para se "debugar" e/ou exibir o código a terceiros, optou-se por escrever um script em python para cada tabela. Assim, para que se pudesesse facilitar o processo para a compilação e o uso do MySQL Workbench, basta que o usuário dê o comando via terminal ```./compilar.sh```.

Assim, para cada arquivo csv, o programa irá percorrer todo o seu conteúdo e convertendo os dados em um arquivo sql, permitindo a inserção destes no banco de dados da AWS. Dentro desses scripts, foi implementado todos os tratamentos necessários para corrigir qualquer erro ou warning que pudesse vir a ocorrer durante a inserção no BD.

Foi feita a criação de uma conta gratuita no sistema da AWS. Esta conta, possui algumas limitações porém não afetam a funcionabilidade do teste em si. O [print do site da aws](https://github.com/BrunoMalosti/IngestaoDados2rp/blob/master/banco%20de%20dados%20AWS.PNG) ilustra como foi instanciado o banco.


- ## Instrução de como executar o software

Basta executar no terminal o comando

```./compilar.sh#```

Neste arquivo .sh, será executado o script de cada tabela, bem como será feito ao final a concatenação de todos esses arquivos em um único arquivo, denominado como [SQL_DADOS.sql](https://github.com/BrunoMalosti/IngestaoDados2rp/blob/master/SQL_DADOS.sql).

As resoluções das querys de análise de dados, estão localizadas no arquivo denominado como [SQL_DADOS.sql](https://github.com/BrunoMalosti/IngestaoDados2rp/blob/master/SQL%20QUERYS.sql).

