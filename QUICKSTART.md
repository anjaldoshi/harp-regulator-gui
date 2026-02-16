# Quick Start Guide

Get up and running with the HARP Firmware Updater GUI in minutes!

## Prerequisites

1. **Python 3.12** (or 3.9+)
2. **HarpRegulator CLI** installed and in PATH
3. **uv** package manager (will be installed in step 1)

## Installation Steps

### 1. Install uv

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Setup Project

```bash
# Navigate to project directory
cd harp-updater-gui

# Install dependencies and create virtual environment
uv sync
```

That's it! All dependencies will be installed automatically.

### 3. Run the Application

**Simple method:**
```bash
uv run harp-updater-gui
```

**Or using the run script:**
```bash
uv run python run.py
```

**With activated virtual environment:**
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Then run
python -m harp_updater_gui.main
```

## First Use

1. **Launch the application** - It will open in your default browser
2. **Connect devices** - Connect your Harp devices via USB
3. **Click "Check for updates"** - Discover connected devices
4. **Select a device** - Click on a device card to select it
5. **Browse firmware** - Choose a firmware file or version
6. **Deploy** - Click "Deploy firmware" to start the update

## Common Commands

```bash
# Install dependencies
uv sync

# Add a new dependency
uv add <package-name>

# Run the app
uv run harp-updater-gui

# Run tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test
uv run pytest tests/test_device_manager.py -v
```

## Troubleshooting

### "HarpRegulator not found"
Ensure HarpRegulator CLI is installed and in your PATH:
```bash
# Test if HarpRegulator is available
HarpRegulator --help
```

### "No devices detected"
1. Check USB connections
2. On Windows, install drivers: `HarpRegulator install-drivers`
3. Try clicking "Check for updates" again
4. Check if devices appear in HarpRegulator CLI: `HarpRegulator list --all`

### Port Permission Issues (Linux)
```bash
# Add user to dialout group
sudo usermod -a -G dialout $USER

# Log out and back in for changes to take effect
```

### uv not found after installation
Close and reopen your terminal to refresh the PATH.

## Development Tips

### Enable Auto-Reload
The application automatically reloads when you make changes to the code.

### View Logs
Check the terminal/console where you launched the app for detailed logs.

### Debugging
Set breakpoints in your IDE and run:
```bash
# VS Code with Python extension
# Or use Python debugger
python -m pdb -m harp_updater_gui.main
```

## Next Steps

- Read the full [README.md](README.md) for detailed information
- Check out [HarpRegulator documentation](https://github.com/harp-tech/harp-regulator)
- Explore the [Harp Protocol](https://harp-tech.org/)

## Getting Help

- Check the application logs in the terminal
- Review HarpRegulator CLI output: `HarpRegulator list --json`
- Open an issue on GitHub (if applicable)

## Project Structure Overview

```
src/harp_updater_gui/
├── main.py              # Application entry point
├── components/          # UI components (NiceGUI)
│   ├── header.py        # Top navigation bar
│   ├── device_list.py   # Left sidebar - device list
│   ├── firmware_browser.py  # Center - firmware browser
│   └── update_workflow.py   # Right sidebar - update progress
├── services/            # Business logic
│   ├── cli_wrapper.py   # HarpRegulator CLI interface
│   ├── device_manager.py    # Device operations
│   └── firmware_service.py  # Firmware operations
└── models/              # Data models (Pydantic)
    ├── device.py        # Device model
    └── firmware.py      # Firmware model
```

Happy firmware updating! 🚀
