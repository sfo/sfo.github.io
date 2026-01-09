from IPython import get_ipython


class IPY():
    def __init__(self):
        self._ipy = get_ipython()

    def _run(self, func):
        if self._ipy is not None:
            func()

    def magic(self, command: str, argument: str) -> None:
        self._run(lambda : self._ipy.run_line_magic(command, argument))

    def delete(self, varname: str) -> None:
        self._run(lambda : self._ipy.del_var(varname))

    def enable_auto_reload(self) -> None:
        self.magic("load_ext", "autoreload")
        self.magic("autoreload", "2")