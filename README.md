# C++ Test Generator

Automatically generates unit tests for C++ projects using LLM.

## Features

- Recursively processes C++ files in nested directories
- Preserves original folder structure in test directory
- Integrates with Google Test framework
- Handles inter-file dependencies

## Requirements

- Python 3.8+
- CMake 3.10+
- Google Test
- LLM access (OpenAI API or local model)

## Installation

```bash
git clone https://github.com/yourusername/cpp-test-generator.git
cd cpp-test-generator
pip install -r requirements.txt  # If you have Python dependencies
```

## Usage

1. Place your C++ source files in `src/` (keep original folder structure)
2. Run the test generator:
   ```bash
   python main.py
   ```
3. Build and run tests:
   ```bash
   mkdir build && cd build
   cmake .. && make
   ctest --output-on-failure
   ```

## Configuration

Edit YAML files in `instructions/` to customize test generation.
