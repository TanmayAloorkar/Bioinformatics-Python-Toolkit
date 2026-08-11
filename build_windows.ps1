$ErrorActionPreference = "Stop"
$moduleSource = (Resolve-Path "modules").Path

python -m pip install --upgrade pip
python -m pip install --upgrade pyinstaller -r requirements.txt
python -m PyInstaller `
    --noconfirm `
    --clean `
    --onefile `
    --name helpdesk `
    --distpath releases/windows `
    --workpath build/windows `
    --specpath build `
    --add-data "$moduleSource;modules" `
    modules/helpdesk.py

Write-Host "Created releases/windows/helpdesk.exe"
