# CSES - Tree Matching

MIN_NODES = 1
MAX_NODES = 200000


def matching(tree: list):
    result = 0
    for node in tree:
        max_matching = 1
        used_nodes = [node["first"], node["second"]]
        
        for other in tree:
            if other["first"] not in used_nodes and other["second"] not in used_nodes:
                max_matching += 1
                used_nodes.append(other["first"])
                used_nodes.append(other["second"])
        
        if max_matching > result:
            result = max_matching

    return result


def main():
    nodes = int(input("Hány elemű a fa: "))
    assert MIN_NODES <= nodes <= MAX_NODES
    
    edges = []
    print("Fa élei:")
    for i in range(0,nodes):
        row = input()
        if row != "":
            row_lst = row.strip().split(sep=" ")
        
            assert MIN_NODES <= int(row_lst[0]) <= MAX_NODES and MIN_NODES <= int(row_lst[1]) <= MAX_NODES
            
            if int(row_lst[1]) < int(row_lst[0]):
                tmp = row_lst[1]
                row_lst[1] = row_lst[0]
                row_lst[0] = tmp

            edge = {"first": int(row_lst[0]), "second": int(row_lst[1])}
            if edge not in edges:
                edges.append(edge)
        
    print(matching(edges))


if __name__ == "__main__":
    main()