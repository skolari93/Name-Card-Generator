import pandas as pd
import os
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.platypus import Image

def parse_excel(file_path):
    df = pd.read_excel(file_path)
    return list(zip(df['Name'], df['Class']))

def generate_name_cards(student_data, file_path, logo_path="logo.png"):
    output_file = os.path.splitext(file_path)[0] + ".pdf"  # Generate output filename from input file
    width, height = landscape(A4)
    c = canvas.Canvas(output_file, pagesize=landscape(A4))
    
    for name, class_name in student_data:
        
        # Draw dashed separator line in the middle
        c.setDash(5, 5)  # Dashed line pattern
        c.line(1*cm, height/2, width - 1*cm, height/2)
        c.setDash()  # Reset to solid line
        
        # Draw name in the lower part, aligned left
        c.setFont("Helvetica-Bold", 48)
        name_y_position = height / 3
        c.drawString(3*cm, name_y_position, name)
        
        # Draw class name below the student's name, in a smaller font
        c.setFont("Helvetica", 18)
        class_y_position = name_y_position - 1.5*cm
        c.drawString(3*cm, class_y_position, class_name)
        
        # Draw logo aligned with the name on the right side of the A4 page
        try:
            logo_width = 5*cm
            logo_height = 5*cm
            c.drawImage(logo_path, width - logo_width - 3*cm, name_y_position - logo_height / 3, width=logo_width, height=logo_height, preserveAspectRatio=True, mask='auto')
        except Exception as e:
            print(f"Error loading logo: {e}")
        c.showPage()  # Start a new page for each name
    
    c.save()
    print(f"PDF saved as {output_file}")

# Example usage
#file_path = "FP_Physik_PHBern.xlsx"  # Replace with your actual file path
#students = parse_excel(file_path)
#generate_name_cards(students, file_path, logo_path="neufeld.png")

file_path = "Test.xlsx"  # Replace with your actual file path
students = parse_excel(file_path)
generate_name_cards(students, file_path, logo_path="logo.png")