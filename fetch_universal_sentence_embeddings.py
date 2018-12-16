import tensorflow as tf
import tensorflow_hub as hub

def fetch_universal_sentence_embeddings(messages, verbose=0):
    """Fetches universal sentence embeddings from Google's
    research paper https://arxiv.org/pdf/1803.11175.pdf.
    
    INPUTS:
    RETURNS:
    """
    module_url = "https://tfhub.dev/google/universal-sentence-encoder/2" #@param ["https://tfhub.dev/google/universal-sentence-encoder/2", "https://tfhub.dev/google/universal-sentence-encoder-large/3"]

    # Import the Universal Sentence Encoder's TF Hub module
    embed = hub.Module(module_url)

    with tf.Session() as session:
        session.run([tf.global_variables_initializer(), tf.tables_initializer()])
        message_embeddings = session.run(embed(messages))
        embeddings = list()
        for i, message_embedding in enumerate(np.array(message_embeddings).tolist()):
            if verbose:
                print("Message: {}".format(messages[i]))
                print("Embedding size: {}".format(len(message_embedding)))
                message_embedding_snippet = ", ".join(
                    (str(x) for x in message_embedding[:3]))
                print("Embedding: [{}, ...]\n".format(message_embedding_snippet))
            embeddings.append(message_embedding)
    return embeddings

embeddings = fetch_universal_sentence_embeddings(txt)
