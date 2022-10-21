
import argparse
import unreal


def get_context():
    parser = argparse.ArgumentParser(description='Starting core')
    parser.add_argument('-r', type=float)
    parser.add_argument('-g', type=float)
    parser.add_argument('-b', type=float)
    parser.add_argument('-a', type=float)
    parser.add_argument('-n', '--name', type=str)
    return parser.parse_args()


def main(context):
    EditorAssetLibrary = unreal.EditorAssetLibrary
    AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
    MaterialEditingLibrary = unreal.MaterialEditingLibrary

    material = '/Game/LEGO/Parts/BaseLegoMaterial.BaseLegoMaterial'
    working_folder = '/Game/LEGO/Parts/'
    instance = f'/Game/LEGO/Parts/LegoMaterial_{context.name}_MI.LegoMaterial_{context.name}_MI'

    if EditorAssetLibrary.does_asset_exist(instance):
        material_instance = EditorAssetLibrary.find_asset_data(
            instance).get_asset()
    else:
        material_instance = AssetTools.create_asset(
            f'LegoMaterial_{context.name}_MI', working_folder, unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())

        MaterialEditingLibrary.set_material_instance_parent(
            material_instance,
            EditorAssetLibrary.find_asset_data(material).get_asset()
        )
        MaterialEditingLibrary.set_material_instance_vector_parameter_value(
            material_instance, "Color", unreal.LinearColor(
                context.r, context.g, context.b, context.a)
        )
        EditorAssetLibrary.save_asset(instance)


if __name__ == "__main__":
    main(get_context())
