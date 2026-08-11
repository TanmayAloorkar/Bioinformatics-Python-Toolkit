#!/usr/bin/env bash
set -euo pipefail
module_source="$(pwd)/modules"

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pyinstaller -r requirements.txt
python3 -m PyInstaller \
    --noconfirm \
    --clean \
    --onefile \
    --name helpdesk \
    --distpath releases/linux \
    --workpath build/linux \
    --specpath build \
    --add-data "$module_source:modules" \
    modules/helpdesk.py

chmod +x releases/linux/helpdesk
echo "Created releases/linux/helpdesk"
