import ast
import networkx as nx
import matplotlib.pyplot as plt


class CallGraphVisitor(ast.NodeVisitor):
    def __init__(self):
        self.call_graph = nx.DiGraph()
        self.current_function = None

    def visit_FunctionDef(self, node):
        # Register each function definition
        function_name = node.name
        self.current_function = function_name
        self.call_graph.add_node(function_name)

        # Visit the function body to find function calls
        self.generic_visit(node)
        self.current_function = None

    def visit_Call(self, node):
        # Register each function call
        if isinstance(node.func, ast.Name):  # direct function call
            called_function = node.func.id
        elif isinstance(node.func, ast.Attribute):  # object method call
            called_function = node.func.attr
        else:
            called_function = None

        if self.current_function and called_function:
            # Add an edge from the caller to the callee
            self.call_graph.add_edge(self.current_function, called_function)

        # Visit further in case of nested calls
        self.generic_visit(node)


def create_call_graph_from_file(file_path: str):
    # Read the source code from the file
    with open(file_path, 'r') as file:
        source_code = file.read()

    # Parse the source code into an AST and create the call graph
    tree = ast.parse(source_code)
    visitor = CallGraphVisitor()
    visitor.visit(tree)
    return visitor.call_graph


def draw_call_graph(call_graph: nx.DiGraph):
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(call_graph)
    nx.draw(call_graph, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold",
            edge_color="gray")
    plt.title("Function Call Graph")
    plt.show()


if __name__ == '__main__':
    # Example usage
    file_path_ = 'code-sample/sample_2.py'  # Replace with the path to your Python file
    call_graph_ = create_call_graph_from_file(file_path_)
    draw_call_graph(call_graph_)
