
# OpenHands Testing Repository

This repository serves as a testing environment for the OpenHands AI assistant. It provides a space to experiment with different tasks and features while maintaining a clean and organized structure.

## Project Overview

- **Purpose**: Testing and experimentation with OpenHands capabilities
- **Language**: Python
- **License**: MIT License

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/test-openhands.git
   cd test-openhands
   ```

2. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Environment:
   ```bash
   cp config.example.json config.json
   ```

## Configuration

- **Settings**: Modify `config.json` to suit your needs
- **Environment Variables**: Set required variables in your shell:
  ```bash
  export OPENHANDS_API_KEY="your-key"
  ```

## Usage

### Basic Operations

1. Run a simple test:
   ```bash
   python3 tests/basic_test.py
   ```

2. Execute a command through OpenHands:
   ```bash
   echo "your-command" | openhands-cli
   ```

### Examples

#### Example 1: Basic Interaction
```bash
openhands-cli --help
```

#### Example 2: Advanced Task
```bash
openhands-cli --task "fix-bug" --params "bug-id=123"
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License

Copyright (c) 2025 OpenHands

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
