
# @class_declaration blackstar_petroleum_albaranes #
from YBLEGACY.constantes import *


class blackstar_petroleum_albaranes(flfacturac):

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
        filters = []
        return filters

    def blackstar_petroleum_albaranes_getForeignFields(self, model, template=None):
        fields = []
        if template == 'formRecord':
            return [
                {'verbose_name': 'pvparticulo', 'func': 'field_pvparticulo'},
            ]
        # {'verbose_name': 'cuotaieh', 'func': 'field_cuotaieh'}
        return fields

    def blackstar_petroleum_albaranes_field_pvparticulo(self, model):
        return 0

    def blackstar_petroleum_albaranes_field_cuotaieh(self, model):
        cuotaieh = 0
        curLA = qsatype.FLSqlCursor(u"lineasalbaranescli")
        curLA.select(ustr(u"idlinea = ", model.idlinea))
        if curLA.next():
            curLA.setModeAccess(curLA.Edit)
            curLA.refreshBuffer()
            curAlbaran = qsatype.FLSqlCursor(u"albaranescli")
            curAlbaran.select(ustr(u"idalbaran = ", model.idalbaran))
            if curAlbaran.next():
                curAlbaran.setModeAccess(curAlbaran.Browse)
                curAlbaran.refreshBuffer()
                cuotaieh = self.iface.calcularImpuestos("cuotaieh", curAlbaran, curLA)
        return cuotaieh

    def blackstar_petroleum_albaranes_editarPvpArticulo(self, model, oParam, cursorLinea):
        curAlbaran = qsatype.FLSqlCursor(u"albaranescli")
        curAlbaran.select(ustr(u"idalbaran = ", model.idalbaran))
        if not curAlbaran.next():
            return False
        if not curAlbaran.valueBuffer("ptefactura"):
            resul = {}
            resul['status'] = -3
            resul['msg'] = "Albaran facturado"
            return resul

        cursorLinea.setValueBuffer("pvpunitario", oParam['pvpunitario'])
        qsatype.FactoriaModulos.get('formRecordlineasalbaranescli').iface.bChCursor("pvpunitario", cursorLinea)
        if not cursorLinea.commitBuffer():
            return False
        curAlbaran.setModeAccess(curAlbaran.Edit)
        curAlbaran.refreshBuffer()
        qsatype.FactoriaModulos.get('formRecordalbaranescli').iface.calcularTotalesCursor(curAlbaran)
        codcliente = curAlbaran.valueBuffer("codcliente")
        riesgomax = qsatype.FLUtil.sqlSelect(u"clientes", u"riesgomax", ustr(u"codcliente = '", codcliente, u"'"))
        if riesgomax:
            riesgoalcanzado = qsatype.FLUtil.sqlSelect(u"clientes", u"riesgoalcanzado", ustr(u"codcliente = '", codcliente, u"'"))
            if curAlbaran.valueBuffer("total") + riesgoalcanzado > riesgomax:
                print("operacion invalida")
                response = {}
                response['status'] = 1
                response['msg'] = "Riesgo máximo alcanzado"
                return False
                return response
            if not curAlbaran.commitBuffer():
                return False
            # self.iface.calcularImpuestos("cuotaieh", curAlbaran, cursorLinea)
        return True

    def blackstar_petroleum_albaranes_editarCantidad(self, model, oParam, cursorLinea):
        curAlbaran = qsatype.FLSqlCursor(u"albaranescli")
        curAlbaran.select(ustr(u"idalbaran = ", model.idalbaran))
        if not curAlbaran.next():
            return False
        if not curAlbaran.valueBuffer("ptefactura"):
            resul = {}
            resul['status'] = -3
            resul['msg'] = "Albaran facturado"
            return resul
        cursorLinea.setValueBuffer("cantidad", oParam['cantidad'])
        cursorLinea.setValueBuffer("cuotaieh", self.iface.calcularImpuestos("cuotaieh", curAlbaran, cursorLinea))
        qsatype.FactoriaModulos.get('formRecordlineasalbaranescli').iface.bChCursor("pvpunitario", cursorLinea)
        if not cursorLinea.commitBuffer():
            return False
        curAlbaran.setModeAccess(curAlbaran.Edit)
        curAlbaran.refreshBuffer()
        qsatype.FactoriaModulos.get('formRecordalbaranescli').iface.calcularTotalesCursor(curAlbaran)
        codcliente = curAlbaran.valueBuffer("codcliente")
        riesgomax = qsatype.FLUtil.sqlSelect(u"clientes", u"riesgomax", ustr(u"codcliente = '", codcliente, u"'"))
        if riesgomax:
            riesgoalcanzado = qsatype.FLUtil.sqlSelect(u"clientes", u"riesgoalcanzado", ustr(u"codcliente = '", codcliente, u"'"))
            if curAlbaran.valueBuffer("total") + riesgoalcanzado > riesgomax:
                print("operacion invalida")
                response = {}
                response['status'] = 1
                response['msg'] = "Riesgo máximo alcanzado"
                return False
                return response
            if not curAlbaran.commitBuffer():
                return False

                # self.iface.calcularImpuestos("cuotaieh", curAlbaran, cursorLinea)
                # print(cuotaieh)
        return True

    def blackstar_petroleum_albaranes_calcularImpuestos(self, fN, cursor, cursorLinea):
        _i = self.iface
        s12_when = fN
        s12_do_work, s12_work_done = False, False
        if s12_when == u"iehautonomicounitario":
            s12_do_work, s12_work_done = True, True
        if s12_do_work:
            referencia = cursorLinea.valueBuffer(u"referencia")
            codcliente = cursor.valueBuffer(u"codcliente")
            regsuspensivo = qsatype.FLUtil.sqlSelect(u"clientes", u"regsuspensivo", ustr(u"codcliente = '", codcliente, u"'"))
            idProvincia = cursor.valueBuffer(u"bi_idprovinciaentrega")
            # idProvincia = qsatype.FLUtil.sqlSelect(u"dirclientes", u"idprovincia", ustr(u"codcliente = '", codcliente, u"' AND domfacturacion"))

            if regsuspensivo:
                valor = 0
                s12_do_work = False  # BREAK
            valor = qsatype.FLUtil.sqlSelect(u"bio_impprovincias", u"iehautonomico", ustr(u"idprovincia = ", idProvincia, u" AND referencia = '", referencia, u"'"))
            if not valor or isNaN(valor):
                valor = 0
            s12_do_work = False  # BREAK

        if s12_when == u"iehestatalunitario":
            s12_do_work, s12_work_done = True, True
        if s12_do_work:
            referencia = cursorLinea.valueBuffer(u"referencia")
            codcliente = cursor.valueBuffer(u"codcliente")
            regsuspensivo = qsatype.FLUtil.sqlSelect(u"clientes", u"regsuspensivo", ustr(u"codcliente = '", codcliente, u"'"))
            idProvincia = cursor.valueBuffer(u"bi_idprovinciaentrega")
            # idProvincia = qsatype.FLUtil.sqlSelect(u"dirclientes", u"idprovincia", ustr(u"codcliente = '", codcliente, u"' AND domfacturacion"))

            if regsuspensivo:
                valor = 0
                s12_do_work = False  # BREAK
            valor = qsatype.FLUtil.sqlSelect(u"bio_impprovincias", u"iehestatal", ustr(u"idprovincia = ", idProvincia, u" AND referencia = '", referencia, u"'"))
            if not valor or isNaN(valor):
                valor = 0
            s12_do_work = False  # BREAK

        if s12_when == u"iehautonomico":
            s12_do_work, s12_work_done = True, True
        if s12_do_work:
            cantidad = parseFloat(cursorLinea.valueBuffer(u"cantidad"))
            iehAutonomicoUnitario = parseFloat(_i.calcularImpuestos(u"iehautonomicounitario", cursor, cursorLinea))
            valor = cantidad * iehAutonomicoUnitario
            s12_do_work = False  # BREAK

        if s12_when == u"iehestatal":
            s12_do_work, s12_work_done = True, True
        if s12_do_work:
            cantidad = parseFloat(cursorLinea.valueBuffer(u"cantidad"))
            iehEstatalUnitario = parseFloat(_i.calcularImpuestos(u"iehestatalunitario", cursor, cursorLinea))
            valor = cantidad * iehEstatalUnitario
            s12_do_work = False  # BREAK

        if s12_when == u"cuotaieh":
            s12_do_work, s12_work_done = True, True
        if s12_do_work:
            cantidad = parseFloat(cursorLinea.valueBuffer(u"cantidad"))
            iehEstatal = parseFloat(_i.calcularImpuestos(u"iehestatal", cursor, cursorLinea))
            iehAutonomico = parseFloat(_i.calcularImpuestos(u"iehautonomico", cursor, cursorLinea))
            valor = (iehAutonomico + iehEstatal)
            s12_do_work = False  # BREAK
        if not s12_work_done:
            s12_do_work, s12_work_done = True, True
        return valor

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

    def editarCantidad(self, model, oParam, cursor):
        return self.ctx.blackstar_petroleum_albaranes_editarCantidad(model, oParam, cursor)

    def editarPvpArticulo(self, model, oParam, cursor):
        return self.ctx.blackstar_petroleum_albaranes_editarPvpArticulo(model, oParam, cursor)

    def field_pvparticulo(self, model):
        return self.ctx.blackstar_petroleum_albaranes_field_pvparticulo(model)

    def field_cuotaieh(self, model):
        return self.ctx.blackstar_petroleum_albaranes_field_cuotaieh(model)

    def calcularImpuestos(self, fN, curAlbaran, cursorLinea):
        return self.ctx.blackstar_petroleum_albaranes_calcularImpuestos(fN, curAlbaran, cursorLinea)

