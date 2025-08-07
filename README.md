#----- TuPrimeraPagina_Velasquez -----

Autor: Omar Velasquez R.

Este es mi primer proyecto web con Django, creado como tercera entrega del curso de Python en CoderHouse.

La aplicación es una tienda online de productos fitness, en la cual se pueden registrar:

- Productos
- Categorias (de productos)
- Clientes


#----- Funcionalidades -----

- Formulario para agregar productos, incluyendo imagen y categoría.
- Formulario para agregar nuevas categorías.
- Formulario para registrar clientes.
- Búsqueda de productos por nombre.
- Panel de administración (Django Admin).


#----- Rutas para probar en el navegador -----

- Agregar producto --> http://127.0.0.1:8000/agregar-producto/
- Agregar categoría --> http://127.0.0.1:8000/agregar-categoria/ 
- Agregar cliente --> http://127.0.0.1:8000/agregar-cliente/
- Buscar producto --> http://127.0.0.1:8000/buscar-producto/
- Panel de administración --> http://127.0.0.1:8000/admin/


#----- ¿Cómo probarlo? -----

1. Clona el repositorio o descarga el ZIP del proyecto.
2. Instala los requerimientos (opcional):  
   `pip install django pillow`
3. Aplica las migraciones:  
   `python manage.py migrate`
4. Crea un superusuario:  
   `python manage.py createsuperuser`
5. Ejecuta el servidor:  
   `python manage.py runserver`
6. Abre el navegador en:  
   `http://127.0.0.1:8000/`


#----- Notas -----

- Las imágenes se guardan en la carpeta `/media/productos/`
- El proyecto usa una base de datos SQLite (`db.sqlite3`)
