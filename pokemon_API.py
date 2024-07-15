import requests
import json
  

# O endereço da API, foi atribuito em uma variável para facilitar a manuntenção :
url = "https://pokeapi.co/api/v2/pokemon/"
# lista para armazenar as informações dos pokemons: 
pokemon_list = list()
# O enquanto é utilizado para que o programa mude as para proxima pagina enquanto ouver valores a serem exibidos :
while url != None:
    response = json.loads(requests.request("GET", url).text) 
    url = response["next"]

    # O for é utilizado para que todas os pokémos tenham seus nomes exibidos:
    for it in response['results']:
        pokemon_name = (it["name"])

        # url para buscar informações por nome :
        url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response_pokemon = json.loads(requests.request("GET", url_pokemon).text) 

        # filtro de dados :
        infos = {
            "name" : pokemon_name,
            "id" : response_pokemon["id"],
            "height" : response_pokemon["height"],
            "weight" : response_pokemon["weight"],
            "is_default" : response_pokemon["is_default"]
        }

        # adiciona as informações a variavel pokemon_list :
        pokemon_list.append(infos)
        # retorna o id ( apenas para testar se o programa está funcionando):
        print(response_pokemon["id"])

# listar todas as informações (final do nosso programa) :
print(pokemon_list)

# salvar ou exportar as informações em um arquivo com formato da sua preferencia para todo grupo de objetos:
file_path = r"C:\Users\irans\arquivo\arUni\pkmInfos.json"
with open(file_path,  'w') as outfile : 
    print(f'salvando o arquivo  em {file_path}')
    json.dump(pokemon_list, outfile)

outfile.close()