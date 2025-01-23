import json
from pathlib import Path


# Função recursiva para criar estrutura de pastas e arquivos
def create_structure(base_path, structure):
    for key, value in structure.items():
        current_path = base_path / key
        current_path.mkdir(parents=True, exist_ok=True)

        if isinstance(value, dict):  # Se for um dicionário, criar subpastas
            create_structure(current_path, value)
        elif isinstance(value, list):  # Se for uma lista, criar arquivos
            for file_name in value:
                (current_path / file_name).touch()  # Criar arquivo vazio


# Carregar a estrutura do arquivo JSON
with open("./src/tree_project.json", "r") as file:
    file_structure = json.load(file)

new_key = "meu_projeto"
if len(file_structure) == 1:  # Certifica-se de que há apenas uma key no topo
    first_key = list(file_structure.keys())[0]  # Obter a primeira key
    file_structure[new_key] = file_structure.pop(first_key)  # Renomear a key

# Definir o caminho base
base_path = Path(input("Digite o caminho base: ").strip())

# Criar estrutura
create_structure(base_path, file_structure)

print(f"Estrutura criada em: {base_path}")
