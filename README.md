# gjpd-python-ai
GAN JIANPING AI Demo using Python and OpenAI

## Overview

This project demonstrates how to use the OpenAI API with Python to create AI-powered applications.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (package installer for Python)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gjpd-python-ai.git
   cd gjpd-python-ai
   ```

2. Upgrade pip to the latest version:
   ```bash
   pip3 install --upgrade pip
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. Setup OPENAI_API_KEY in .zshrc file:
   ```bash
   echo 'export OPENAI_API_KEY=your_api_key_here' >> ~/.zshrc
   source ~/.zshrc
   ```

## Usage

Run the introduction example:
```bash
python3 openai/text-input.py
```

## Project Structure

- `requirements.txt`: Required Python packages
- `.env`: Environment variables (not tracked by git)

## Useful Commands

### Check installed OpenAI library info
```bash
pip show openai
```

## Useful Resources

- [AI Cookbook](https://github.com/daveebbelaar/ai-cookbook/tree/main) - This Cookbook contains examples and tutorials to help developers build AI systems, offering copy/paste code snippets that you can easily integrate into your own projects.

## License

This project is licensed under the MIT License - see the LICENSE file for details.