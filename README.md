# UnrealLegoImport
Imports Lego parts in the scene by reading ldr file

Automatically creates fbx files via Blender and imports them into unreal

Requires Blender and Ldraw library and https://github.com/cuddlyogre/ExportLDraw plugin installed in Blender


# Instal Process

Git clone inside Unreal Projects "Plugins" folder `<ProjectPath>/Plugins/UnrealLegoImport`

by default `git clone` will create folder named UnrealLegoImport

run **get_dependencies.bat** to remote execution from https://github.com/EpicGames/BlenderTools 

run **set_local_paths.bat** to add paths to dependencies

Install https://github.com/TobyLobster/ImportLDraw plugin into blender

Copy Content Folder into target Unreal project

import_lego_in_scene.ipynb have code that reads ldraw files 

currently there shouldn't be any submodels in the file
