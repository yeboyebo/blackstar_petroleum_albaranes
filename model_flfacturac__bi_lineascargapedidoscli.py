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

    def initValidation(name, data=None):
        return form.iface.initValidation(name, data)

    def iniciaValoresLabel(self, template=None, cursor=None, data=None):
        return form.iface.iniciaValoresLabel(self, template, cursor)

    def bChLabel(fN=None, cursor=None):
        return form.iface.bChLabel(fN, cursor)

    def getFilters(self, name, template=None):
        return form.iface.getFilters(self, name, template)

    def getForeignFields(self, template=None):
        return form.iface.getForeignFields(self, template)

    def getDesc():
        return form.iface.getDesc()

    @helpers.decoradores.accion(aqparam=["oParam", "cursor"])
    def editarLitros(self, oParam, cursor):
        return form.iface.editarLitros(self, oParam, cursor)

    @helpers.decoradores.accion(aqparam=["oParam", "cursor"])
    def editarOrdendeCarga(self, oParam, cursor):
        return form.iface.editarOrdendeCarga(self, oParam, cursor)

    def field_instalacion(cursor):
        return form.iface.field_instalacion(cursor)

    def field_cliente(cursor):
        return form.iface.field_cliente(cursor)


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
