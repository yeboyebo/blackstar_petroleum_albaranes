
# @class_declaration blackstar_petroleum_albaranes #
from models.flfactppal.agentes import agentes


class blackstar_petroleum_albaranes(flfacturac):

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
        if not agente:
            return labels
        apellidos = agente[0].apellidos
        nombre = agente[0].nombre + " " + apellidos
        labels["nombreAgente"] = nombre
        return labels

    def blackstar_petroleum_albaranes_bChLabel(self, fN=None, cursor=None):
        labels = {}
        return labels

    def blackstar_petroleum_albaranes_getFilters(self, model, name, template=None):
        filters = []
        if name == 'albaranesagente':
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
        if not model.ptefactura:
            return "cSuccess"
        else:
            return None
        return None

    def blackstar_petroleum_albaranes_nuevoalbaran(self, model, oParam):
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

    def blackstar_petroleum_albaranes_damenuevoalbaran(self, model):
        usr = qsatype.FLUtil.nameUser()
        codagente = qsatype.FLUtil.sqlSelect(u"agentes", u"codagente", ustr(u"dnicif = '", usr, "'"))
        url = '/agentes/albaranescli/newRecord?p_codagente=' + codagente
        return url

    def blackstar_petroleum_albaranes_nuevalineaalbaran(self, model, oParam, cursor):
        print(oParam)
        print(cursor.valueBuffer("idalbaran"))
        if not cursor.valueBuffer("ptefactura"):
            resul = {}
            resul['status'] = -3
            resul['msg'] = "Albaran facturado"
            return resul

        _cFL = qsatype.FactoriaModulos.get('formRecordlineasalbaranescli').iface.pub_commonCalculateField
        descripcion = qsatype.FLUtil.sqlSelect(u"articulos", u"descripcion", u"referencia = '{}'".format(oParam['codarticulo']))
        curL = qsatype.FLSqlCursor(u"lineasalbaranescli")
        curL.setModeAccess(curL.Insert)
        curL.refreshBuffer()
        curL.setValueBuffer(u"idalbaran", cursor.valueBuffer("idalbaran"))
        curL.setValueBuffer(u"referencia", oParam['codarticulo'])
        curL.setValueBuffer(u"descripcion", descripcion)
        curL.setValueBuffer(u"cantidad", 0)
        curL.setValueBuffer(u"pvpunitario", 0)
        curL.setValueBuffer(u"pvpsindto", _cFL(u"pvpsindto", curL))
        curL.setValueBuffer(u"pvptotal", _cFL(u"pvptotal", curL))
        curL.setValueBuffer(u"codimpuesto", _cFL(u"codimpuesto", curL))
        curL.setValueBuffer(u"iva", _cFL(u"iva", curL))
        curL.setValueBuffer(u"recargo", _cFL(u"recargo", curL))
        if not curL.commitBuffer():
            return False
        return True

    def blackstar_petroleum_albaranes_iniciaValoresCursor(self, cursor=None):
        _i = self.iface
        qsatype.FactoriaModulos.get('formRecordpedidoscli').iface.iniciaValoresCursor(cursor)
        hoy = qsatype.Date()
        codejercicio = _i.dameEjercicioActualBlackstar(hoy)
        cursor.setValueBuffer("codejercicio", codejercicio)
        # De momento no se filtran los clientes por agente al crear albaran.
        # codagente = qsatype.FLUtil.sqlSelect(u"agentes", u"codagente", u"dnicif = '{}'".format(qsatype.FLUtil.nameUser()))
        # if codagente:
        #     cursor.setValueBuffer("codagente", codagente)
        return True

    def blackstar_petroleum_albaranes_dameEjercicioActualBlackstar(self, fecha):
        codejercicio = ""
        codejercicio = qsatype.FLUtil.sqlSelect(u"ejercicios", u"codejercicio", u"fechainicio <= '{0}' AND fechafin >= '{0}' AND idempresa = 6 AND estado = 'ABIERTO'".format(fecha))
        return codejercicio

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

    def nuevoalbaran(self, model, oParam):
        return self.ctx.blackstar_petroleum_albaranes_nuevoalbaran(model, oParam)

    def field_colorRow(self, model):
        return self.ctx.blackstar_petroleum_albaranes_field_colorRow(model)

    def damenuevoalbaran(self, model):
        return self.ctx.blackstar_petroleum_albaranes_damenuevoalbaran(model)

    def nuevalineaalbaran(self, model, oParam, cursor):
        return self.ctx.blackstar_petroleum_albaranes_nuevalineaalbaran(model, oParam, cursor)

    def iniciaValoresCursor(self, cursor=None):
        return self.ctx.blackstar_petroleum_albaranes_iniciaValoresCursor(cursor)

    def dameEjercicioActualBlackstar(self, fecha):
        return self.ctx.blackstar_petroleum_albaranes_dameEjercicioActualBlackstar(fecha)

