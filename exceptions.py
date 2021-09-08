class PageNotFoundError(Exception):
    def __init__(self, message='The requested page was not found'):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


