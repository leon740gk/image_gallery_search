FROM python:3.8.6-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV SRC=./
ENV SRVHOMEDIR=/srv

# Update the default application repository sources list
RUN apt-get update && apt-get install -y \
  vim \
  nginx \
  supervisor \
  tmux \
  htop

# Create application subdirectories
WORKDIR $SRVHOMEDIR
RUN mkdir media static logs
VOLUME ["$SRVHOMEDIR/logs/"]

# Copy application source code to SRCDIR
COPY $SRC $SRVHOMEDIR

# Install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r $SRVHOMEDIR/requirements.txt

EXPOSE 8000
