# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration blackstar_petroleum_albaranes #
from YBLEGACY.constantes import *


class blackstar_petroleum_albaranes(interna):

    def blackstar_petroleum_albaranes_initValidation(self, name, data=None):
        response = True
        return response

    def blackstar_petroleum_albaranes_iniciaValoresLabel(self, model=None, template=None, cursor=None):
        labels = {}
        return labels

    def blackstar_petroleum_albaranes_bChLabel(self, fN=None, cursor=None):
        labels = {}
        return labels

    def blackstar_petroleum_albaranes_getFilters(self, model, name, template=None):
        print("getfilter", name)
        filters = []
        return filters

    def blackstar_petroleum_albaranes_getForeignFields(self, model, template=None):
        fields = []
        if template == 'cargapedidos':
            return [
                {'verbose_name': 'instalacion', 'func': 'field_instalacion'},
                {'verbose_name': 'cliente', 'func': 'field_cliente'}
            ]
        return fields

    def blackstar_petroleum_albaranes_field_instalacion(self, model):
        return model.codalmacen

    def blackstar_petroleum_albaranes_field_cliente(self, model):
        return model.codcliente.nombre

    def blackstar_petroleum_albaranes_getDesc(self):
        desc = None
        return desc

    def blackstar_petroleum_albaranes_editarLitros(self, model, oParam, cursorLinea):
        for p in oParam:
            tipo = p
            val = oParam[p]
        # TODO ver si el pedido esta abierto.
        cursorLinea.setValueBuffer(tipo, val)
        qsatype.FactoriaModulos.get('formRecordbi_lineascargapedidoscli').iface.bChCursor(tipo, cursorLinea)
        if not cursorLinea.commitBuffer():
            return False
        return True

    def blackstar_petroleum_albaranes_editarOrdendeCarga(self, model, oParam, cursorLinea):
        print("editarordencarga", oParam)
        cursorLinea.setValueBuffer("ordendecarga", oParam["ordendecarga"])
        if not cursorLinea.commitBuffer():
            return False
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def initValidation(self, name, data=None):
        return self.ctx.blackstar_petroleum_albaranes_initValidation(name, data=None)

    def iniciaValoresLabel(self, model=None, template=None, cursor=None):
        return self.ctx.blackstar_petroleum_albaranes_iniciaValoresLabel(model, template, cursor)

    def bChLabel(self, fN=None, cursor=None):
        return self.ctx.blackstar_petroleum_albaranes_bChLabel(fN, cursor)

    def getFilters(self, model, name, template=None):
        return self.ctx.blackstar_petroleum_albaranes_getFilters(model, name, template)

    def getForeignFields(self, model, template=None):
        return self.ctx.blackstar_petroleum_albaranes_getForeignFields(model, template)

    def getDesc(self):
        return self.ctx.blackstar_petroleum_albaranes_getDesc()

    def editarLitros(self, model, oParam, cursor):
        return self.ctx.blackstar_petroleum_albaranes_editarLitros(model, oParam, cursor)

    def editarOrdendeCarga(self, model, oParam, cursor):
        return self.ctx.blackstar_petroleum_albaranes_editarOrdendeCarga(model, oParam, cursor)

    def field_instalacion(self, model):
        return self.ctx.blackstar_petroleum_albaranes_field_instalacion(model)

    def field_cliente(self, model):
        return self.ctx.blackstar_petroleum_albaranes_field_cliente(model)


# @class_declaration head #
class head(blackstar_petroleum_albaranes):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
