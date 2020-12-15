
def printToX3D(x3dSceneTree):
    print(x3dSceneTree)
    print(x3dSceneTree.toX3DString())

    for i in range(len(x3dSceneTree.children)):
        printToX3D(x3dSceneTree.children[i])

