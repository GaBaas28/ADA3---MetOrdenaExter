import tkinter as tk
from tkinter import messagebox

def extraer_tramos(arr):
    # Identifica "Runs" (tramos naturales ya ordenados)
    tramos = []
    if not arr: return tramos
    tramo_actual = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            tramo_actual.append(arr[i])
        else:
            tramos.append(tramo_actual)
            tramo_actual = [arr[i]]
    tramos.append(tramo_actual)
    return tramos

def mezcla_equilibrada(arr):
    tramos = extraer_tramos(arr)
    log_visual = []
    
    while len(tramos) > 1:
        # Distribución equilibrada en 2 cintas
        cinta1 = tramos[0::2]
        cinta2 = tramos[1::2]
        log_visual.append(f"Distribución -> C1: {cinta1} | C2: {cinta2}")
        
        nuevos_tramos = []
        # Fusión equilibrada
        for i in range(min(len(cinta1), len(cinta2))):
            fusionado = []
            r1, r2 = cinta1[i], cinta2[i]
            p1, p2 = 0, 0
            while p1 < len(r1) and p2 < len(r2):
                if r1[p1] <= r2[p2]:
                    fusionado.append(r1[p1]); p1 += 1
                else:
                    fusionado.append(r2[p2]); p2 += 1
            fusionado.extend(r1[p1:])
            fusionado.extend(r2[p2:])
            nuevos_tramos.append(fusionado)
            
        if len(cinta1) > len(cinta2):
            nuevos_tramos.append(cinta1[-1])
            
        tramos = nuevos_tramos
        
    return tramos[0] if tramos else [], log_visual

def ejecutar_equilibrada():
    try:
        datos = [int(x.strip()) for x in entry_sensores.get().split(",")]
        resultado, logs = mezcla_equilibrada(datos)
        
        txt_log.delete(1.0, tk.END)
        for log in logs:
            txt_log.insert(tk.END, log + "\n")
        txt_log.insert(tk.END, f"\nDATOS FINALES:\n{resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa datos numéricos válidos.")

# --- Configuración de la GUI (Tkinter) ---
root3 = tk.Tk()
root3.title("Sensores - Mezcla Equilibrada (Natural)")
root3.geometry("500x350")

tk.Label(root3, text="Logs de sensores (parcialmente ordenados):").pack(pady=5)
entry_sensores = tk.Entry(root3, width=60)
# Fíjate en los tramos naturales: [1, 5, 9], [2, 3], [8], [4, 7]
entry_sensores.insert(0, "1, 5, 9, 2, 3, 8, 4, 7") 
entry_sensores.pack(pady=5)

btn_equilibrada = tk.Button(root3, text="Aplicar Mezcla Equilibrada", command=ejecutar_equilibrada, bg="lightcoral", fg="white")
btn_equilibrada.pack(pady=10)

txt_log = tk.Text(root3, height=12, width=58)
txt_log.pack(pady=5)

root3.mainloop()