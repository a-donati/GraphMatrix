

def get_edges(n):
    temp = n * 2
    edges = []
    for x in range(temp):
        i = int(input("Enter the origin"))
        j = int(input("Enter the destination"))
        w = int(input("Enter the edge weight "))
        edges.append([i,w,j])
        print(edges)
        return edges
    

def main():
    user_input = int(input("Enter the number of vertices from 2 to 5 "))
    get_edges(user_input)
    
main()