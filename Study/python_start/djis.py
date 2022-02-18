# you need to study decorator! 
import queue

graph = {
    's': {'t': 10, 'y': 5},
    'y': {'t': 3, 'x': 9, 'z': 2},
    't': {'y': 2, 'x': 1},
    'x': {'z': 4},
    'z': {'s': 7, 'x': 6}
}

st = queue()
st.Queue()