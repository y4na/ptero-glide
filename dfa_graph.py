# as simple dfa graph showing the states and inputs

from graphviz import Digraph

dot = Digraph()

dot.node('q0')
dot.node('q1')
dot.node('q2')
dot.node('q3')
dot.node('q4')
dot.node('q5')

dot.edge('q0', 'q1', 'Start Game')
dot.edge('q1', 'q2', 'Jump Pressed')
dot.edge('q2', 'q1', 'Landed')
dot.edge('q1', 'q3', 'Collision')
dot.edge('q3', 'q0', 'Restart Game')
dot.edge('q1', 'q4', 'Score >= 300')
dot.edge('q4', 'q5', 'Score >= 600')
dot.edge('q1', 'q1', 'Score Increment / Speed Change')

dot.render('dfa_graph', format='png', cleanup=True)
