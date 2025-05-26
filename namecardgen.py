import pandas as pd
import os
import argparse
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.platypus import Image

def parse_excel(file_path):
    """Parse Excel file and return list of (name, class) tuples"""
    try:
        df = pd.read_excel(file_path)
        return list(zip(df['Name'], df['Class']))
    except FileNotFoundError:
        print(f"Error: Excel file '{file_path}' not found.")
        return None
    except KeyError as e:
        print(f"Error: Required column {e} not found in Excel file.")
        return None
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

def generate_name_cards(student_data, file_path, logo_path="logo.png"):
    """Generate PDF name cards from student data"""
    output_file = os.path.splitext(file_path)[0] + ".pdf"
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
        if logo_path and os.path.exists(logo_path):
            try:
                logo_width = 5*cm
                logo_height = 5*cm
                c.drawImage(logo_path, width - logo_width - 3*cm, name_y_position - logo_height / 3, 
                          width=logo_width, height=logo_height, preserveAspectRatio=True, mask='auto')
            except Exception as e:
                print(f"Error loading logo '{logo_path}': {e}")
        elif logo_path:
            print(f"Warning: Logo file '{logo_path}' not found. Continuing without logo.")
        
        c.showPage()  # Start a new page for each name
   
    c.save()
    print(f"PDF saved as {output_file}")

def main():
    """Main function to handle command line arguments"""
    parser = argparse.ArgumentParser(description='Generate name cards from Excel file')
    parser.add_argument('excel_file', nargs='?', default='Test.xlsx', 
                       help='Path to Excel file containing Name and Class columns (default: Test.xlsx)')
    parser.add_argument('-l', '--logo', help='Path to logo image file (optional)', default='logo.png')
    
    args = parser.parse_args()
    
    # Check if Excel file exists
    if not os.path.exists(args.excel_file):
        print(f"Error: Excel file '{args.excel_file}' not found.")
        return
    
    # Parse Excel file
    students = parse_excel(args.excel_file)
    if students is None:
        return
    
    if not students:
        print("No student data found in Excel file.")
        return
    
    print(f"Found {len(students)} students in the Excel file.")
    
    # Generate name cards
    generate_name_cards(students, args.excel_file, args.logo)

if __name__ == "__main__":
    main()