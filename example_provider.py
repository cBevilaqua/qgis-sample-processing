from qgis.core import QgsApplication, QgsProcessingProvider
from .example_algorithm import ExampleProcessingAlgorithm


class ExampleProvider(QgsProcessingProvider):
    def __init__(self):
        super().__init__()

    def id(self):
        # Unique identifier for your provider
        return "custom"

    def getAlgs(self):
        algs = [
            ExampleProcessingAlgorithm(),
        ]
        return algs

    def name(self):
        return "Example Provider"

    def loadAlgorithms(self):
        self.algs = self.getAlgs()
        for a in self.algs:
            self.addAlgorithm(a)
