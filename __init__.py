class Test:
    def __init__(self):
        pass


def WPSClassFactory(iface):
    # from .example_algorithm import ExampleProcessingAlgorithm
    from .example_provider import ExampleProvider

    iface.registerProvider(ExampleProvider())
    return Test()
