# Use a Python 3.7 image (Debian-based)
FROM python:3.7

# Install development libraries for PortAudio (Debian-based)
RUN apt-get update && apt-get install -y \
    libasound-dev \
    libportaudio2 \
    libportaudiocpp0 \
    portaudio19-dev \
    usbutils \
    espeak

# Install required libraries
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your project files
COPY . .

# Add entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set working directory
WORKDIR /app

# Use host's PulseAudio server
ENV PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native

# Add user to the audio group for access to audio devices
RUN groupadd -r docker && usermod -aG audio docker

# Set permissions for PulseAudio socket
RUN mkdir -p /var/run/pulse && chown -R docker:docker /var/run/pulse

# Entry point
ENTRYPOINT ["/entrypoint.sh"]

# Command to run your script
CMD ["python", "talking_offline_ai.py"]

