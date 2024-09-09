# Network Diagram Plotter with Interactive GUI

This project is a Python-based application that allows users to visualize network diagrams from an Excel file containing GPS coordinates. The diagram is interactive and allows zooming, dragging, node selection, and highlighting of links within specified hops. The tool provides a GUI for selecting the input file, the number of hops, and other options.

## Features

- **Interactive Network Diagram**: Displays a network graph with nodes and edges based on coordinates in an Excel file.
- **Node Highlighting**: Click on a node to highlight connected links up to a user-specified number of hops.
- **Zoom and Drag Support**: Use the mouse scroll to zoom in and out, and drag the diagram with a left-click hold.
- **Node Labels**: The name of each node is displayed above its icon.
- **Link Highlighting**: The tool can either keep highlighted links for all clicked nodes or reset highlights with each new click.
- **GUI for Ease of Use**: The GUI prompts users to select an Excel file, input the number of hops, and configure other settings.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/i-tri/network-diagram-plotter.git
   cd network-diagram-plotter
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that you have **Python 3.10+** installed on your system.

4. Install the following dependencies:
   - `pandas`
   - `matplotlib`
   - `networkx`
   - `tkinter` (comes pre-installed with most Python distributions)

## Usage

1. Run the application by executing the following command:
   ```bash
   python Network_Plotter.py
   ```

2. The GUI will open, prompting you to:
   - **Select the Excel file**: The file should contain GPS coordinates of nodes and links.
   - **Specify the number of hops**: Determine how many hops to calculate when highlighting links from the selected node.
   - **Keep highlighted links**: Choose whether to keep highlighted links after selecting a new node or reset them.

3. Once the file is selected and the hops are specified, click **"Select File and Plot"** to visualize the network diagram.

4. Interact with the network by:
   - **Clicking nodes** to highlight links within the specified hops.
   - **Scrolling** to zoom in or out.
   - **Dragging** the diagram to move it around the screen.

## Excel File Format

The Excel file should contain the following columns:

- **A-End Site Name**: The name of the starting node (e.g., a router).
- **Site-A Latitude**: The latitude coordinate of the starting node.
- **Site-A Longitude**: The longitude coordinate of the starting node.
- **Z-End Site Name**: The name of the ending node.
- **Site-Z Latitude**: The latitude coordinate of the ending node.
- **Site-Z Longitude**: The longitude coordinate of the ending node.
- **Link ID**: (Optional) A unique identifier for the link.
- **Link Capacity**: The capacity of the link (optional for plotting).

## Screenshots
### Excel sheet column format:
<img width="710" alt="Network Plotter excel" src="https://github.com/user-attachments/assets/5f0636e7-00b3-4eea-b9e3-ba09bca3fa60">


### GUI that open once application is running:
<img width="202" alt="Network Plotter GUI" src="https://github.com/user-attachments/assets/74b33b07-ebe5-4be6-9c54-de67deb851fc">

### Network drawn, but no selection made as yet:
<img width="752" alt="Network Plotter GUI No Selection" src="https://github.com/user-attachments/assets/02c72de2-620c-484f-af9d-354e76aa8320">

### Selection made, Node colour change and paths highlighted:
<img width="751" alt="Network Plotter GUI With Selection" src="https://github.com/user-attachments/assets/e27023fb-9b64-42f1-8ad8-03f88fb9d184">


## Troubleshooting

- Ensure that the input Excel file contains valid GPS coordinates.
- If the plot does not display correctly, check the scaling of latitude and longitude values in the dataset.
- Install any missing packages by running `pip install package_name`.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you'd like to improve the tool.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Test it yourself
Download the attached excel file with sites cities and links to test the application.

---

