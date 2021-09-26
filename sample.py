
import pygraphviz as pgv
import networkx as nx

#普通にnetworkxのグラフを作成
h = nx.newman_watts_strogatz_graph(10,3,0.4)
h = nx.star_graph(6)


#これをagraphクラス（PyGraphviz）に変換
g = nx.nx_agraph.to_agraph(h)

#file.pdfという名前で出力，レイアウトはcircoを使う
g.draw('file.png',prog='dot')


