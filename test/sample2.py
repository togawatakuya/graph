from xml.etree import ElementTree
from graphviz import Digraph

XMLFILE = "fram.xml"

tree = ElementTree.parse(XMLFILE)  # ファイルから読み込み
root = tree.getroot()

dg = Digraph(format='png')
dg.engine = 'neato'
#twopi
dg.attr(overlap='true', splines='true')
#dg.attr('node', shape='hexagon', color='blue')

for sub in root.iter(tag='function'):
    print(sub.tag, sub.text)
    for e in sub.iter():
        print(e.tag, e.text) 
        if e.tag == 'id':
            n = e.text
        if e.tag =='label':
            l = e.text
    """
    dg.node(n, l, shape='hexagon', height='1', width='1') # 1というラベルがついたノードを設定

    
    dg.edge(n+'i', n, len='0.01', arrowhead='none')
    dg.edge(n+'o', n, len='0.01', arrowhead='none')
    dg.edge(n+'p', n, len='0.01', arrowhead='none')
    dg.edge(n+'r', n, len='0.01', arrowhead='none')
    dg.edge(n+'c', n, len='0.01', arrowhead='none')
    dg.edge(n+'t', n, len='0.01', arrowhead='none')

    #dg.node(n, l, shape='hexagon', height='1', width='1')
    dg.node(n+'i','i', height='0.1', width='0.1')
    dg.node(n+'o','o', height='0.1', width='0.1')
    dg.node(n+'p','p', height='0.1', width='0.1')
    dg.node(n+'r','r', height='0.1', width='0.1')
    dg.node(n+'c','c', height='0.1', width='0.1')
    dg.node(n+'t','t', height='0.1', width='0.1')



    """
    with dg.subgraph(name=l) as c:
        #dg.attr(layout='circo')
        #dg.engine = 'neato'
        #c.node_attr.update(style='filled', color='white')
        c.node(n, l, shape='hexagon', height='1', width='1')
       
        c.node(n+'i','i', height='0.1', width='0.1')
        c.node(n+'o','o', height='0.1', width='0.1')
        c.node(n+'p','p', height='0.1', width='0.1')
        c.node(n+'r','r', height='0.1', width='0.1')
        c.node(n+'c','c', height='0.1', width='0.1')
        c.node(n+'t','t', height='0.1', width='0.1')
        
        nel=0.7

        c.edge(n+'i', n, len='0.7', arrowhead='none')
        c.edge(n+'o', n, len='0.7', arrowhead='none')
        c.edge(n+'p', n, len='0.7', arrowhead='none')
        c.edge(n+'r', n, len='0.7', arrowhead='none')
        c.edge(n+'c', n, len='0.7', arrowhead='none')
        c.edge(n+'t', n, len='0.7', arrowhead='none')
       
        c.attr(label='cl'+l)
    
    
    for e in sub.iter():
        if e.tag =='i':
            #dg.edge(e.text+':e', n+":w", len='10')
            dg.edge(e.text+'o', n+"i", minlen='5')
        if e.tag =='p':
            #dg.edge(e.text+':e', n+":se")
            dg.edge(e.text+'o', n+"p")
        if e.tag =='r':
            #dg.edge(e.text+':e', n+":sw")
            dg.edge(e.text+'o', n+"r")
        if e.tag =='c':
            #dg.edge(e.text+':e', n+":ne")
             dg.edge(e.text+'o', n+"c")
        if e.tag =='t':
            #dg.edge(e.text+':e', n+":nw")
             dg.edge(e.text+'o', n+"t")
    print("ここまで\n")

     

dg.render('./test/dgraph5') # テストフォルダにdgraphという名前で保存(拡張子は書かない)