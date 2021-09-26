from xml.etree import ElementTree
from graphviz import Digraph
import re

def label_font(l):
    fs=13
    if len(l)>=6: 
        fs=10
    return fs

def tree2graph(tree, dg, cl):
    if tree.tag=='data':
        for sub in tree:
            tree2graph(sub, dg, cl)
            cl+=1
        for t in range(cl):
            dg.edge("source"+str(t),"sink"+str(t),style="dotted", weight="1000", color="#808080")
            if t>=1:
                dg.edge("sink"+str(t-1),"source"+str(t),style="dotted", weight="1000", color="#808080")
        for sub in tree.iter(tag='function'):
            n=sub.find('id').text
            for e in sub.iter():
                if e.tag=='i' or e.tag=='p' or e.tag=='r' or e.tag=='c' or e.tag=='t':
                    dg.edge(e.text, n, headlabel=e.tag, labeldistance="2.0", color="#808080")
    elif tree.tag=='cluster':
        with dg.subgraph(name="cluster"+str(cl)) as sg:
            for sub in tree:
                tree2graph(sub, sg, cl)
    elif tree.tag=='rank':
        with dg.subgraph() as sg:
            sg.graph_attr['rank']=tree.text.strip()   #source,sink,same
            sg.node(tree.text.strip()+str(cl),"phase"+str(cl), style="dotted") 
            for sub in tree:
                tree2graph(sub, sg, cl)
    elif tree.tag=='function':
        n=tree.find('id').text
        l=tree.find('label').text
        try:
            color=tree.find('color').text
        except AttributeError:
            color="#ccddff"
        l2=re.sub("(.{5})",'\\1\n', n+l)  
        fs=label_font(l)     
        dg.node(n, l2, height='0.5', width='1', fontsize=str(fs), shape="box", style="rounded,filled", color='808080', fillcolor=color) 

XMLFILE = "fram3.xml"
tree = ElementTree.parse(XMLFILE)  # ファイルから読み込み
root = tree.getroot()

dg = Digraph(format='png', engine='dot')
dg.attr(rankdir='LR', concentrate='true')

tree2graph(root, dg, 0)

dg.render('./img/dgraph5') 
