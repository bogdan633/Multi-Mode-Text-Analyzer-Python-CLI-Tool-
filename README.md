# 📝 Multi-Mode Text Analyzer (Python CLI Tool)

This is a beginner-friendly command-line Python tool that allows you to analyze a `.txt` file in multiple ways using different modes:

- 🔢 Count total words
- 📄 Count total lines
- 🔠 Count total characters
- 🔍 Search for a word and count how many times it appears

---

## 🚀 Features

- Simple and lightweight
- Accepts command-line arguments via `argparse`
- Handles empty or missing files safely
- Supports case-insensitive word search
- Works on Windows, macOS, and Linux

---

## 📦 Requirements

- Python 3.x (no external libraries needed — uses only the standard library)

---

## ⚙️ How to Use

### 🔹 Syntax

```bash
python text_analyzer.py <path_to_file> --mode <mode> [--query <word>] [--verbosity <level>]
