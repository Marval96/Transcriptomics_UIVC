import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

def calcular_hubs(input_file, percentil=0.80):
    # Crear directorio de salida
    output_dir = "results_hubs"
    os.makedirs(output_dir, exist_ok=True)

    # Obtener el prefijo del archivo de entrada
    file_prefix = os.path.basename(input_file).split(".")[0]
    
    # Archivo de salida
    output_csv = os.path.join(output_dir, f"hubs_{file_prefix}.csv")
    output_png = os.path.join(output_dir, f"hubs_{file_prefix}.png")
    output_log = os.path.join(output_dir, f"hubs_{file_prefix}.txt")

    # Redirigir salida de terminal a un archivo
    sys.stdout = open(output_log, "w")

    # Cargar archivo
    print(f"📂 Cargando archivo: {input_file}")
    df = pd.read_csv(input_file)

    # Verificar columnas necesarias
    if "Gene" not in df.columns or "Score" not in df.columns:
        print("❌ Error: El archivo debe contener las columnas 'Gene' y 'Score'.")
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        return

    # Ordenar y calcular percentil
    df_sorted = df.sort_values(by="Score", ascending=False)
    threshold = df_sorted["Score"].quantile(percentil)
    
    # Filtrar top percentil
    top_hubs = df_sorted[df_sorted["Score"] >= threshold]
    
    # Guardar resultados
    top_hubs.to_csv(output_csv, index=False)
    print(f"✅ Hubs guardados en: {output_csv}")

    # Graficar distribución
    plt.figure(figsize=(8, 5))
    sns.histplot(df_sorted["Score"], bins=30, kde=True, color="blue")
    plt.axvline(threshold, color="red", linestyle="dashed", label=f"Top {int((1-percentil)*100)}%")
    plt.xlabel("Score")
    plt.ylabel("Frecuencia")
    plt.title("Distribución de Scores")
    plt.legend()
    plt.savefig(output_png, dpi=300)
    plt.close()
    
    print(f"📊 Gráfico guardado en: {output_png}")

    # Cerrar el archivo de salida
    sys.stdout.close()
    sys.stdout = sys.__stdout__


