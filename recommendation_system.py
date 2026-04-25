#Recommendation System
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

data = np.array([[5,0,0],[4,0,0],[0,5,5]])

sim = cosine_similarity(data)

print(sim)
