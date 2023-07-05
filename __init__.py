def WPSClassFactory(iface):
    from .example_algorithm import ExampleProcessingAlgorithm

    iface.registerProvider(ExampleProcessingAlgorithm())
