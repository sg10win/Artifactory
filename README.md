# Simple Python Artifactory  

## Overview  
This is a lightweight artifactory site that allows users to download Python libraries through a simple web interface. The application is built with **FastAPI** and serves library files stored in a local directory.  

### Features  
- Download Python libraries by filename.  
- User-friendly web interface powered by Jinja2 templates.  
- Automatic initialization of the library database on startup.  

### Limitations  
- Does not currently support uploading new libraries.  
- Assumes all libraries are pre-stored in a `files` directory.  

---

## Installation  

### Prerequisites  
- Python 3.8 or higher.  
- FastAPI and Uvicorn installed.  

### Steps  
1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/yourusername/simple-python-artifactory.git  
   cd simple-python-artifactory  
  ```
