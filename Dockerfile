FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR ./

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5002

# Command to run the app
CMD ["python", "app.py"]
