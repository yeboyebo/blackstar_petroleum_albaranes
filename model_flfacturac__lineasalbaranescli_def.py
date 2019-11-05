
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
            curAlbaran.select(ustr(u"idalbaran = ", model.idalbaran.idalbaran))
            if curAlbaran.next():
                curAlbaran.setModeAccess(curAlbaran.Browse)
                curAlbaran.refreshBuffer()
                cuotaieh = self.iface.calcularImpuestos("cuotaieh", curAlbaran, curLA)
        return cuotaieh

    def blackstar_petroleum_albaranes_editarPvpArticulo(self, model, oParam, cursor):
        curAlbaran = qsatype.FLSqlCursor(u"albaranescli")
        curAlbaran.select(u"idalbaran = {}".format(cursor.valueBuffer("idalbaran")))
        if not curAlbaran.first():
            return False
        if not curAlbaran.valueBuffer("ptefactura"):
            resul = {}
            resul['status'] = -3
            resul['msg'] = "Albaran facturado"
            return resul
        cursor.setActivatedBufferCommited(True)
        cursor.setValueBuffer("pvpunitario", oParam['pvpunitario'])
        qsatype.FactoriaModulos.get('formRecordlineasalbaranescli').iface.bChCursor("pvpunitario", cursor)
        if not cursor.commitBuffer():
            return False
        curAlbaran.setModeAccess(curAlbaran.Browse)
        curAlbaran.refreshBuffer()
        # qsatype.FactoriaModulos.get('formRecordalbaranescli').iface.calcularTotalesCursor(curAlbaran)
        codcliente = curAlbaran.valueBuffer("codcliente")
        riesgomax = qsatype.FLUtil.sqlSelect(u"clientes", u"riesgomax", u"codcliente = '{}'".format(codcliente))
        if riesgomax:
            riesgoalcanzado = qsatype.FLUtil.sqlSelect(u"clientes", u"riesgoalcanzado", u"codcliente = '{}'".format(codcliente))
            if curAlbaran.valueBuffer("total") + riesgoalcanzado > riesgomax:
                print("operacion invalida")
                response = {}
                response['status'] = 1
                response['msg'] = "Riesgo máximo alcanzado"
                return response
            if not curAlbaran.commitBuffer():
                return False
        return True

    def blackstar_petroleum_albaranes_editarCantidad(self, model, oParam, cursor):
        curAlbaran = qsatype.FLSqlCursor(u"albaranescli")
        curAlbaran.select(u"idalbaran = {}".format(cursor.valueBuffer("idalbaran")))
        if not curAlbaran.first():
            return False
        if not curAlbaran.valueBuffer("ptefactura"):
            resul = {}
            resul['status'] = -3
            resul['msg'] = "Albaran facturado"
            return resul
        cursor.setActivatedBufferCommited(True)
        cursor.setValueBuffer("cantidad", oParam['cantidad'])
        codcliente = curAlbaran.valueBuffer("idalbaran")
        idProvincia = curAlbaran.valueBuffer("bi_idprovinciaentrega")
        cursor.setValueBuffer("cuotaieh", self.iface.calcularImpuestos("cuotaieh", cursor, codcliente, idProvincia))
        qsatype.FactoriaModulos.get('formRecordlineasalbaranescli').iface.bChCursor("cantidad", cursor)
        if not cursor.commitBuffer():
            return False
        curAlbaran.setModeAccess(curAlbaran.Browse)
        curAlbaran.refreshBuffer()
        # qsatype.FactoriaModulos.get('formRecordalbaranescli').iface.calcularTotalesCursor(curAlbaran)
        riesgomax = qsatype.FLUtil.sqlSelect(u"clientes", u"riesgomax", u"codcliente = '{}'".format(codcliente))
        if riesgomax:
            riesgoalcanzado = qsatype.FLUtil.sqlSelect(u"clientes", u"riesgoalcanzado", u"codcliente = '{}'".format(codcliente))
            if curAlbaran.valueBuffer("total") + riesgoalcanzado > riesgomax:
                print("operacion invalida")
                response = {}
                response['status'] = 1
                response['msg'] = "Riesgo máximo alcanzado"
                return response
            if not curAlbaran.commitBuffer():
                return False
        return True

    def blackstar_petroleum_albaranes_calcularImpuestos(self, fN, cursorLinea, codcliente, idProvincia):
        _i = self.iface
        if fN == u"iehautonomicounitario":
            referencia = cursorLinea.valueBuffer(u"referencia")
            regsuspensivo = qsatype.FLUtil.sqlSelect(u"clientes", u"regsuspensivo", u"codcliente = '{}'".format(codcliente))
            # idProvincia = qsatype.FLUtil.sqlSelect(u"dirclientes", u"idprovincia", ustr(u"codcliente = '", codcliente, u"' AND domfacturacion"))
            if regsuspensivo:
                valor = 0
            else:
                valor = qsatype.FLUtil.sqlSelect(u"bio_impprovincias", u"iehautonomico", u"idprovincia = {} AND referencia = '{}'".format(idProvincia, referencia))
                if not valor or isNaN(valor):
                    valor = 0
        elif fN == u"iehestatalunitario":
            referencia = cursorLinea.valueBuffer(u"referencia")
            regsuspensivo = qsatype.FLUtil.sqlSelect(u"clientes", u"regsuspensivo", u"codcliente = '{}'".format(codcliente))
            # idProvincia = qsatype.FLUtil.sqlSelect(u"dirclientes", u"idprovincia", ustr(u"codcliente = '", codcliente, u"' AND domfacturacion"))
            if regsuspensivo:
                valor = 0
            else:
                valor = qsatype.FLUtil.sqlSelect(u"bio_impprovincias", u"iehestatal", u"idprovincia = {} AND referencia = '{}'".format(idProvincia, referencia))
                if not valor or isNaN(valor):
                    valor = 0
        elif fN == u"iehautonomico":
            cantidad = parseFloat(cursorLinea.valueBuffer(u"cantidad"))
            iehAutonomicoUnitario = parseFloat(_i.calcularImpuestos(u"iehautonomicounitario", cursorLinea, codcliente, idProvincia))
            valor = cantidad * iehAutonomicoUnitario

        elif fN == u"iehestatal":
            cantidad = parseFloat(cursorLinea.valueBuffer(u"cantidad"))
            iehEstatalUnitario = parseFloat(_i.calcularImpuestos(u"iehestatalunitario", cursorLinea, codcliente, idProvincia))
            valor = cantidad * iehEstatalUnitario

        elif fN == u"cuotaieh":
            cantidad = parseFloat(cursorLinea.valueBuffer(u"cantidad"))
            iehEstatal = parseFloat(_i.calcularImpuestos(u"iehestatal", cursorLinea, codcliente, idProvincia))
            iehAutonomico = parseFloat(_i.calcularImpuestos(u"iehautonomico", cursorLinea, codcliente, idProvincia))
            valor = (iehAutonomico + iehEstatal)
        else:
            valor = 0
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

    def calcularImpuestos(self, fN, cursorLinea, codcliente, idProvincia):
        return self.ctx.blackstar_petroleum_albaranes_calcularImpuestos(fN, cursorLinea, codcliente, idProvincia)

