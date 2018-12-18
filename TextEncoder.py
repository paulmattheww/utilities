from sklearn.decomposition import PCA
class TextEncoder(BaseEstimator, TransformerMixin):
    """Uses a defined encoder model to transform text data
    into a latent space to represent its features in a more
    dense format.
    """
    def __init__(self, encoder_model):
        self.encoder_model = encoder_model
        
    def preprocess_encodings(self, X, num_words=5000, maxlen=5000):
        tokenizer = Tokenizer(num_words=num_words)
        tokenizer.fit_on_texts(X)
        txt = tokenizer.texts_to_sequences(X)
        vocab_size = len(tokenizer.word_index) + 1  # Adding 1 because of reserved 0 index
        txt = pad_sequences(txt, padding='post', maxlen=maxlen)
        return txt
        
    def fit(self, X, y=None):
        """interface conforming for fit_transform"""
        return self
    
    def transform(self, X, use_pca=False):
        print('ENCODING FEATURES ...')
        X_new = self.preprocess_encodings(X)
        if use_pca:
            return PCA(n_components=10).fit_transform(self.encoder_model.predict(X_new))
        else:
            return self.encoder_model.predict(X_new)

