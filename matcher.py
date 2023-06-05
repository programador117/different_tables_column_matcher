import os
import pandas as pd

folder_tables_to_compare = 'compared_tables'
folder_comparison_results = 'comparison_results'
# Obtener la lista de archivos en la carpeta folder_tables_to_compare
excel_files = [f for f in os.listdir(folder_tables_to_compare) if f.endswith('.xlsx')]

# Asegurarse de que hay exactamente dos archivos de Excel en la carpeta
assert len(excel_files) == 2, f"Debe haber exactamente dos archivos de Excel en la carpeta {folder_tables_to_compare}"

# Crear las rutas completas a los archivos de Excel
excel_file_1 = os.path.join(folder_tables_to_compare, excel_files[0])
excel_file_2 = os.path.join(folder_tables_to_compare, excel_files[1])

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
        # Obtener los valores de la columna actual en la tabla A (excluyendo los valores vacíos)
        a_values = set(df_a[col_a].dropna().values)
        
        # Si todos los valores de la columna B están contenidos en la columna A, agregar el nombre de la columna A a la lista de columnas coincidentes
        if b_values.issubset(a_values):
            matching_a_columns.append(col_a)
    
    # Si solo hay una columna coincidente en la tabla A, agregar el par de nombres de columnas al diccionario
    if len(matching_a_columns) == 1:
        column_matches[col_b] = matching_a_columns[0]
    # Si hay varias columnas coincidentes en la tabla A, agregar la columna B y las columnas coincidentes a la lista de columnas inciertas
    elif len(matching_a_columns) > 1:
        uncertain_columns.append([col_b, ', '.join(matching_a_columns)])

# Crear un DataFrame a partir del diccionario de coincidencias
matches_df = pd.DataFrame(list(column_matches.items()), columns=['B', 'A'])

# Guardar el DataFrame en un archivo de Excel
matches_df.to_excel('column_matches.xlsx', index=False)

# Crear un DataFrame a partir de la lista de columnas inciertas
uncertain_df = pd.DataFrame(uncertain_columns, columns=['B', 'Matching A columns'])

# Guardar el DataFrame en un archivo de Excel
uncertain_df.to_excel('columns_uncertain.xlsx', index=False)
