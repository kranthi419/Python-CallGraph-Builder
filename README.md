# Function Call Graph Generator

This project generates a function call graph from a given Python source file. It uses the `ast` module to parse the source code into an Abstract Syntax Tree (AST) and `networkx` to create and visualize the call graph.

## Features

- Parses Python source code to extract function definitions and calls.
- Generates a directed graph representing the function call relationships.
- Visualizes the call graph using `matplotlib`.

## Getting Started

### Prerequisites

- Python 3.x
- `networkx` library
- `matplotlib` library

You can install the required libraries using pip:

```sh
pip install networkx matplotlib