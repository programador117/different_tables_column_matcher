import os
import pandas as pd

folder_tables_to_compare = 'compared_tables'
folder_comparison_results = 'comparison_results'

# Establecer el número máximo de valores adicionales permitidos
max_additional_values = 2

# Obtener la lista de archivos en la carpeta folder_tables_to_compare
excel_files = [f for f in os.listdir(folder_tables_to_compare) if f.endswith('.xlsx')]

# Asegurarse de que hay exactamente dos archivos de Excel en la carpeta
assert len(excel_files) == 2, f"Debe haber exactamente dos archivos de Excel en la carpeta {folder_tables_to_compare}"

# Verificar que los nombres de los archivos comiencen con 'A_' y 'B_' respectivamente
assert excel_files[0].startswith('A_') and excel_files[1].startswith('B_'), "Los nombres de los archivos deben comenzar con 'A_' y 'B_' respectivamente"

# Crear las rutas completas a los archivos de Excel
excel_file_1 = os.path.join(folder_tables_to_compare, excel_files[0])
excel_file_2 = os.path.join(folder_tables_to_compare, excel_files[1])

# Obtener nombres de archivos sin extensión y sin A_ o B_ para nombrar las columnas de los documentos resultantes
excel_file_1_name = excel_files[0].replace('.xlsx', '').replace('A_', '')
excel_file_2_name = excel_files[1].replace('.xlsx', '').replace('B_', '')

# Leer las tablas en DataFrames de pandas
df_a = pd.read_excel(excel_file_1)
df_b = pd.read_excel(excel_file_2)

# Crear un diccionario vacío para almacenar las coincidencias
column_matches = {}

# Crear una lista vacía para almacenar las columnas inciertas
uncertain_columns = []

# Iterar sobre las columnas de la tabla B
for col_b in df_b.columns:
    # Obtener los valores de la columna actual en la tabla B (excluyendo los valores vacíos)
    b_values = set(df_b[col_b].dropna().values)
    
    # Crear una lista vacía para almacenar las columnas coincidentes en la tabla A
    matching_a_columns = []
    
    # Iterar sobre las columnas de la tabla A
    for col_a in df_a.columns:
        # Verificar si la columna A ya ha sido asociada con una columna B
        if col_a not in column_matches.values():
            # Obtener los valores de la columna actual en la tabla A (excluyendo los valores vacíos)
            a_values = set(df_a[col_a].dropna().values)
            
            # Calcular el número de valores adicionales en la columna B
            additional_values = len(b_values.difference(a_values))
            
            # Si todos los valores de la columna B están contenidos en la columna A, agregar el nombre de la columna A a la lista de columnas coincidentes
            if len(b_values) > 0 and len(a_values.intersection(b_values)) > 0: 
                if (b_values.issubset(a_values)) or (additional_values <= max_additional_values and abs(len(a_values) - len(b_values)) == additional_values):
                    matching_a_columns.append(col_a)
    
    # Si solo hay una columna coincidente en la tabla A, agregar el par de nombres de columnas al diccionario
    if len(matching_a_columns) == 1:
        column_matches[col_b] = matching_a_columns[0]
    # Si hay varias columnas coincidentes en la tabla A, agregar la columna B y las columnas coincidentes a la lista de columnas inciertas
    elif len(matching_a_columns) > 1:
        uncertain_columns.append([col_b, ', '.join(matching_a_columns)])

# Crear un DataFrame a partir del diccionario de coincidencias
matches_df = pd.DataFrame(list(column_matches.items()), columns=[excel_file_2_name, excel_file_1_name])

# Crear la carpeta folder_comparison_results si no existe
if not os.path.exists(folder_comparison_results):
    os.makedirs(folder_comparison_results)

# Guardar el DataFrame en un archivo de Excel en la carpeta folder_comparison_results
matches_df.to_excel(os.path.join(folder_comparison_results, 'column_matches.xlsx'), index=False)

# Crear un DataFrame a partir de la lista de columnas inciertas
uncertain_df = pd.DataFrame(uncertain_columns, columns=[excel_file_2_name, f'Matching "{excel_file_1_name}" columns'])

# Guardar el DataFrame en un archivo de Excel en la carpeta folder_comparison_results
uncertain_df.to_excel(os.path.join(folder_comparison_results, 'columns_uncertain.xlsx'), index=False)