import tkinter as tk
from tkinter import messagebox

def intercalar_transacciones(lista1, lista2):
    # Simula la lectura secuencial de dos archivos ya ordenados
    resultado = []
    i, j = 0, 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    # Añadimos los elementos restantes (si un archivo terminó antes que el otro)
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado

def ejecutar_intercalacion():
    try:
        # Extraer y limpiar datos de la GUI
        sucursal_norte = [int(x.strip()) for x in entry_norte.get().split(",")]
        sucursal_sur = [int(x.strip()) for x in entry_sur.get().split(",")]
        
        # Validar que vengan ordenados (requisito de la intercalación)
        if sucursal_norte != sorted(sucursal_norte) or sucursal_sur != sorted(sucursal_sur):
            messagebox.showwarning("Advertencia", "Los registros de cada sucursal deben venir ordenados.")
            return

        resultado = intercalar_transacciones(sucursal_norte, sucursal_sur)
        lbl_resultado.config(text=f"Registro Maestro: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa solo números enteros separados por comas.")

# --- Configuración de la GUI (Tkinter) ---
root1 = tk.Tk()
root1.title("Banco - Intercalación de Sucursales")
root1.geometry("400x250")

tk.Label(root1, text="Transacciones Sucursal Norte (ordenadas, separadas por coma):").pack(pady=5)
entry_norte = tk.Entry(root1, width=50)
entry_norte.insert(0, "101, 105, 110, 120")
entry_norte.pack(pady=5)

tk.Label(root1, text="Transacciones Sucursal Sur (ordenadas, separadas por coma):").pack(pady=5)
entry_sur = tk.Entry(root1, width=50)
entry_sur.insert(0, "102, 103, 115, 125")
entry_sur.pack(pady=5)

btn_fusionar = tk.Button(root1, text="Intercalar Registros", command=ejecutar_intercalacion, bg="lightblue")
btn_fusionar.pack(pady=15)

lbl_resultado = tk.Label(root1, text="Registro Maestro: ", font=("Arial", 10, "bold"))
lbl_resultado.pack(pady=5)

root1.mainloop()
