# Fiesta Online Map Generator

## Project Documentation
This project is a map generator for the game Fiesta Online. It allows users to create and customize game maps with ease.

## Features
- Generate maps for different game modes.
- Customize terrain and objects.
- Export maps in the required format for Fiesta Online.

## Setup Instructions
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/mariosanlina-ai/fiesta-map-generator.git
   cd fiesta-map-generator
   ```  

2. **Install dependencies:**  
   Make sure you have Python (version 3.7 or higher) installed.  
   ```bash
   pip install -r requirements.txt
   ```  

3. **Run the application:**  
   ```bash
   python main.py
   ```

## Usage Examples
Once the application is running, you can generate a new map using the following commands:

1. **Create a new map:**  
   ```bash
   create_map --name "MyFirstMap" --mode adventure
   ```

2. **Customize the map:**  
   Add terrain and objects with the following commands:  
   ```bash
   add_terrain --type grass --coordinates 10,15
   add_object --type tree --coordinates 12,15
   ```

3. **Export the map:**  
   ```bash
   export_map --name "MyFirstMap" --format json
   ```

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries, please reach out to:  
**Mariosan Lina**  
[mariosanlina-ai@example.com](mailto:mariosanlina-ai@example.com)  

Happy mapping!