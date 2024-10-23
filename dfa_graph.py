from graphviz import Digraph

dot = Digraph()

dot.node('start', shape='point')
dot.node('q0', label='q0')
dot.node('q1', label='q1')
dot.node('q2', label='q2')
dot.node('q3', label='q3')
dot.node('q4', label='q4')
dot.node('q5', label='q5', shape='doublecircle')

dot.edge('start', 'q0', label='Start')
dot.edge('q0', 'q1', 'Start Game')
dot.edge('q1', 'q2', 'Jump Pressed')
dot.edge('q2', 'q1', 'Landed')
dot.edge('q1', 'q3', 'Collision')
dot.edge('q3', 'q0', 'Restart Game')
dot.edge('q1', 'q4', 'Score >= 300')
dot.edge('q4', 'q5', 'Score >= 600')
dot.edge('q1', 'q1', 'Score Increment, Speed Change')

dot.node('legend', label='Legend:\nq0: Initial State\nq1: Game Running\nq2: Jump Action\nq3: Collision Detected\nq4: Score >= 300\nq5: Score >= 600 (End)', shape='box', fontsize='10')

dot.render('dfa_graph', format='png', cleanup=True)
