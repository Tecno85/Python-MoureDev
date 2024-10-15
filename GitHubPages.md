
### Paso 1: Crea un repositorio en GitHub
1. Inicia sesión en tu cuenta de [GitHub](https://github.com).
2. Crea un **nuevo repositorio**:
   - Dale un nombre a tu repositorio. Para crear una página personal, el repositorio debe llamarse: `tu-nombre-de-usuario.github.io`.
   - Elige que sea público y no es necesario inicializar con un README (puedes agregarlo después).

### Paso 2: Clona el repositorio localmente
1. Abre Git Bash o tu terminal.
2. Clona el repositorio que creaste a tu máquina local usando:
   ```bash
   git clone https://github.com/tu-nombre-de-usuario/tu-repositorio.git
   ```

### Paso 3: Agrega el contenido de tu web
1. Navega hasta el repositorio clonado en tu máquina:
   ```bash
   cd tu-repositorio
   ```
2. Crea o agrega los archivos de tu página web en este directorio. Esto incluirá un archivo `index.html`, que es la página principal.

### Paso 4: Realiza commit y push de los archivos
1. Añade los archivos al repositorio:
   ```bash
   git add .
   ```
2. Realiza un commit de los cambios:
   ```bash
   git commit -m "Publicar mi sitio web"
   ```
3. Sube los archivos a GitHub:
   ```bash
   git push origin main
   ```

### Paso 5: Configura GitHub Pages
1. En GitHub, ve a la configuración de tu repositorio.
2. Desplázate hacia abajo hasta la sección **Pages**.
3. En la sección **Source**, selecciona la rama `main` y luego la carpeta `/root` como fuente.
4. Guarda los cambios.

### Paso 6: Accede a tu web
Después de unos minutos, tu sitio estará disponible en la URL: `https://tu-nombre-de-usuario.github.io`.

¡Listo! Tu web está publicada.