# Research Paper Processing

## Setup
```bash
pip install -r requirements.txt
```

**With pip (Python>=3.11)**
```bash
pip install browser-use
playwright install chromium --with-deps --no-shell
```

Create `.env` file:
```
GEMINI_API_KEY=your-api-key-here
```

## Process

### 0. Generate CSV (Browser Automation)
```bash
python main.py
```
- Uses [browser-use](https://github.com/browser-use/browser-use) for browser automation
- Scrapes/generates CSV with PDF links
- Configure `prompt.md` before running
- **CSV is automatically saved to temp directory** in the filesystem

### 1. Download PDFs
```bash
python downloadpdfs.py
```

### 2. Extract Text
```bash
python extract_text.py
```

### 3. Generate AI Summaries
```bash
python summary.py
```

## CSV Format
```csv
Code,Title,Research Paper Link
R1-NLP,"Paper Title",https://example.com/paper.pdf
```

## Output
- `pdfs/` - Downloaded PDFs
- `text/` - Extracted text files
- `summary/` - AI-generated summaries (.md files)
