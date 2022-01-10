from enum import Enum 

class FileSystem:

    def __init__(self):
        self.root = DirNode("/")
        
    def splitPath(self, path:str) -> List[str]:
        if path == "/":
            return [""]
        return path.split("/")
                    

    def ls(self, path: str) -> List[str]:
        pathList = self.splitPath(path)
        node = self.root
        for i in range(1, len(pathList)):
            p = pathList[i]
            node = node.subDirectory[p]
        if isinstance(node, DirNode):
            dirs = list(node.subDirectory.keys())
            dirs.sort()
            return dirs
        else:
            # print(node.name)
            return [node.name]
          

    def mkdir(self, path: str) -> None:
        pathList = self.splitPath(path)
        node = self.root
        for i in range(1, len(pathList)):
            p = pathList[i]
            if p not in node.subDirectory:
                subNode = DirNode(p)
                node.subDirectory[p] = subNode
            node = node.subDirectory[p]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        pathList = self.splitPath(filePath)
        node = self.root
        for i in range(1, len(pathList) - 1):
            p = pathList[i]
            node = node.subDirectory[p]
        p = pathList[-1]
        if p not in node.subDirectory:
            subNode = FileNode(p, content)
            node.subDirectory[p] = subNode
        else:
            node = node.subDirectory[p].append(content)
        
    
    def readContentFromFile(self, filePath: str) -> str:
        pathList = self.splitPath(filePath)
        node = self.root
        for i in range(1, len(pathList)):
            p = pathList[i]
            node = node.subDirectory[p]
        return node.content

    
class FileNodeType(Enum):
    Directory = 1
    File = 2
    #Link = 3

class INode:
    def __init__(self, name, nodeType):
        self.name = name
        self.nodeType = nodeType

class FileNode(INode):
    def __init__(self, name, content):
        INode.__init__(self, name, FileNodeType.File)
        self.content = content
    
    def append(self, content):
        self.content += content

class DirNode(INode):
    def __init__(self, name):
        INode.__init__(self, name, FileNodeType.Directory)
        self.subDirectory = {}
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)