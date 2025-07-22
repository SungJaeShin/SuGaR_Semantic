import os
import torch
import numpy as np
from sklearn.decomposition import PCA

# Input features shape: (16, H, W)
def feature_to_rgb(features):
    # Reshape features for PCA
    H, W = features.shape[1], features.shape[2]
    features_reshaped = features.view(features.shape[0], -1).T

    # Apply PCA and get the first 3 components
    pca = PCA(n_components=3)
    # pca_result = pca.fit_transform(features_reshaped.cpu().numpy())
    pca_result = pca.fit_transform(features_reshaped.detach().cpu().numpy())

    # Reshape back to (H, W, 3)
    pca_result = pca_result.reshape(H, W, 3)

    # Normalize to [0, 255]
    pca_normalized = 255 * (pca_result - pca_result.min()) / (pca_result.max() - pca_result.min())

    rgb_array = pca_normalized.astype('uint8')

    return rgb_array
