
def WriteX3DFile(f, X3DNode):
    print(X3DNode, X3DNode.getFlag(), X3DNode.getDepth(), X3DNode.toX3DString())
    if X3DNode.getFlag() == 1:
        writeData = '\t' * X3DNode.getDepth() + '<' + X3DNode.toX3DString() + '/>\n'
    else:
        writeData = '\t' * X3DNode.getDepth() + '<' + X3DNode.toX3DString() + '>\n'
    f.write(writeData)

    for i in range(len(X3DNode.children)):
        WriteX3DFile(f, X3DNode.children[i])

    if X3DNode.getFlag() == 1: return
    else: f.write('\t' * X3DNode.getDepth() + '</' + X3DNode.getNodeName() + '>\n')
