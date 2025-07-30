#"Start with a clean machine that already has Python 3.10.3 installed."
FROM python:3.10.3

# Inside the container, work inside a folder called /app
WORKDIR /app

# Take requirements.txt from my computer and copy it into the container's /app folder
COPY requirements.txt .

#Database credentials or URL — kept outside the image for security and flexibility.


# Install all the Python libraries listed in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m venv venv

# Copy everything (your app files) into the container.
COPY . .

# Expose port (change if your app uses a different port)
EXPOSE 8000


# Run FastAPI app with uvicorn
#The server inside the container listens on all network interfaces — basically, it accepts connections from anywhere inside the container’s network.
#This line starts your FastAPI app inside the Docker container and makes it accessible from outside the container on port 8000.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# To build the Docker image, run:
# docker build -t imagename .

# To run the container, use:
# docker run -p 8000:8000 imagename its like uvicorn main:app 






