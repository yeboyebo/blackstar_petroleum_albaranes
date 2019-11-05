# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration blackstar_petroleum_albaranes_albaranes #
from YBLEGACY.constantes import *


class blackstar_petroleum_albaranes(interna):

    def blackstar_petroleum_albaranes_getDesc(self):
        return None

    def blackstar_petroleum_albaranes_initValidation(self, name, data=None):
        response = True
        # if name == "cargapedidos":
        #     print(qsatype.FLUtil.nameUser())
        #     print(data['DATA']['codagente'])
        return response

    def blackstar_petroleum_albaranes_iniciaValoresLabel(self, model=None, template=None, cursor=None):
        labels = {}
        usr = qsatype.FLUtil.nameUser()
        agente = agentes.objects.filter(dnicif__exact=usr)
        apellidos = agente[0].apellidos
        nombre = agente[0].nombre + " " + apellidos
        labels["nombreAgente"] = nombre
        return labels

    def blackstar_petroleum_albaranes_bChLabel(self, fN=None, cursor=None):
        labels = {}
        return labels

    def blackstar_petroleum_albaranes_getFilters(self, model, name, template=None):
        filters = []
        if name == 'pedidosagente':
            aEjercicios = []
            codejercicios = qsatype.FactoriaModulos.get('flfactppal').iface.dameEjerciciosEmpresa(6)
            codejercicios = codejercicios.replace("'", "")
            aEjercicios = codejercicios.split(",")
            filters = [{'criterio': 'codejercicio__in', 'valor': aEjercicios}]
            usr = qsatype.FLUtil.nameUser()
            agente = agentes.objects.filter(dnicif__exact=usr)
            filters.append({'criterio': 'codagente__in', 'valor': [agente[0].codagente]})
        return filters

    def blackstar_petroleum_albaranes_getForeignFields(self, model, template=None):
        fields = []
        if template == 'mastercargapedidos':
            return [
                {'verbose_name': 'rowColor', 'func': 'field_colorRow'}
            ]
        return fields

    def blackstar_petroleum_albaranes_field_colorRow(self, model):
        if model.estado == "Cerrada":
            return "cSuccess"
        else:
            return None
            print(cantidad, cantmontada)
        return None

    def blackstar_petroleum_albaranes_nuevacargapedidos(self, model):
        print("nueva carga de pedidos")
        usr = qsatype.FLUtil.nameUser()
        agente = agentes.objects.filter(dnicif__exact=usr)
        codagente = agente[0].codagente
        curLCP = qsatype.FLSqlCursor(u"bi_cargapedidoscli")
        curLCP.setModeAccess(curLCP.Insert)
        curLCP.refreshBuffer()
        curLCP.setValueBuffer("estado", "Abierta")
        curLCP.setValueBuffer("codagente", codagente)
        curLCP.setValueBuffer("fechaalta", str(qsatype.Date())[:10])

        if not curLCP.commitBuffer():
            return False
        return True

    def blackstar_petroleum_albaranes_nuevalineacargapedidos(self, model, oParam):
        if "codalmacen" not in oParam and "codcliente" not in oParam:
            response = {}
            response['status'] = -1
            response['data'] = {}
            response['params'] = [
                {
                    "tipo": 56,
                    "componente": "YBFieldDB",
                    "prefix": "otros",
                    "rel": "almacenes",
                    "aplic": "lineascargapedidos",
                    "key": "codalmacen",
                    "desc": "nombre",
                    "auto_name": "Almacén",
                    "null": True
                },
                {
                    "tipo": 56,
                    "componente": "YBFieldDB",
                    "prefix": "otros",
                    "rel": "clientes",
                    "aplic": "lineascargapedidos",
                    "key": "codcliente",
                    "desc": "nombre",
                    "auto_name": "Instalación",
                    "null": True
                }
            ]
            return response
        else:
            print("nueva linea carga de pedidos", oParam)
            curLCP = qsatype.FLSqlCursor(u"bi_lineascargapedidoscli")
            curLCP.setModeAccess(curLCP.Insert)
            curLCP.refreshBuffer()
            curLCP.setValueBuffer("idcargapedidos", model.idcargapedidos)
            curLCP.setValueBuffer("codalmacen", oParam['codalmacen'])
            curLCP.setValueBuffer("codcliente", oParam['codcliente'])

            if not curLCP.commitBuffer():
                return False
        return True

    def blackstar_petroleum_albaranes_dameTemplateCargaPedidoscli(self, model):
        print("damtetemplatecargapedidoscli")
        return True

    def blackstar_petroleum_albaranes_dameCargaAgente(self, model):
        print("???")
        url = '/agentes/bi_cargapedidoscli/' + str(model.idcargapedidos) + '/cargapedidos'
        return url

    def blackstar_petroleum_albaranes_cerrarcargapedidos(self, model, cursor):
        estado = cursor.valueBuffer("estado")
        if cursor.valueBuffer("estado") == "Abierta":
            estado = "Cerrada"
        elif cursor.valueBuffer("estado") == "Cerrada":
            estado = "Abierta"
        cursor.setValueBuffer("estado", estado)
        if not cursor.commitBuffer():
            return False
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def initValidation(self, name, data=None):
        return self.ctx.blackstar_petroleum_albaranes_initValidation(name, data)

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

    def nuevacargapedidos(self, model):
        return self.ctx.blackstar_petroleum_albaranes_nuevacargapedidos(model)

    def cerrarcargapedidos(self, model, cursor):
        return self.ctx.blackstar_petroleum_albaranes_cerrarcargapedidos(model, cursor)

    def nuevalineacargapedidos(self, model, oParam):
        return self.ctx.blackstar_petroleum_albaranes_nuevalineacargapedidos(model, oParam)

    def dameTemplateCargaPedidoscli(self, model):
        return self.ctx.blackstar_petroleum_albaranes_dameTemplateCargaPedidoscli(model)

    def dameCargaAgente(self, model):
        return self.ctx.blackstar_petroleum_albaranes_dameCargaAgente(model)

    def field_colorRow(self, model):
        return self.ctx.blackstar_petroleum_albaranes_field_colorRow(model)


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
