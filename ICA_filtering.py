from sklearn.decomposition import FastICA
def apply_ica(eeg_data, num_components):
    ica = FastICA(n_components=num_components)
    components = ica.fit_transform(eeg_data.T).T
    return components
#FAST ICA DECOMPOSITION
