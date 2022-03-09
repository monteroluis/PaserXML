from xml.dom import minidom, Node
from xml.dom.minidom import Element


def scanNode( node,space=0):
     msg=""
     texto = ""
     if node.nodeType == Node.ELEMENT_NODE:
        msg += node.tagName

     elif node.nodeType == Node.TEXT_NODE:
          texto = ": " + node.data
     print(" "* space * 2, msg, texto)

     if node.hasChildNodes:
         for child in node.childNodes:
             scanNode(child, space + 1)

doc = minidom.parse('Archivos/Concesionario.xml')
print(scanNode(doc))





