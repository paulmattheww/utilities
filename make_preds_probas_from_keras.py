def make_preds_probas_from_keras(model, X_val, y_val, cutoff, n_classes=3):
    '''Analyzes the predictions from a Keras model object
    for a classification model by reviewing the probabilities of the
    predicted labels.
    
    ARGS: model, X_val, y_val, cutoff
    KWARGS: n_classes
    '''
    class_cols = np.arange(0, n_classes)
    pred_df = pd.DataFrame(model.predict(X_val), columns=class_cols)
    pred_df['label'] = y_val.values
    pred_df['pred'] = pred_df[class_cols].idxmax(axis=1)
    pred_df['top_proba'] = pred_df[class_cols].max(axis=1)
    pred_df['top_proba_bin'] = pd.cut(pred_df.top_proba, bins=20)
    pred_df['is_correct'] = pred_df.label == pred_df.pred
    pred_df['top_proba_>_sum_others'] = pred_df['top_proba'] > (pred_df[class_cols].sum(axis=1) - pred_df['top_proba'])
    pred_df['sum_probas'] = pred_df[class_cols].sum(axis=1)
    pred_df['sum_proba_bin'] = pd.cut(pred_df.top_proba, bins=20)
    pred_df['adj_pred'] = pred_df['pred']
    pred_df.loc[pred_df.sum_probas < cutoff, 'adj_pred'] = 1
    return pred_df
