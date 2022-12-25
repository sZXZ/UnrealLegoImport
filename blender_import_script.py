import bpy 
import argparse
from pathlib import Path
import sys
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

print(argv)  # --> ['example', 'args', '123']


bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

part = argv[0]
path = argv[1]
if Path(f"{path}\\parts\\{part}.dat").exists():
    bpy.ops.ldraw_exporter.import_operator(
        filepath=f"C:\\Program Files\\Studio 2.0\\ldraw\\parts\\{part}.dat", 
        ldraw_path="C:\\Program Files\\Studio 2.0\\ldraw",
        import_scale=0.01
    )
    bpy.ops.export_scene.fbx(filepath=f'models\\{part}.fbx')
    bpy.ops.wm.quit_blender()
if Path(f"{path}\\UnOfficial\\parts\\{part}.dat").exists():
    bpy.ops.ldraw_exporter.import_operator(
        filepath=f"C:\\Program Files\\Studio 2.0\\ldraw\\UnOfficial\\parts\\{part}.dat", 
        ldraw_path="C:\\Program Files\\Studio 2.0\\ldraw",
        import_scale=0.01
    )
    bpy.ops.export_scene.fbx(filepath=f'models\\{part}.fbx')
    bpy.ops.wm.quit_blender()
bpy.ops.wm.quit_blender()