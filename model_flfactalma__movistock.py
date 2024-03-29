# @class_declaration interna_movistock #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_movistock(modelos.mtd_movistock, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration blackstar_petroleum_albaranes_movistock #
class blackstar_petroleum_albaranes_movistock(interna_movistock, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration movistock #
class movistock(blackstar_petroleum_albaranes_movistock, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.movistock_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
