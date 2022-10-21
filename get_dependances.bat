git clone https://github.com/EpicGames/BlenderTools --filter=blob:none --sparse
cd BlenderTools
git sparse-checkout set --no-cone send2ue/dependencies/
cd ..
python -m venv venv && venv\\Scripts\\activate && pip install -r requirements.txt
