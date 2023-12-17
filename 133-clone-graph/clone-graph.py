class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
    
    # Use a dictionary to map original nodes to their corresponding copies
        node_dict = {}
    
    # Define a recursive DFS function to traverse and clone the graph
        def dfs(original):
        # If the original node has already been cloned, return its copy
            if original in node_dict:
                return node_dict[original]
        
        # Create a copy of the current node
            copy_node = Node(original.val)
        
        # Add the copy node to the dictionary
            node_dict[original] = copy_node
        
        # Recursively clone neighbors and add them to the copy node
            for neighbor in original.neighbors:
                copy_node.neighbors.append(dfs(neighbor))
        
            return copy_node
    
    # Start DFS from the given node (val = 1)
        return dfs(node)
        