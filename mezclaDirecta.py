import tkinter as tk
from tkinter import messagebox

def mezcla_directa(arr):
    block_size = 1
    n = len(arr)
    pasos = [] # Para visualizar en la GUI
    
    while block_size < n:
        # Fase de Partición a dos "cintas" simuladas
        f1, f2 = [], []
        for i in range(0, n, 2 * block_size):
            f1.extend(arr[i : i + block_size])
            f2.extend(arr[i + block_size : i + 2 * block_size])
            
        pasos.append(f"Bloque {block_size} -> Cinta 1: {f1} | Cinta 2: {f2}")
        
        # Fase de Fusión (Merge)
        arr = []
        i, j = 0, 0
        while i < len(f1) and j < len(f2):
            c1, c2 = 0, 0
            # Fusionar bloques de tamaño block_size
            while c1 < block_size and c2 < block_size and i < len(f1) and j < len(f2):
                if f1[i] < f2[j]:
                    arr.append(f1[i]); i += 1; c1 += 1
                else:
                    arr.append(f2[j]); j += 1; c2 += 1
            # Vaciar restos del bloque
            while c1 < block_size and i < len(f1):
                arr.append(f1[i]); i += 1; c1 += 1
            while c2 < block_size and j < len(f2):
                arr.append(f2[j]); j += 1; c2 += 1
                
        # Vaciar restos de las cintas
        arr.extend(f1[i:])
        arr.extend(f2[j:])
        block_size *= 2
        
    return arr, pasos

def ejecutar_mezcla_directa():
    try:
        datos = [int(x.strip()) for x in entry_libros.get().split(",")]
        resultado, pasos = mezcla_directa(datos)
        
        txt_output.delete(1.0, tk.END)
        txt_output.insert(tk.END, "PROCESO DE CINTAS:\n")
        for p in pasos:
            txt_output.insert(tk.END, p + "\n")
        txt_output.insert(tk.END, f"\nLIBROS ORDENADOS:\n{resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa IDs válidos (números separados por coma).")

# --- Configuración de la GUI (Tkinter) ---
root2 = tk.Tk()
root2.title("Biblioteca - Ordenamiento por Mezcla Directa")
root2.geometry("450x350")

tk.Label(root2, text="IDs de libros (desordenados):").pack(pady=5)
entry_libros = tk.Entry(root2, width=50)
entry_libros.insert(0, "45, 12, 89, 33, 1, 9, 77, 22")
entry_libros.pack(pady=5)

btn_directa = tk.Button(root2, text="Aplicar Mezcla Directa", command=ejecutar_mezcla_directa, bg="lightgreen")
btn_directa.pack(pady=10)

txt_output = tk.Text(root2, height=12, width=52)
txt_output.pack(pady=5)

root2.mainloop()