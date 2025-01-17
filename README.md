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

## Installation  

### Prerequisites  
- Python 3.8 or higher.  
- FastAPI and Uvicorn installed.  

### Steps  
1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/sg10win/artifactory.git  
   cd artifactory  
   ```  

2. **Install Dependencies**:  
   ```bash  
   pip install fastapi uvicorn jinja2  
   ```  

3. **Prepare Your Libraries**:  
   - Create a `files` directory in the project root.  
   - Place the `.whl` or other library files in this directory.  

4. **Set Up Templates**:  
   - Ensure you have an `index.html` file in the `templates` directory for the web interface.  

5. **Run the Application**:  
   ```bash  
   python main.py  
   ```  

6. **Access the App**:  
   Open a browser and navigate to `http://127.0.0.1:8080`.  

## API Endpoints  

### 1. Download a Library  
**Endpoint**: `GET /root/{p_name}`  
- **Description**: Downloads a file by its name.  
- **Response**:  
  - File response if the file exists.  
  - JSON message if the file does not exist.  

### 2. View Libraries  
**Endpoint**: `GET /root/ui` or `GET /`  
- **Description**: Displays the list of available libraries in a web interface.  

## Example Directory Structure  
```plaintext  
simple-python-artifactory/  
├── files/  
│   ├── library1.whl  
│   ├── library2.whl  
├── templates/  
│   └── index.html  
├── main.py  
```
