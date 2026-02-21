# Use a tiny base image
FROM python:3.11-slim

# Install only the necessary runpod library
RUN pip install --no-cache-dir runpod

# Copy our mock handler into the root
COPY handler.py /handler.py

# Run the handler with unbuffered output so logs show up instantly
CMD [ "python", "-u", "/handler.py" ]