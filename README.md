# HARP Firmware Updater GUI

A modern graphical user interface for the HarpRegulator CLI application, enabling users to browse and update firmware for connected Harp devices. Built with Python and NiceGUI, providing a web-based interface with a clean, intuitive design.

## Features

- **Device Management**: Automatically discover and list connected Harp devices
  - Real-time device status monitoring
  - Support for both Pico (RP2040/RP2350) and ATxmega-based devices
  - Device health indicators and filtering
  
- **Firmware Browsing**: Browse and select firmware versions
  - Inspect firmware files (.uf2 and .hex formats)
  - View firmware metadata and compatibility information
  - Browse local firmware files or select from repository
  
- **Update Workflow**: Streamlined firmware deployment process
  - Step-by-step progress tracking (Validation → Flashing → Verification)
  - Real-time log output
  - Error handling with retry and rollback options
  - Progress visualization

## Prerequisites

- Python 3.9 or higher (3.12 recommended)
- HarpRegulator CLI tool installed and accessible in PATH
- Harp devices connected to your computer

## Installation

This project uses [uv](https://docs.astral.sh/uv/) for fast, reliable Python project management.

### 1. Install uv

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd harp-updater-gui

# Install dependencies and create virtual environment
uv sync

# Activate the virtual environment (optional, uv run does this automatically)
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

## Usage

### Running the Application

Using uv (recommended):
```bash
uv run harp-updater-gui
```

Or with activated virtual environment:
```bash
python -m harp_updater_gui.main
```

### Development Mode

Run with auto-reload for development:
```bash
uv run python -m harp_updater_gui.main
```

The application will open in your default web browser at `http://localhost:8080`.

## Project Structure

```
harp-updater-gui/
├── src/
│   └── harp_updater_gui/
│       ├── __init__.py
│       ├── main.py                    # Application entry point
│       ├── components/                # UI components
│       │   ├── header.py              # Application header
│       │   ├── device_list.py         # Device discovery sidebar
│       │   ├── firmware_browser.py    # Firmware selection panel
│       │   └── update_workflow.py     # Update progress panel
│       ├── services/                  # Business logic
│       │   ├── cli_wrapper.py         # HarpRegulator CLI interface
│       │   ├── device_manager.py      # Device management
│       │   └── firmware_service.py    # Firmware operations
│       ├── models/                    # Data models
│       │   ├── device.py              # Device model
│       │   └── firmware.py            # Firmware model
│       └── utils/                     # Utilities
│           └── constants.py           # Application constants
├── tests/                             # Unit tests
│   ├── test_device_manager.py
│   └── test_firmware_service.py
├── pyproject.toml                     # Project configuration
├── .python-version                    # Python version (3.12)
└── README.md
```

## Development

### Adding Dependencies

```bash
# Add a runtime dependency
uv add <package-name>

# Add a development dependency
uv add --dev <package-name>
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=harp_updater_gui

# Run specific test file
uv run pytest tests/test_device_manager.py
```

### Code Quality

```bash
# Format code (if you add ruff or black)
uv run ruff format .

# Lint code
uv run ruff check .
```

## HarpRegulator CLI Integration

This GUI integrates with the HarpRegulator CLI tool. Ensure HarpRegulator is installed and available in your system PATH.

### Example HarpRegulator Commands

```bash
# List all devices
HarpRegulator list --json --all --allow-connect

# Inspect firmware
HarpRegulator inspect firmware.uf2 --json
HarpRegulator inspect firmware.hex --json

# Upload firmware
HarpRegulator upload firmware.uf2 --target COM3
HarpRegulator upload firmware.hex --target /dev/ttyUSB0 --force
```

## Configuration

The application can be configured by modifying `src/harp_updater_gui/utils/constants.py` or by setting environment variables (if implemented).

## Troubleshooting

### HarpRegulator not found
Ensure the HarpRegulator CLI is installed and in your PATH. You can specify a custom path in `services/cli_wrapper.py` or `device_manager.py`.

### No devices detected
- Check that Harp devices are properly connected
- On Windows, you may need to install drivers using `HarpRegulator install-drivers`
- Try running with `--allow-connect` flag enabled

### Port access issues
- On Linux, you may need to add your user to the `dialout` group:
  ```bash
  sudo usermod -a -G dialout $USER
  ```
- Log out and back in for changes to take effect

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`uv run pytest`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Related Projects

- [HarpRegulator](https://github.com/harp-tech/harp-regulator) - The CLI tool this GUI wraps
- [Harp Protocol](https://harp-tech.org/) - The Harp protocol specification
- [NiceGUI](https://nicegui.io/) - The web framework used for the UI

## Acknowledgments

- Built with [NiceGUI](https://nicegui.io/) by Zauberzeug
- Uses [uv](https://docs.astral.sh/uv/) by Astral for project management
- Integrates with HarpRegulator CLI by the Harp community