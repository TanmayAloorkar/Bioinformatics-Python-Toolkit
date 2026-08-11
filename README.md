# Bioinformatics Python Toolkit

A collection of small Python modules for common bioinformatics tasks, including
sequence analysis, FASTA/FASTQ processing, motif searches, variant handling,
population genetics, protein analysis, and alignment utilities.

## Setup

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
```

Activate the environment and install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Helpdesk

The helpdesk discovers the public functions in `modules` without importing the
individual analysis modules.

```bash
python -m modules.helpdesk list
python -m modules.helpdesk search fasta
python -m modules.helpdesk show reverse_complement
```

Functions can be imported through their category and module:

```python
from modules.seq_tools.reverse_complement import reverse_complement

print(reverse_complement("ACGT"))
```

## Project structure

- `modules/` — bioinformatics functions grouped by category
- `modules/helpdesk.py` — searchable command-line function reference
- `build_windows.ps1` — builds a standalone Windows executable
- `build_linux.sh` — builds a standalone Linux executable

Generated executables are placed under `releases/` and are intentionally not
tracked by Git. They are better distributed through GitHub Releases.

## Building standalone executables

PyInstaller creates native binaries for the operating system on which it runs.
The `modules` source directory is bundled because the helpdesk reads function
signatures and documentation from those files. Each build script automatically
installs PyInstaller and the dependencies listed in `requirements.txt` before
creating the executable.

### Windows

Run the following command from PowerShell in the toolkit directory:

```powershell
.\build_windows.ps1
```

The executable is created at `releases/windows/helpdesk.exe`.
When opened by double-clicking, the Windows executable waits for Enter before
closing. Commands run with arguments still exit normally.

### Linux

Run the following commands from a terminal in the toolkit directory:

```bash
chmod +x build_linux.sh
./build_linux.sh
```

The executable is created at `releases/linux/helpdesk`.

The Linux executable must be built on Linux or in a Linux container or virtual
machine. The Windows executable must be built on Windows.

## License

This project is available under the [MIT License](LICENSE).
