# detailed graph/flow of the states

from graphviz import Digraph

dot = Digraph()

dot.node('A', 'Menu')
dot.node('B', 'Playing')
dot.node('C', 'Jumping')
dot.node('D', 'Game Over')
dot.node('E', 'Background 1')  
dot.node('F', 'Background 2')  
dot.node('G', 'Background 3')  
dot.node('H', 'Speed Normal') 
dot.node('I', 'Speed Fast')   
dot.node('J', 'Speed Fastest')

dot.edge('A', 'B', 'Start Game')
dot.edge('B', 'C', 'Jump Pressed')
dot.edge('C', 'B', 'Landed')
dot.edge('B', 'D', 'Collision')
dot.edge('D', 'A', 'Restart Game')

dot.edge('B', 'E', 'Score < 300')
dot.edge('B', 'F', 'Score >= 300')
dot.edge('F', 'G', 'Score >= 600')
dot.edge('G', 'F', 'Score < 600')  

dot.edge('B', 'H', 'Score < 100')  
dot.edge('H', 'I', 'Score >= 100')  
dot.edge('I', 'J', 'Score >= 200')  
dot.edge('J', 'I', 'Score < 200') 

dot.render('graph', format='png', cleanup=True) 
