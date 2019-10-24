# @class_declaration interna_bi_lineascargapedidoscli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_bi_lineascargapedidoscli(modelos.mtd_bi_lineascargapedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration blackstar_petroleum_albaranes_bi_lineascargapedidoscli #
class blackstar_petroleum_albaranes_bi_lineascargapedidoscli(interna_bi_lineascargapedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration bi_lineascargapedidoscli #
class bi_lineascargapedidoscli(blackstar_petroleum_albaranes_bi_lineascargapedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.bi_lineascargapedidoscli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
