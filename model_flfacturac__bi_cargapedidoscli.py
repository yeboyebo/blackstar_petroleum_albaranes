# @class_declaration interna_bi_cargapedidoscli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_bi_cargapedidoscli(modelos.mtd_bi_cargapedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration blackstar_petroleum_albaranes_bi_cargapedidoscli #
class blackstar_petroleum_albaranes_bi_cargapedidoscli(interna_bi_cargapedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration bi_cargapedidoscli #
class bi_cargapedidoscli(blackstar_petroleum_albaranes_bi_cargapedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.bi_cargapedidoscli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
