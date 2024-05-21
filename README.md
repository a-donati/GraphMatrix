# GraphMatrix
School Project.

`In graph theory and computer science, an adjacency matrix is a square matrix used to represent a finite graph. The elements of the matrix indicate whether pairs of vertices are adjacent or not in the graph.`

1. Ask for the number of vertices:
    - Prompt the user to enter integer `n` that represents the number of vertices in the graph. This integer should be between 2 and 5.
2. Initialize the adjacency matrix:
    - Create an `n x n` matrix filled with zeros. The matrix will represent the graph where the entry at row `i` and column `j` will store the weight of the edge from the vertex `i` to vertex `j`
3. Ask for the edges:
    - `2 * n` edges are needed for a directed graph. For each edge, prompt the user to enter three integers: `i` (origin vertex), `j` (destination vertex), and `w` (weight of the edge).
4. Update the adjacency matrix:
    - Use the egde information provided by the user input to update the entries in the adjacency matrix.
5. Print the adjacency matrix:
    - Display the final adjacency matrix.