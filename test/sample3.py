from xml.etree import ElementTree
from graphviz import Digraph

def label_trans(l):
    counter=0
    l2=""
    for char in l:
        counter+=1
        l2 += char
        if counter%6==0:
            l2 += "\n"                
    return l2

def label_font(l):
    ll=len(l)
    fs=10
    if ll>=6:
        fs=8
    return fs

XMLFILE = "fram3.xml"

tree = ElementTree.parse(XMLFILE)  # ファイルから読み込み
root = tree.getroot()

dg = Digraph(format='png')
dg.engine = 'dot'
dg.attr(rankdir='LR', overlap='true', splines='true')#, newrank='ture')
dg.attr('node', color='blue')

for sub in root.iter(tag='function'):
    for e in sub.iter():
        if e.tag == 'id':
            n = e.text
        if e.tag =='label':
            l = e.text
            l2=label_trans(l)
            fs=label_font(l)     
    dg.node(n, n+l2, height='0.5', width='1', fontsize=str(fs), shape="box", style="rounded,filled",fillcolor="#ccddff") 
    for e in sub.iter():
        if e.tag=='i' or e.tag=='p' or e.tag=='r' or e.tag=='c' or e.tag=='t':
            dg.edge(e.text, n, headlabel=e.tag, margin="1")

c=0
for sub in root.iter(tag='cluster'):
    with dg.subgraph(name="cluster"+str(c)) as sg:
        for e in sub.iter(tag='id'):
            sg.node(e.text)
        for subsub in sub.iter(tag='rank'):
            rtype=subsub.text.strip()   #source,sink,same
            with sg.subgraph() as ssg:
                ssg.graph_attr['rank']=rtype
                for e in subsub.iter(tag='id'):
                    ssg.node(e.text)
                ssg.node(rtype+str(c)) 
    c+=1

for t in range(c):
    dg.node("source"+str(t),style="dotted")
    dg.node("sink"+str(t),style="dotted")
    dg.edge("source"+str(t),"sink"+str(t),style="dotted", weight="1000")
    if t>=1:
        dg.edge("sink"+str(t-1),"source"+str(t),style="dotted", weight="1000")

dg.render('./test/dgraph5') # テスト




