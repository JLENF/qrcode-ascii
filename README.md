# QR Code ASCII Generator

A web application that generates QR codes and displays them as ASCII art.

### Example QR Code ASCII

```
 ▄▄▄▄▄▄▄▄▄   ▄    ▄▄  ▄▄▄▄  ▄  ▄▄▄▄▄▄▄▄▄
 █ ▄▄▄▄  █ ▀▀█▄▄█▀  ▄█▀▀▀▄  █  █ ▄▄▄▄  █
 █ ████  █ ▄▄█▀▀█   ▀▀   ▀  ▀  █ ████  █
 █ ▀▀▀▀  █ ▄▄ ██ ▀██▄▄██▄▀  ▀  █ ▀▀▀▀  █
 █▄▄▄▄▄▄▄█ ██ ██ ▄▀▀█▀██▀▄  ▄  █▄▄▄▄▄▄▄█
 ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ █▀▀▄▄  ▄█▄▄▀▄▄ ▄  ▄ ▄▄ 
 █▀██▀█▄▄▀▀███▀▀ ▀  ▀▀▄▄██▀▀▄▀▀▄█▄▄▀ ▀▀▄
   ██ █  █   █  ██   ████        ██     
 █ ▀▀▀ ▄▄▄ ▀▀█▀▀█   ▀▄▄▄▄ ██       █▄▀▀ 
     ████ ██████ ████ ██    ███████    █
 ██▀▀ ▀▀▀▀█▀▀▀▄▄ ▄██▀█▀▀ ▀▄▄███▄▄██▀▀▄▄ 
     ██████  ███ █  ██  █ ██ ██ █  ██   
 █ ██▀▀██▄█▀▀█▀▀▄▄   ▄██▄▄▀▀▄▀▀████ █  ▀
 █ ██ █   █   ███   ████ █  ████     ██ 
 ▀ ▀▀▀ ▀▀▀ ▄▄▀▀▀▀▄▄▄▄   ▀▄▀▀█▀▀▀▀██▄████
 ▄▄▄▄▄▄▄▄▄ ██▄   ▀███▄▄▄▄█▄▄█  ▄ ████▀▀▀
 █ ▄▄▄▄  █ ▄▄▀▄▄ █▀▀▄█▀▀▄ ▀▀█▄▄▄▄██ ▄   
 █ ████  █ ██ ██ ▀  ▀▀▄▄█▄▄▄█▀▀▀▀▀▀▄█▄▄▄
 █ ▀▀▀▀  █ ███  █▀  ▄█▄▄▀ ▀▀███▀█▀▀█▀██ 
 █▄▄▄▄▄▄▄█ ███  █   ▀█▀▀▄ ▄▄▀▀▀▄█▄▄▀▄▀▀
```

## Overview

This project allows you to convert text or URLs into QR codes and view them in both ASCII art format and as standard QR code images.

This project was inspired by [asciiqr.com](http://asciiqr.com/), but has been completely rewritten using Python and Flask. The original project used PHP and the deprecated Google Chart API for QR code generation. This version uses the modern [QR Server API](https://goqr.me/api/) and Python's image processing capabilities for more accurate ASCII art generation.

### Features

- Generate QR codes from any text or URL
- Display QR codes as ASCII art using block characters (█, ▀, ▄)
- View the QR code as a standard image
- Modern, responsive web interface
- Docker containerized for easy deployment

## Getting Started

### Prerequisites

- Docker and Docker Compose (for containerized setup)
- Python 3.8+ with pip (for local development)

### Running with Docker

1. Clone this repository
2. Navigate to the project directory
3. Run the Docker Compose command:

```bash
docker-compose up -d
```

4. Access the application at http://localhost:5001

### Local Development

1. Clone this repository
2. Navigate to the project directory
3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Access the application at http://localhost:5001

## How It Works

The application works as follows:

1. User submits text or a URL to be encoded
2. The app sends a request to the QR Server API to generate a QR code image
3. Python's Pillow library processes the image to detect QR code patterns
4. The image is converted to ASCII art using Unicode block characters
5. Both the ASCII art and the original QR code image are displayed to the user

## License

This project is open source and available under the MIT License.

## Acknowledgements

- Inspired by [asciiqr.com](http://asciiqr.com/)
- Uses the [QR Server API](https://goqr.me/api/) for QR code generation
- Built with Python, Flask, and Pillow
