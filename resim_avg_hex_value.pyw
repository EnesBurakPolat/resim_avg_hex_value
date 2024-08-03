import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import numpy as np

#Gerekenler
#python -m pip install Pillow
#python -m pip install numpy

def calculate_average_color(image_path):
    with Image.open(image_path) as img:
        img = img.convert('RGB')  # Resmi RGB formatına çevir
        img_array = np.array(img)
        avg_color = img_array.mean(axis=(0, 1)).astype(int)
        return tuple(avg_color)

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def copy_to_clipboard(value):
    app.clipboard_clear()
    app.clipboard_append(value)
    app.update()

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        avg_color = calculate_average_color(file_path)
        hex_color = rgb_to_hex(avg_color)
        
        result_rgb_value.set(f"RGB: {avg_color}")
        result_hex_value.delete(1.0, tk.END)  # Önceki içeriği temizle
        result_hex_value.insert(tk.END, hex_color)  # Yeni HEX değerini ekle
        result_hex_value.config(bg=hex_color)

app = tk.Tk()
app.title("Average Color Calculator")
app.geometry("500x300")  # Pencere boyutunu 500x300 piksel olarak ayarla
app.configure(bg='#282828')

select_button = tk.Button(app, text="Select Image", command=select_image)
select_button.pack(pady=20)

result_rgb_value = tk.StringVar()
result_rgb = tk.Label(app, text="RGB: ", font=("Helvetica", 16))
result_rgb.pack(pady=10)
result_rgb_display = tk.Label(app, textvariable=result_rgb_value, font=("Helvetica", 12))
result_rgb_display.pack()

result_hex_value = tk.Text(app, height=1, width=20, font=("Helvetica", 12))
result_hex = tk.Label(app, text="HEX: ", font=("Helvetica", 16))
result_hex.pack(pady=10)
result_hex_value.pack()

copy_rgb_button = tk.Button(app, text="Copy RGB", command=lambda: copy_to_clipboard(result_rgb_value.get().split(': ')[1]))
copy_rgb_button.pack(pady=5)

copy_hex_button = tk.Button(app, text="Copy HEX", command=lambda: copy_to_clipboard(result_hex_value.get(1.0, tk.END).strip()))
copy_hex_button.pack(pady=5)

app.mainloop()
