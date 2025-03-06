
import os
#extract basename
def getFileBaseName(fileName):
    file_name = os.path.basename(fileName)
    return file_name

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def remove_redundant_points(vertices, threshold):
    new_vertices = [vertices[0]]  # 保留多边形的第一个点

    for i in range(1, len(vertices)):
        if distance(vertices[i], new_vertices[-1]) > threshold:
            new_vertices.append(vertices[i])

    # 如果新的顶点列表的最后一个点与第一个点距离太近，则删除
    if len(new_vertices) > 1 and distance(new_vertices[-1], new_vertices[0]) < threshold:
        new_vertices.pop()

    return new_vertices
