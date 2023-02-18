FROM ubuntu:latest

# Update the package manager and install SSH
RUN apt-get update && \
    apt-get -y install openssh-server

# Install Python 3.7 and related packages
RUN apt-get -y install software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get -y install python3.7 python3.7-dev python3-pip python3.7-venv

# Install pip for Python 3.7
RUN python3.7 -m ensurepip --default-pip && \
    ln -s /usr/bin/pip3.7 /usr/local/bin/pip

RUN python3.7 -m pip install uncompyle6

# Create a new user for SSH access
RUN useradd -ms /bin/bash jafffy

# Set the password for the new user
RUN echo 'jafffy:asdf700' | chpasswd
RUN echo 'root:asdf700' | chpasswd

# Copy the updated SSH configuration file
COPY sshd_config /etc/ssh/sshd_config

# Restart the SSH daemon to apply the new configuration
RUN service ssh restart

# Set the working directory to the new user's home directory
WORKDIR /home/jafffy

# Start the SSH service
CMD ["/usr/sbin/sshd", "-D"]

