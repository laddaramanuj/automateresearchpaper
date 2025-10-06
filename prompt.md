# ICLR Research Paper Scraper

## Task Overview
Go to the ICLR research conference website and extract the latest research papers from 2024 and 2025. Include the top 50 papers from each year and ensure PDF download links are included in the CSV output.

## CSV Format Specification

### Required Columns
- **Date**: Current date in DD/MM/YYYY format
- **Name**: Your first name (for identification)
- **Code**: R<Serial No.>-<DomainCode> (e.g., R1-NLP, R2-CV)
- **Title**: Full title of the research paper
- **Domain**: Research paper domain(s) - can include multiple
- **Conference / Journal Name**: Conference or journal name
- **Publication Year**: Year of publication (2024 or 2025 only)
- **Research Paper Link**: Direct PDF download link
- **Summary Doc Link**: Link to summary document (leave empty)
- **Remarks**: Any additional notes or remarks

## Specific Instructions
1. **Date**: Use today's date in DD/MM/YYYY format
2. **Name**: Use "Ramanuj"
3. **Conference**: Use "ICLR"
4. **Years**: Only include papers from 2024 and 2025
5. **PDF Links**: Ensure all PDF download links are working
6. **Summary Links**: Leave empty (not required)
7. **Remarks**: Add if any special notes needed

## Source URL
**ICLR Papers**: https://openreview.net/group?id=ICLR.cc

## Output
Generate a CSV file with 100 entries (50 from 2024 + 50 from 2025) following the exact format specified above.