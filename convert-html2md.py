import os
import sys
import logging
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def convert_html_to_markdown(folder):
    # Set up logging
    logging.basicConfig(filename='conversion.log', level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Check if the folder exists
    if not os.path.isdir(folder):
        logging.error(f"Folder {folder} does not exist.")
        return
    
    # Loop through all files in the folder
    for filename in os.listdir(folder):
        if filename.endswith(".html"):
            try:
                # Read the HTML file
                filepath = os.path.join(folder, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    soup = BeautifulSoup(file, 'html.parser')
                
                # Find the div with class "container-wide"
                container = soup.find('div', class_='container-wide')
                if container:
                    # Convert the contents to markdown
                    markdown_content = md(str(container))
                    
                    # Save the markdown to a new file
                    new_filename = filename.replace('.html', '.md')
                    new_filepath = os.path.join(folder, new_filename)
                    with open(new_filepath, 'w', encoding='utf-8') as md_file:
                        md_file.write(markdown_content)
                    
                    # Log the successful conversion
                    logging.info(f"Converted {filename} to {new_filename}")
                else:
                    logging.warning(f"No 'container-wide' div found in {filename}")
            except Exception as e:
                # Log any errors encountered
                logging.error(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert.py <folder>")
    else:
        folder = sys.argv[1]
        convert_html_to_markdown(folder)