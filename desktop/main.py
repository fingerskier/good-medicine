import eel
import os


# Initialize the Eel application
eel.init('web')  # 'web' folder will contain the frontend files (HTML, CSS, JS)


# Example Python function to perform bioinformatics calculations
def calculate_gc_content(sequence):
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    gc_content = (gc_count / len(sequence)) * 100 if sequence else 0
    return gc_content


# Expose the function to the Eel frontend
def get_gc_content(sequence):
    return calculate_gc_content(sequence)

eel.expose(get_gc_content)


# Start the Eel application
if __name__ == '__main__':
    if not os.path.exists('web/index.html'):
        print("Error: Frontend files not found. Please create an 'index.html' in the 'web' folder.")
    else:
        eel.start('index.html', size=(800, 600))