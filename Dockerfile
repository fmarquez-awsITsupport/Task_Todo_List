# 1. Imagen base
FROM python:3.10-slim

# 2. Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# 3. Copiar el requirements.txt al contenedor
COPY requirements.txt .

# 4. Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar todo el código fuente del proyecto al contenedor
COPY . .

# 6. Indicar el puerto que Flask va a usar
EXPOSE 5000

# 7. Comando para arrancar tu app Flask
CMD ["python", "run.py"]
