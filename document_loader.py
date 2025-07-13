import PyPDF2
from pathlib import Path 

class DocumentLoader: 
    """" Una clase para cargar texto desde archivos PDF. """

    @staticmethod
    def load_single_pdf(file_path: str) -> str:    
        """ Extrae texto de un archivo pdf"""
        print(f"Cargando documento desde: {file_path}")
        reader = PyPDF2.PdfReader(file_path)
        text = ""
        try: 
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text() or ""
        except FileNotFoundError:
            print(f"Error! : The file {file_path} was not found")
        return text

    @staticmethod
    def load_pdfs_from_directory(directory_path: str) -> str:
        print("Loading all the PDFs from the directory: {directory_path}")
        # Path() converts the string of the route in a more powerful object
        path = Path(directory_path)
        # .glob finds all the files that end up with .pdf in that route. 
        pdf_files = list(path.glob('*.pdf'))

        all_texts = []
        for pdf_file in pdf_files:
            text = DocumentLoader.load_single_pdf(str(pdf_file))
            all_texts.append(text)
        
        print(f" {len(pdf_files)} PDF documents were loaded.  ")
        return "\n\n--- END OF THE DOCUMENT ---\n\n".join(all_texts)


if __name__ == "__main__": 
    file_path = "data"  
    texto = DocumentLoader.load_pdf(file_path)
    print("Texto extraído:")
    print(texto)