
# Asociación de Columnas en Tablas de Excel

Este repositorio contiene un script de Python que te permite asociar automáticamente las columnas de dos tablas de Excel con nombres de columnas diferentes.

## ¿Cómo funciona?

El script lee ambas tablas en `DataFrames` de `pandas` y luego itera sobre las columnas de ambas tablas para encontrar coincidencias en los valores. Si una columna en la tabla B tiene valores que son un subconjunto de los valores en una columna de la tabla A, el script agrega el par de nombres de columnas a un diccionario. Luego, el script guarda el diccionario en un archivo de Excel con dos columnas llamadas A y B.

Si hay varias columnas en la tabla B que coinciden con la misma columna en la tabla A, el script guarda esas columnas en un archivo de Excel separado llamado `columns_uncertain.xlsx`.

## ¿Cómo usarlo?

1. Asegúrate de tener instaladas las librerías `pandas` y `openpyxl`.
2. Coloca tus archivos de Excel en el mismo directorio que el script y asegúrate de que los nombres de los archivos sean `tabla_a.xlsx` y `tabla_b.xlsx`.
3. Ejecuta el script con el comando `python script.py`.
4. Revisa los archivos `column_matches.xlsx` y `columns_uncertain.xlsx` para ver los resultados.

## Contribuciones

Si tienes alguna sugerencia o mejora para el código, no dudes en hacer un pull request o abrir un issue. ¡Toda contribución es bienvenida!
