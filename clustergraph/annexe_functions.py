                                            #####################                 
                                            # ANNEXES FUNCTIONS #
                                            #####################

            
"""
Function which in a numpy darray replace the crossing positions values for the lines list_1 and columns list_2 and inverse (symetric change) , by the value wanted

Returns teh darray modified

Parameters :
-val : the value we want to be in those positions
-list_1 and list_2 : the rows and columns in which we want to change the value (are lists or arrays)
-arr : the darray that we want to modify
"""
def replace_in_array(list_1,list_2, arr, val) :
    for i in list_1 :
        for j in list_2 :
            arr[i,j] = val
            arr[j,i] = val
    return arr

"""            
Function which inserts in a ordered list a new element. Each element has this form [keys_1, keys_2, value] and we order depending of on the 'value' element.
Returns the ordered list with the new element
Parameters :
- liste : list of element each element is represented by a list [keys_1, keys_2, value], the list is already ordered based on the 'value'
- element_to_insert : list as followed [keys_1, keys_2, value] that we want to insert in the list by keeping it ordered
"""
def insert_sorted_list(liste, element_to_insert):
    if(len(element_to_insert) < 3 ) :
        raise ValueError("Element to insert has less than 3 elements")
        
    index = len(liste)
    if(liste==[]) :
        return [element_to_insert]
    # Searching for the position
    for i in range(len(liste)):
        if liste[i][2] > element_to_insert[2]:
            index = i
            break
    if index == len(liste):
        liste = liste[:index] + [element_to_insert]
    else:
        liste = liste[:index] + [element_to_insert] + liste[index:]

    return liste


#-------------------------------------------------------
# Function which from a list of element [keys, value] return a list of the values
def get_values(list_key_value) :
    if(list_key_value == [] ) :
        raise ValueError("List is empty")
    values = []
    for i in list_key_value :
        values.append(i[1])
    return values



"""
From a graph, return a list of edges ordered from shortest to longest one

Return list of edge and each edge has this representation  [node_i, node_j, length_edge]

Parameters :
-graph : networkx graph from which we want to get the edges ordered
-variable_length : string which is the label which lets us compare and then order from shortest to longest
"""
def get_sorted_edges(graph, variable_length = 'label') : 
    edges = []  
    for edge in graph.edges :
        edges= insert_sorted_list(edges, [edge[0], edge[1], graph.edges[edge][variable_length] ])
        
    return edges




"""
Functions which returns a list of edges connecting only the given vertices to each others
- edges : list of edges and each edge is a list like [vertice_i, vertice_j, length_edge]
- vertices : list of integers and each integers represent a vertice
"""
def get_corresponding_edges(vertices, edges) : 
    corres_edges = []
    for edge in edges :
        if(edge[0] in vertices and edge[1] in vertices) :
            corres_edges = insert_sorted_list(corres_edges, edge)
    return corres_edges




"""
Functions which from a graph and often the points covered, returns the nodes which covers the most points
Returns the maximum length of the given variable (expected to get a list for this label in each nodes)

Parameters :
- graph : netowrkx graph for which we want to know to biggest node
- variable : string which correspond to the label in the graph for which we want to compare to get the maximum size
- nodes : list of integers in case we want to limit the reseach to some specific nodes
"""
def max_size_node_graph(graph, variable, nodes = None) :
    if(not(nodes)):
        nodes = graph.nodes
    maxi =0    
    for node in nodes :
        #print("NODE", node)
        #print("TEST", graph.nodes[node][variable])
        size = len(graph.nodes[node][variable])
        if(size> maxi) :
            maxi = size
    return maxi





