class ModelEvaluator:
    def __init__(self, model, X_test, y_test):
        self.model = model
        self.X_test = X_test
        self.y_test = y_test

    def evaluate(self):
        predictions = self.model.predict(self.X_test)
        accuracy = (predictions == self.y_test).mean()
        return accuracy

    def print_results(self):
        accuracy = self.evaluate()
        print(f'\nModel Evaluation Results:\nAccuracy: {accuracy:.2f}\n')
