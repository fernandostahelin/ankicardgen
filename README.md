
# Anki Code Generator

Esse projeto surgiu como uma forma de resolver uma dor que encontrei enquanto estudava inglês: gerar cards para Anki de uma forma automatizada, sem ter que inserir manualmente.


## Extrair sentenças de um arquivo
A aplicação deve reber qualquer arquivo de texto, seja um txt, docx, pdf, etc.
Utilizando a integração com o GPT-4 (avaliar outra lib de reconhecimento de lingua), a aplicação reconhecerá em que língua estão as frases no arquivo fornecido pelo usuário, com base em um input fornecido pelo usuário.

### Exemplo
Quero aprender: inglês.  
Minha língua nativa é: Português

#### Conteúdo do arquivo
Hello, I'm the Anki Card Generator.  
Olá, eu sou o Gerador de Cards do Anki.

### Resultado
Com base nos dados fornecidos, a aplição deve extrair as sentenças, identificando em qual língua está a frase, e criar frente e verso das frases, sendo frente na língua que o usuário deseja aprender, e verso na língua que ele domina.

## Gerador de cards Anki
Com base nas sentenças geradas acima, criar um arquivo .txt, utilizando um separador entre as frases de diferentes línguas, que possa ser importado no Anki.
