### Recuperação de Informações de Pokémon da PokéAPI

Este script em Python interage com a PokéAPI para obter informações detalhadas sobre Pokémon e as armazena em um arquivo JSON. Abaixo está uma documentação detalhada para entender e utilizar o script de forma eficaz.

#### Visão Geral

O script utiliza Python e faz uso da biblioteca `requests` para buscar dados da [PokéAPI ](https://pokeapi.co/). Ele itera por várias páginas de dados de Pokémon, recupera informações específicas para cada Pokémon e então armazena esses dados em um arquivo JSON para uso posterior.


#### Explicação do Script

- **Variáveis Utilizadas:**
  - `counter`: Mantém o controle da contagem de iterações.
  - `url`: URL base para a PokéAPI.
  - `pokemon_list`: Lista para armazenar as informações dos Pokémon.
  - `file_path`: Caminho para salvar o arquivo JSON com as informações dos Pokémon.

- **Funcionalidade Principal:**
  - Utiliza um loop `while` para iterar por páginas de dados de Pokémon até que não haja mais páginas disponíveis (`url` se torna `None`).
  - Faz uma requisição GET HTTP para a PokéAPI para buscar uma página de dados de Pokémon.
  - Para cada Pokémon na resposta:
    - Recupera detalhes adicionais (ID, altura, peso, status padrão) fazendo outra chamada de API usando o nome do Pokémon.
    - Armazena essas informações na `pokemon_list`.
    - Imprime o ID do Pokémon para verificação.
  - Uma vez que todos os dados dos Pokémon são coletados, imprime toda a `pokemon_list`.
  - Salva a `pokemon_list` como um arquivo JSON (`pkmInfos.json`) no `file_path` especificado.

#### Observações

- O script pressupõe uma conexão de internet estável para interagir com a PokéAPI.
- Certifique-se de lidar adequadamente com conjuntos de dados grandes ao lidar com um número substancial de Pokémon.
- Modifique `file_path` conforme a estrutura de diretórios do seu sistema.

Este script demonstra a interação básica com API e manipulação de JSON em Python, projetado especificamente para recuperar dados de Pokémon da PokéAPI. Ajustes podem ser feitos para atender requisitos específicos ou melhorias adicionais.
