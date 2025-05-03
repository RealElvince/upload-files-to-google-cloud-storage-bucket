FROM python:3.13-slim



# Set the working directory
WORKDIR /app

# Copy all files into the container at /app
COPY . /app


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make entrypoint.sh executable
RUN chmod +x /app/scripts/entrypoint.sh

# entrypoint.sh is a script that will be run when the container starts
ENTRYPOINT [ "/bin/bash", "/app/scripts/entrypoint.sh" ]
