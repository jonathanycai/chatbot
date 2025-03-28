from bs4 import BeautifulSoup

def extract_text_from_html(file_path):
    """
    Extract text from an HTML file.
    
    Parameters:
    - file_path (str): Path to the HTML file.
    
    Returns:
    - Extracted text from the HTML.
    """
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    return soup.get_text()