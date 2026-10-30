# Deep Learning — Comprehensive Study Notes

**Audience:** Python learners building a practical portfolio. **Data:** all records are synthetic; results are illustrative.

## Learning objectives

### 1. Neurons, weights, biases and activations

### 2. Feedforward networks and backpropagation

### 3. Training, validation and test sets

### 4. Feature scaling and overfitting

### 5. Early stopping and regularization

### 6. TensorFlow/Keras Sequential API

### 7. Loss curves and model evaluation

### 8. Ethical considerations and reproducibility

A neuron computes an affine transformation followed by an activation. ReLU is common in hidden layers; linear output suits regression.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Forward propagation produces predictions; gradient descent adjusts weights using derivatives of loss via backpropagation.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Training data fits weights, validation data guides model selection, and a held-out test set estimates generalization.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Standardize continuous features using statistics from training only. Overfitting appears when training loss improves while validation loss worsens.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Early stopping monitors validation loss and restores the best weights. L2 penalties and dropout can help, but do not guarantee generalization.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Keras Sequential stacks Dense layers. Compile with optimizer, loss, and metrics; fit with validation_data and EarlyStopping.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Compare to a mean or linear-regression baseline. Report MAE and RMSE on held-out examples and plot training/validation loss.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

Set random seeds and document package versions. Synthetic data and small samples do not establish production readiness.

**Check yourself:** Explain when this idea is useful, a common mistake, and how you would test it.

## Workflow checklist
1. Define the question and the unit of analysis.
2. Inspect schema, missingness, duplicates, and target leakage.
3. Build a simple baseline and keep an independent test set where relevant.
4. Create interpretable charts and explain uncertainty.
5. Record assumptions, limitations, and next actions.

## Suggested references
- pandas documentation: https://pandas.pydata.org/docs/
- scikit-learn user guide: https://scikit-learn.org/stable/user_guide.html
- Matplotlib documentation: https://matplotlib.org/stable/
