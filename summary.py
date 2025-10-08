import os
from google import genai
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


# this is the script to generate the summaries for the text files
# the text files are in the text folder
# the summaries are generated using the gemini api
# the summaries are saved to the summary folder
# the summaries are saved in the same format as the text files with the same name but with a _summary.txt extension

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
TEXT_DIR = Path("text")
SUMMARY_DIR = Path("summary")

def generate_summaries_for_all_texts():
    if not GEMINI_API_KEY:
        print("GEMINI_API_KEY not found in environment variables")
        return

    if not TEXT_DIR.exists():
        print("text directory not found")
        return

    client = genai.Client(api_key=GEMINI_API_KEY)

    text_files = list(TEXT_DIR.glob("*.txt"))

    for text_file in text_files:
        print(f"Processing: {text_file.name}")

        try:
            with open(text_file, 'r', encoding='utf-8') as f:
                text_content = f.read()
        except Exception as e:
            print(f"✗ Failed to read: {text_file.name}")
            continue

        try:
            prompt = f"""
            You are a helpful teacher explaining a research paper to undergraduate students who are not ML/AI experts.

            IMPORTANT: Students will use this paper as a BASE for their own research work. They need to understand it thoroughly so they can build upon it, extend it, and conduct further research in this area.

            Please create a comprehensive, easy-to-understand summary of this research paper that students can actually comprehend and use as a learning resource and BASE for their own research:

            Source: {text_file.name}

            Content:
            {text_content}

            Write a detailed summary that includes:

            **What did they try to achieve?**
            (Explain the main goal in simple terms - what problem were they trying to solve?)

            **How did they do it?**
            (List the main methods/approaches/techniques they used - explain them like you're teaching a beginner)

            **What did they discover/find?**
            (What were their main results? What worked better than before?)

            **What new things did they contribute?**
            (What novel ideas or improvements did they add to the field?)

            **Background Knowledge Needed**
            (What concepts should students understand before diving into this paper? What prerequisite knowledge is required?)

            **Key Technical Terms Explained Simply**
            (Define important technical terms in simple language that students can understand)

            **Glossary of Important Terms**
            (List key terms students should look up and understand, with brief simple explanations)

            **Dataset and Evaluation Details**
            (What dataset was used? How did they measure success? What metrics were important? Include specific details and links if mentioned)

            **Code and Data Availability**
            (Is the code publicly available? Where can students find it? Is the dataset accessible? Include any GitHub links, project pages, or data sources mentioned)

            **Time Investment and Difficulty Level**
            (How much time should students invest to understand this? Beginner/Intermediate/Advanced level? Learning curve assessment)

            **Why does this matter for students/researchers?**
            (How could this help in real-world applications or future research?)

            **What could students like you contribute or improve?**
            (What aspects could be extended, what limitations could be addressed, or what follow-up work could be done? How can students use this as a base for their own research? What specific research directions could they pursue?)

            **How to Use This as Your Research Base**
            (Specific ways students can build upon this work. What components can they modify, extend, or combine with other methods? What would be good starting points for their own research projects?)

            **Recommended Learning Path**
            (What should students study next? What related papers should they read? What skills should they develop in this field to conduct meaningful research based on this work?)

            Use simple language, avoid technical jargon, and make it conversational like a teacher explaining to students. Keep it comprehensive but understandable!
            """

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            summary = response.text
        except Exception as e:
            print(f"✗ Failed to generate summary: {text_file.name}")
            continue

        try:
            SUMMARY_DIR.mkdir(exist_ok=True)

            text_name_without_ext = text_file.stem
            summary_filename = f"{text_name_without_ext}_summary.md"
            summary_filepath = SUMMARY_DIR / summary_filename

            with open(summary_filepath, 'w', encoding='utf-8') as f:
                f.write(f"Summary for: {text_file.name}\n")
                f.write("=" * 50 + "\n\n")
                f.write(summary)

            print(f"✓ Summarized: {text_file.name}")
        except Exception as e:
            print(f"✗ Failed to save summary: {text_file.name}")

    print("Summary generation completed!")

def main():
    generate_summaries_for_all_texts()

if __name__ == "__main__":
    main()
