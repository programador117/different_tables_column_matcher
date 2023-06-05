# Asociación de Columnas en Tablas de Excel

Este repositorio contiene un script de Python que te permite asociar automáticamente las columnas de dos tablas de Excel con nombres de columnas diferentes.

## ¿Cómo funciona?

El script lee automáticamente dos archivos de Excel en una carpeta llamada `compared_tables`, encuentra las coincidencias entre las columnas de ambas tablas y guarda los resultados en una carpeta llamada `comparison_results`. El script permite un cierto número de valores adicionales en las columnas de la tabla B (por si tiene alguno extra que no está en la tabla A) y utiliza los nombres de los archivos (sin la extensión `.xlsx` y sin el prefijo `A_` o `B_`) para nombrar las columnas en los archivos de resultados.

## ¿Cómo usarlo?

1. Asegúrate de tener instaladas las librerías `pandas` y `openpyxl`.
2. Coloca tus archivos de Excel en una carpeta llamada `compared_tables`. Los nombres de los archivos deben comenzar con `A_` y `B_` respectivamente para identificar cuál tabla es `A` y cuál es `B`(Se agrega `A_` o `B_` al comienzo de los nombres de los archivos si no lo tienen).
3. Ejecuta el script con el comando `python script.py`.
4. Revisa los archivos en la carpeta `comparison_results` para ver los resultados.

## Contribuciones

Si tienes alguna sugerencia o mejora para el código, no dudes en hacer un pull request o abrir un issue. ¡Toda contribución es bienvenida!
