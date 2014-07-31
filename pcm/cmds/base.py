class BaseCmd(object):
    """Docstring for Search """

    name = 'wonk'
    help_text = ("wonk it")
    aliases = []

    def __init__(self, sub_parser):
        """todo: to be defined

        :param sub_parser: arg description
        :type sub_parser: type description
        """
        self._sub_parser = sub_parser
        self._cmd_parser = self._sub_parser.add_parser(
            self.name,
            help=self.help_text,
            aliases=self.aliases,
        )
    #__init__()

    def build(self):
        self._cmd_parser.set_defaults(func=self.exec)
        return self._cmd_parser
    #build()

    def exec(self, args):
        print(args)
    #exec()
# BaseCmd
