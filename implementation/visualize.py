import numpy as np
from sklearn.manifold import TSNE
import plotly.graph_objects as go

def visualize_vectors_2d(vectors, documents, doc_types, colors):
    tsne = TSNE(n_components=2, random_state=42)
    reduced = tsne.fit_transform(vectors)
    fig = go.Figure(data=[go.Scatter(
        x=reduced[:, 0],
        y=reduced[:, 1],
        mode='markers',
        marker=dict(size=5, color=colors, opacity=0.8),
        text=[f"Type: {t}<br>Text: {d[:100]}..." for t, d in zip(doc_types, documents)],
        hoverinfo='text'
    )])
    fig.update_layout(title='2D Chroma Vector Store Visualization', width=800, height=600)
    fig.show()

def visualize_vectors_3d(vectors, documents, doc_types, colors):
    tsne = TSNE(n_components=3, random_state=42)
    reduced = tsne.fit_transform(vectors)
    fig = go.Figure(data=[go.Scatter3d(
        x=reduced[:, 0],
        y=reduced[:, 1],
        z=reduced[:, 2],
        mode='markers',
        marker=dict(size=5, color=colors, opacity=0.8),
        text=[f"Type: {t}<br>Text: {d[:100]}..." for t, d in zip(doc_types, documents)],
        hoverinfo='text'
    )])
    fig.update_layout(title='3D Chroma Vector Store Visualization', width=900, height=700)
    fig.show()
