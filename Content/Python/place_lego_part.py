import argparse
import unreal


def get_context():
    parser = argparse.ArgumentParser(description='Starting core')
    parser.add_argument('-b', '--brick', type=str)
    parser.add_argument('-v', '--vector', type=str)
    parser.add_argument('-r', '--rotation_matrix', type=str)
    parser.add_argument('-m', '--material', type=str)
    return parser.parse_args()


def main(context):
    EditorAssetLibrary = unreal.EditorAssetLibrary
    AssetRegistry = unreal.AssetRegistryHelpers.get_asset_registry() # type: unreal.AssetRegistry
    asset = AssetRegistry.get_asset_by_object_path(f"/UnrealLegoImport/Parts/Lego_{context.brick}.Lego_{context.brick}")
    if asset.is_valid():
        part = unreal.load_asset(asset.package_name)
    else:
        reg = AssetRegistry.get_assets_by_path('/UnrealLegoImport/Parts/')
        asset = None # type: unreal.AssetData
        for asset in reg:
            try:
                asset_name = asset.get_full_name().split('.')[-1].split('_')[1]
            except:
                # skips non lego brick assets
                continue
            if context.brick == asset_name:
                part = unreal.load_asset(asset.package_name)
                break
    print(part)
    instance = f'/UnrealLegoImport/Parts/LegoMaterial_{context.material}_MI.LegoMaterial_{context.material}_MI'
    vector = context.vector.split(',')
    matrix = context.rotation_matrix.split(',')
    mv = []
    for v in matrix:
        mv.append(float(v))
    a = mv[0]
    b = mv[1]
    c = mv[2]
    d = mv[3]
    e = mv[4]
    f = mv[5]
    g = mv[6]
    h = mv[7]
    i = mv[8]
    x = float(vector[0])
    y = float(vector[1])
    z = float(vector[2])

    matrix = unreal.Matrix(
        (
            a,d,g,0
        ),
        (
            b,e,h,0
        ),
        (
            c,f,i,0
        ),
        (
            x,y,z,1
        ),
    )

    actor = unreal.EditorLevelLibrary.spawn_actor_from_object(
        part,
        unreal.Vector(),
        unreal.Rotator()
    )  # type: unreal.Actor
    #matrix = matrix.mirror(unreal.AxisType.X,unreal.AxisType.NONE)
    #matrix = matrix.mirror(unreal.AxisType.Z,unreal.AxisType.NONE)
    rot = unreal.MathLibrary.compose_rotators( unreal.Rotator(-90,0,0) ,matrix.rotator() )
    transform = matrix.transform()
    transform.rotation = rot.quaternion()
    transform.scale3d = unreal.Vector(1,-1,1)
    
    rotate_around = unreal.Transform(unreal.Vector(), unreal.Rotator(90,0,0), unreal.Vector(1,1,-1))
    transform = unreal.MathLibrary.compose_transforms(transform, rotate_around)
    actor.set_actor_transform(
        transform, False, False
    )
    actor.set_actor_scale3d(unreal.Vector(1,1,1))
    actor.add_actor_local_rotation(unreal.Rotator(180,0,0),False , False)
    sm = actor.static_mesh_component  # type: unreal.StaticMeshComponent
    material_instance = EditorAssetLibrary.find_asset_data(
        instance).get_asset()
    sm.set_material(0, material_instance)


if __name__ == "__main__":
    main(get_context())
