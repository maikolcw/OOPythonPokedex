class Request:
    """
    This class holds the results from arg parse from terminal.
    """
    def __init__(self, **kwargs):
        """
        Mode holds the search mode term, input type is either 'file' or 'console', input value is the text file name or
        parameter used for the url query, expanded is boolean, and output type is default 'console' or text file name.
        :param kwargs:
        """
        self._mode = kwargs["mode"]
        self._input_type = kwargs["input_type"]
        self._input_value = kwargs["input_value"]
        self._expanded = kwargs["expanded"]
        self._output_type = kwargs["output_type"]

    def get_mode(self):
        """
        Retrieves the mode attribute
        :return: str
        """
        return self._mode

    def get_input_type(self):
        """
        Retrieves the input type attribute
        :return: str
        """
        return self._input_type

    def get_input_value(self):
        """
        Retrieves the input value
        :return: str
        """
        return self._input_value

    def get_expanded(self):
        """
        Retrieves expanded boolean
        :return: boolean
        """
        return self._expanded

    def get_output_type(self):
        """
        Retrieves output type
        :return: str
        """
        return self._output_type

    def set_input_type(self, input_type):
        """
        Sets input type
        :param input_type: str
        """
        self._input_type = input_type

    def set_input_value(self, input_value):
        """
        Sets input value
        :param input_value: str
        """
        self._input_value = input_value

    def set_expanded(self, expanded):
        """
        Sets boolean
        :param expanded: boolean
        """
        self._expanded = expanded

    def set_output_type(self, output_type):
        """
        Sets output type
        :param output_type: str
        """
        self._output_type = output_type

    def __str__(self):
        """
        :return: a string representation of a request object
        """
        return f"Mode: {self._mode}\n" \
               f"Input Type: {self._input_type}\n" \
               f"Input Value: {self._input_value}\n" \
               f"Expanded: {self._expanded}\n" \
               f"Output Type: {self._output_type}\n"
