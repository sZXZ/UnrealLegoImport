import argparse
import unreal

# thanks https://www.artstation.com/blogs/deonwilson/bl7N/using-python-in-unreal-to-import-static-meshes

def get_context():
    parser = argparse.ArgumentParser(description='Starting core')
    parser.add_argument('-f', '--file', type=str)
    return parser.parse_args()


def build_static_mesh_data():
    static_mesh_data = unreal.FbxStaticMeshImportData()
    static_mesh_data.set_editor_property("build_nanite", True)
    static_mesh_data.set_editor_property("auto_generate_collision", False)
    return static_mesh_data


def build_import_options(static_mesh_data):
    options = unreal.FbxImportUI()
    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', False)
    options.set_editor_property('import_materials', False)
    options.set_editor_property('import_as_skeletal', False)
    options.set_editor_property("static_mesh_import_data", static_mesh_data)
    return options


def build_import_tasks(filename: str, destination_name: str, destination_path: str, options):
    tasks = []
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)
    task.set_editor_property("destination_name", destination_name)
    task.set_editor_property("destination_path", destination_path)
    task.set_editor_property("filename", filename)
    task.set_editor_property('options', options)
    tasks.append(task)
    return tasks


def execute_import_static_mesh(file_path):
    mesh_data = build_static_mesh_data()
    mesh_options = build_import_options(mesh_data)
    name = file_path.split('\\')[-1][0:-4]
    import_tasks = build_import_tasks(file_path, f"Lego_{name}", "/Game/LEGO/Parts",
                                      mesh_options)
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    asset_tools.import_asset_tasks(import_tasks)


def main(context):
    execute_import_static_mesh(context.file)
    print('done')


if __name__ == "__main__":
    main(get_context())
