import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import tkinter as tk
from tkinter import filedialog, messagebox

# Create the GUI window
root = tk.Tk()
root.title("Network Plotter")

# Global variables
highlighted_edges = set()
keep_highlighted = tk.BooleanVar(value=False)
hops_value = tk.IntVar(value=3)
prev_x = None
prev_y = None
dragging = False
selected_node = None  # Variable to track the selected node

# Create and place widgets
tk.Label(root, text="Select Excel file and number of hops").pack(pady=10)


# File selection button
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if not file_path:
        return

    hops = hops_value.get()
    if hops < 1:
        messagebox.showerror("Error", "Invalid number of hops. Please enter a positive integer.")
        return

    plot_network(file_path, hops)


tk.Button(root, text="Select File and Plot", command=open_file).pack(pady=10)

# Entry widget for number of hops
tk.Label(root, text="Number of hops:").pack(pady=5)
hops_entry = tk.Entry(root, textvariable=hops_value)
hops_entry.pack(pady=5)

tk.Checkbutton(root, text="Keep highlighted links", variable=keep_highlighted).pack(pady=10)


# Function to load data and plot the network
def plot_network(file_path, max_hops):
    global highlighted_edges, prev_x, prev_y, dragging, selected_node

    # Load the Excel sheet
    df = pd.read_excel(file_path)

    # Clean data
    df = df.dropna(subset=['Site-A Latitude', 'Site-A Longitude', 'Site-Z Latitude', 'Site-Z Longitude'])
    df[['Site-A Latitude', 'Site-A Longitude', 'Site-Z Latitude', 'Site-Z Longitude']] = df[
        ['Site-A Latitude', 'Site-A Longitude', 'Site-Z Latitude', 'Site-Z Longitude']].apply(pd.to_numeric,
                                                                                              errors='coerce')
    df = df.dropna(subset=['Site-A Latitude', 'Site-A Longitude', 'Site-Z Latitude', 'Site-Z Longitude'])

    # Create NetworkX graph
    G = nx.Graph()
    for idx, row in df.iterrows():
        G.add_node(row['A-End Site Name'], pos=(row['Site-A Longitude'], row['Site-A Latitude']))
        G.add_node(row['Z-End Site Name'], pos=(row['Site-Z Longitude'], row['Site-Z Latitude']))
        G.add_edge(row['A-End Site Name'], row['Z-End Site Name'], capacity=row['Link Capacity'])

    # Normalize node positions to fit in plotting space
    pos = nx.get_node_attributes(G, 'pos')

    # Define the plotting area limits based on longitude and latitude ranges
    x_coords, y_coords = zip(*pos.values())
    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)

    # Adjust the scaling of positions for better visualization
    scale_x = 1.0 / (x_max - x_min)
    scale_y = 1.0 / (y_max - y_min)

    pos = {node: (scale_x * (x - x_min), scale_y * (y - y_min)) for node, (x, y) in pos.items()}

    # Plotting the network diagram
    fig, ax = plt.subplots(figsize=(15, 10))
    plt.ion()  # Enable interactive mode

    def draw_network():
        ax.clear()  # Clear the current plot

        # Draw nodes with different colors for the selected node
        node_colors = ['darkblue' if node == selected_node else 'lightblue' for node in G.nodes()]
        nx.draw_networkx_nodes(G, pos, node_size=80, node_color=node_colors, edgecolors='black', ax=ax)

        # Draw edges
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='gray', width=1, alpha=0.5, ax=ax)

        # Draw highlighted edges if any
        if highlighted_edges:
            highlighted_edges_list = [tuple(sorted(edge)) for edge in highlighted_edges]
            nx.draw_networkx_edges(G, pos, edgelist=highlighted_edges_list, edge_color='red', width=2, alpha=0.7, ax=ax)

        # Draw labels above nodes
        nx.draw_networkx_labels(G, pos, labels={node: node for node in G.nodes()}, font_size=8,
                                verticalalignment='bottom', ax=ax)

        # Set axis limits to maintain zoom level
        x_coords, y_coords = zip(*pos.values())
        ax.set_xlim(min(x_coords) - 0.1, max(x_coords) + 0.1)
        ax.set_ylim(min(y_coords) - 0.1, max(y_coords) + 0.1)

        plt.draw()

    def on_scroll(event):
        # Get the current mouse pointer position
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        x_click, y_click = event.xdata, event.ydata

        if x_click is None or y_click is None:
            return

        # Calculate the zoom factor
        zoom_factor = 1.1
        if event.button == 'up':
            # Zoom in
            new_xlim = [x_click - (x_click - xlim[0]) / zoom_factor, x_click + (xlim[1] - x_click) / zoom_factor]
            new_ylim = [y_click - (y_click - ylim[0]) / zoom_factor, y_click + (ylim[1] - y_click) / zoom_factor]
        elif event.button == 'down':
            # Zoom out
            new_xlim = [x_click - (x_click - xlim[0]) * zoom_factor, x_click + (xlim[1] - x_click) * zoom_factor]
            new_ylim = [y_click - (y_click - ylim[0]) * zoom_factor, y_click + (ylim[1] - y_click) * zoom_factor]

        ax.set_xlim(new_xlim)
        ax.set_ylim(new_ylim)
        plt.draw()

    def on_click(event):
        global highlighted_edges, prev_x, prev_y, selected_node
        if event.inaxes != ax:
            return

        # Get the clicked point
        x_click, y_click = event.xdata, event.ydata

        # Find the nearest node to the click
        closest_node = None
        min_dist = float('inf')
        for node, (x, y) in pos.items():
            dist = (x - x_click) ** 2 + (y - y_click) ** 2
            if dist < min_dist:
                min_dist = dist
                closest_node = node

        if closest_node is None:
            return

        # Update the selected node and change its color
        selected_node = closest_node

        # Find all nodes within specified hops
        nodes_within_hops = set()
        for i in range(1, max_hops + 1):  # Up to specified hops
            nodes_within_hops.update(nx.single_source_shortest_path_length(G, closest_node, cutoff=i).keys())

        # Find all edges within specified hops
        edges_within_hops = set()
        for node in nodes_within_hops:
            for neighbor in G.neighbors(node):
                if neighbor in nodes_within_hops:
                    edges_within_hops.add(frozenset([node, neighbor]))

        # Convert frozensets to tuples for compatibility with NetworkX
        edges_within_hops = set(tuple(sorted(edge)) for edge in edges_within_hops)

        # Update highlighted edges based on the checkbox
        if keep_highlighted.get():
            highlighted_edges.update(edges_within_hops)
        else:
            highlighted_edges = edges_within_hops

        # Draw network with highlighted edges and selected node
        draw_network()

    def on_drag(event):
        global prev_x, prev_y, dragging
        if event.inaxes != ax:
            return

        if event.button == 1:  # Left mouse button
            if not dragging:
                dragging = True
                prev_x, prev_y = event.xdata, event.ydata

            def update_drag(event):
                global prev_x, prev_y, dragging
                if event.inaxes != ax or not dragging:
                    return
                dx = event.xdata - prev_x
                dy = event.ydata - prev_y
                xlim = ax.get_xlim()
                ylim = ax.get_ylim()
                ax.set_xlim([x - dx for x in xlim])
                ax.set_ylim([y - dy for y in ylim])
                prev_x, prev_y = event.xdata, event.ydata
                plt.draw()

            fig.canvas.mpl_connect('motion_notify_event', update_drag)

    def stop_drag(event):
        global dragging
        dragging = False
        fig.canvas.mpl_disconnect('motion_notify_event')

    fig.canvas.mpl_connect('button_press_event', on_click)
    fig.canvas.mpl_connect('scroll_event', on_scroll)
    fig.canvas.mpl_connect('button_press_event', on_drag)
    fig.canvas.mpl_connect('button_release_event', stop_drag)

    draw_network()
    plt.show()


root.mainloop()
