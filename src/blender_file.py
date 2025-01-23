import bpy

# Criar um cubo
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))

# Definir nome do arquivo
file_path = "/home/fetas/Downloads/meu_arquivo.blend"

# Salvar o arquivo .blend
bpy.ops.wm.save_as_mainfile(filepath=file_path)
