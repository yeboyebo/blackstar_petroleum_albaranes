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

    @helpers.decoradores.accion(tipo="O")
    def nuevacargapedidos(self):
        return form.iface.nuevacargapedidos(self)

    @helpers.decoradores.accion(aqparam=["cursor"])
    def cerrarcargapedidos(self, cursor):
        return form.iface.cerrarcargapedidos(self, cursor)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def nuevalineacargapedidos(self, oParam):
        return form.iface.nuevalineacargapedidos(self, oParam)

    @helpers.decoradores.accion()
    def dameTemplateCargaPedidoscli(self):
        return form.iface.dameTemplateCargaPedidoscli(self)

    @helpers.decoradores.accion()
    def dameCargaAgente(self):
        return form.iface.dameCargaAgente(self)

    def field_colorRow(cursor):
        return form.iface.field_colorRow(cursor)


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
