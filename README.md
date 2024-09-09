This project is a Python-based application that allows users to visualize network diagrams from an Excel file containing GPS coordinates. The diagram is interactive and allows zooming, dragging, node selection, and highlighting of links within specified hops. The tool provides a GUI for selecting the input file, the number of hops, and other options.

Features
Interactive Network Diagram: Displays a network graph with nodes and edges based on coordinates in an Excel file.
Node Highlighting: Click on a node to highlight connected links up to a user-specified number of hops.
Zoom and Drag Support: Use the mouse scroll to zoom in and out, and drag the diagram with a left-click hold.
Node Labels: The name of each node is displayed above its icon.
Link Highlighting: The tool can either keep highlighted links for all clicked nodes or reset highlights with each new click.
GUI for Ease of Use: The GUI prompts users to select an Excel file, input the number of hops, and configure other settings.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/network-diagram-plotter.git
cd network-diagram-plotter
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Ensure that you have Python 3.10+ installed on your system.

Install the following dependencies:

pandas
matplotlib
networkx
tkinter (comes pre-installed with most Python distributions)
Usage
Run the application by executing the following command:

bash
Copy code
python Network_Plotter.py
The GUI will open, prompting you to:

Select the Excel file: The file should contain GPS coordinates of nodes and links.
Specify the number of hops: Determine how many hops to calculate when highlighting links from the selected node.
Keep highlighted links: Choose whether to keep highlighted links after selecting a new node or reset them.
Once the file is selected and the hops are specified, click "Select File and Plot" to visualize the network diagram.

Interact with the network by:

Clicking nodes to highlight links within the specified hops.
Scrolling to zoom in or out.
Dragging the diagram to move it around the screen.
Excel File Format
The Excel file should contain the following columns:

A-End Site Name: The name of the starting node (e.g., a router).
Site-A Latitude: The latitude coordinate of the starting node.
Site-A Longitude: The longitude coordinate of the starting node.
Z-End Site Name: The name of the ending node.
Site-Z Latitude: The latitude coordinate of the ending node.
Site-Z Longitude: The longitude coordinate of the ending node.
Link ID: (Optional) A unique identifier for the link.
Link Capacity: The capacity of the link (optional for plotting).
Screenshots
Excel sheet columns:
<img width="710" alt="Network Plotter excel" src="https://github.com/user-attachments/assets/2308fc8d-9389-4798-853e-126c0a26227d">


Troubleshooting
Ensure that the input Excel file contains valid GPS coordinates.
If the plot does not display correctly, check the scaling of latitude and longitude values in the dataset.
Install any missing packages by running pip install package_name.
Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request if you'd like to improve the tool.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or suggestions, feel free to contact me via email at [your-email@example.com].


