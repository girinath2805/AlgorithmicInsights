import io
import numpy as np

def evalSpice(filename):
    sfp = io.StringIO(filename)
    current_sources = []
    voltage_sources = []
    nodes = set()
    resistors = []
    inside_circuit = False
    node_dict = {}
    

    for line in sfp:
        line = line.strip().split()

        if not line:
            continue

        if line[0] == ".circuit":
            inside_circuit = True
            continue

        if inside_circuit and line[0] != ".end":
            if line[0][0] == 'V':
                voltage_sources.append(line[1:])
                nodes.add(line[1])
                nodes.add(line[2])

            elif line[0][0] == 'I':
                current_sources.append(line[1:])
                nodes.add(line[1])
                nodes.add(line[2])

            elif line[0][0] == 'R':
                resistors.append(line[1:])
                nodes.add(line[1])
                nodes.add(line[2])

    nodes.discard("GND")

    no_of_nodes = len(nodes)
    no_of_sources = len(voltage_sources)

    size = no_of_nodes + no_of_sources

    G = np.zeros((size,size))
    I = np.zeros((size,1))

        
    node_dict["GND"] = 0
        
    for i,node in enumerate(nodes):
        node_dict[node] = i+1

    for resistor in resistors:
        node1,node2,resistance = resistor
        resistance = float(resistance)

        i = node_dict[node1] - 1
        j = node_dict[node2] - 1

        
        if i == -1 :
            G[j][j] += 1/resistance
        elif j == -1 :
            G[i][i] += 1/resistance
        else:
            G[i][i] += 1/resistance
            G[j][j] += 1/resistance
            G[i][j] -= 1/resistance
            G[j][i] -= 1/resistance

    for k,source in enumerate(voltage_sources):
        node1,node2,source_info  = source[0],source[1],source[2:]
        i = node_dict[node1] - 1
        j = node_dict[node2] - 1

        
        if source_info[0] == "dc":
            value = float(source_info[1])
        else:
            value = float(source_info[0])
        row = no_of_nodes + k

        
        if j == -1:
            G[row][i] = 1
            G[i][row] = 1
        elif i == -1:
            G[row][j] = -1
            G[j][row] = 1
        else:
            G[row][j] = 1
            G[row][i] = -1
            G[i][j] = 1 

        I[row] = value
        

    for current_source in current_sources:
        node1,node2,current = current_source
        current = float(current)

        i = node_dict[node1] - 1
        j = node_dict[node2] - 1

        if i == -1:
            I[j][0] += current
        elif j == -1:
            I[i][0] -= current
        else:
            I[i][0] -= current
            I[j][0] += current

    x = np.linalg.solve(G,I)

    

    return node_dict,x
 
