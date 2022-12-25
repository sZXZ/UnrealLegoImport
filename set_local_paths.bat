set cur_path=%cd%
@echo %cd% >"%cd%/venv/Lib/site-packages/root.pth"
@echo %cd%\BlenderTools\send2ue\dependencies\ >"%cd%/venv/Lib/site-packages/sendtoue.pth"
del %cd%\BlenderTools\send2ue\dependencies\unreal.py
cd ..
cd ..
@echo %cd%\Intermediate\PythonStub\ >"%cur_path%/venv/Lib/site-packages/unreal_stab.pth"