import flet
from flet import Column, TextField, Page, ElevatedButton, Text, Image
import os
import pytesseract
from PIL import Image as PILImage
import re

# Configura la ruta al ejecutable de tesseract si es necesario
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\benna\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def main(page: Page):
    page.scroll = "auto"

    image_loc = TextField(label="Image Name", width=200)
    id_number = TextField(label="ID Number", width=200)
    surname_txt = TextField(label="Surname", width=200)
    name_txt = TextField(label="Name", width=200)
    birth_year = TextField(label="Birth Year", width=200)

    image_preview = Image(src="", width=250, height=250)

    def process_image(e):
        image_filename = image_loc.value
        image_path = os.path.join('data', image_filename)  # Ruta a la carpeta 'data'
        if not os.path.isfile(image_path):
            page.add(Text("Error: File not found.", color="red"))
            return

        try:
            
            img_pro = PILImage.open(image_path)
            # Procesa la imagen con pytesseract
            text = pytesseract.image_to_string(img_pro, lang="eng")
            print("Detected Text:")
            print(text)

            # Guarda el texto en un archivo
            with open("result.txt", "w", encoding="utf-8") as file:
                file.write(text)
            
            # Lee el texto del archivo
            with open("result.txt", mode="r", encoding="utf-8") as file:
                text = file.read()

            # Extrae secciones del texto
            sections = {}
            lines = text.split("\n")

            # Inicializa variables para almacenar los datos extraídos
            surname = ""
            name = ""
            birth_year_value = ""
            id_number_value = ""

            for line in lines:
                line = line.strip()
                if "Nom:" in line:
                    surname = line.split("Nom:")[-1].strip()
                    surname = re.sub(r'[^\w\s]', '', surname).strip()  # Elimina caracteres no alfanuméricos


                elif re.search(r'Pr(?:é|e)nom', line, re.IGNORECASE):
                    # Verifica que la línea contenga ":" o un espacio, y no contenga "usuel"
                    if (":" in line or " " in line) and "usuel" not in line.lower():
                        if ":" in line:
                            # Extrae el nombre después del primer ":"
                            name = line.split(":", 1)[1].strip()
                        else:
                            # Si no hay ":", extrae después del primer espacio
                            name = line.split(" ", 1)[1].strip()
                        
                        name = re.sub(r'\s+', ' ', name).replace(',', '').strip()  # Limpia espacios y comas
                        name = re.sub(r'[^\w\s]', '', name).strip()  # Elimina caracteres no alfanuméricos
                        # Guarda el nombre en una variable o en el resultado
                        name_txt.value = name

                                            



                elif  "Né(e} le:" in line:
                    # Extrae el año de nacimiento
                    match = re.search(r'\d{2}/\d{2}/(\d{4})', line)
                    birth_year_value = match.group(1) if match else "Not found"
                
                elif  "Né(e}le:" in line:
                    # Extrae el año de nacimiento
                    match = re.search(r'\d{2}/\d{2}/(\d{4})', line)
                    birth_year_value = match.group(1) if match else "Not found"
                elif re.search(r'\d{2}\.\d{2}\.\d{4}', line):
                    match = re.search(r'\d{2}\.\d{2}\.(\d{4})', line)
                    birth_year_value = match.group(1) if match else "Not found"
              

                elif "CARTE" in line.upper():
                    match = re.search(r'\d+[\w\d]*', line)
                    if match:
                        id_number_value = match.group(0)
                elif "RTE" in line:
                    match = re.search(r'RTE\s*(\d+)', line)
                    id_number_value = match.group(1) if match else "Not found"


                  
            # Actualiza las secciones
            sections["Surname"] = surname
            sections["Name"] = name
            sections["Birth Year"] = birth_year_value
            sections["ID Number"] = id_number_value

            print("Extracted Sections:")
            print(sections)

            # Actualiza los campos de texto en la interfaz de usuario
            id_number.value = sections.get("ID Number", "Not found")
            surname_txt.value = sections.get("Surname", "Not found")
            name_txt.value = sections.get("Name", "Not found")
            birth_year.value = sections.get("Birth Year", "Not found")

            # Actualiza la vista previa de la imagen
            image_preview.src = image_path
            page.update()

        except Exception as e:
            print(f"Error processing image: {e}")
            page.add(Text(f"Error processing image: {e}", color="red"))

    page.add(
        Column([
            image_loc,
            ElevatedButton("Process Image",
                           bgcolor="blue", color="white",
                           on_click=process_image),
            Text("Image Result", weight="bold"),
            image_preview,
            id_number,
            surname_txt,
            name_txt,
            birth_year
        ])
    )

flet.app(target=main)
