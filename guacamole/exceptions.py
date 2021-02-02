"""
The underlying work for this code is published under the MIT License (MIT)
(https://pypi.org/project/pyguacamole/)
"""


class GuacamoleError(Exception):
    def __init__(self, message):
        super(GuacamoleError, self).__init__(
            'Guacamole Protocol Error. %s' % message
        )


class InvalidInstruction(Exception):
    def __init__(self, message):
        super(InvalidInstruction, self).__init__(
            'Invalid Guacamole Instruction! %s' % message
        )
