# Splunk App Icon Generator

A Flask-based web application that automates the creation of icon assets for Splunk Apps. It takes a single high-resolution source image and generates all the required PNG files with the correct filenames and dimensions specified in the [Splunk Developer Guide](https://dev.splunk.com/enterprise/docs/developapps/createapps/).

## Features

- **One-Click Generation**: Upload one image, get a ZIP file with all required assets.
- **Smart Resizing**:
  - Forces square dimensions for app icons (`36x36`, `72x72`).
  - Preserves aspect ratio for navigation logos (`160x40`, `320x80`).
  - **Splunk Ready**: The downloaded ZIP includes a `README.txt` with specific installation instructions for your Splunk instance.

## Installation

### Prerequisites

- Python 3.8+
- pip

### Local Setup

1. Clone the repository

```bash
$ git clone https://github.com/Tes3awy/splunk-icon-generator.git
$ cd splunk-icon-generator
```

2. Create a virtual environment

```bash
$ python -m venv .venv --upgrade-deps
$ source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies

```bash
$ pip install -r requirements.txt
```

4. Run the application

```bash
$ flask run # Or python app.py
```

### Docker Usage

You can also run this application in a container without installing Python locally.

1. Build the image

```bash
docker build -t splunk-icon-gen .
```

2. Run the container

```bash
docker run -p 8080:8080 splunk-icon-gen
```

Open your browser to `http://127.0.0.1:8080`.


## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contributing

Contributions are welcome!