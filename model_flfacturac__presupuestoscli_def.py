
# @class_declaration blackstar_petroleum_albaranes #
from YBLEGACY.constantes import *
from YBUTILS import notifications


class blackstar_petroleum_albaranes(flfacturac):

    def blackstar_petroleum_albaranes_initValidation(self, name, data):
        response = True
        return response

    def blackstar_petroleum_albaranes_getForeignFields(self, model, template):
        return []

    def blackstar_petroleum_albaranes_getFilters(self, model, name, template):
        return []

    def blackstar_petroleum_albaranes_envioPresupuesto(self, model, oParam):
        print("____", oParam)
        print(qsatype.FLUtil.nameUser())
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"clientes")
        q.setSelect(u"nombre")
        q.setFrom(u"clientes")
        q.setWhere(ustr(u"cifnif = '", qsatype.FLUtil.nameUser(), u"'"))

        if q.exec_():
            if q.next():
                cliente = q.value(0)
        if(oParam):
            titulo = "Solicitud Presupuesto " + str(cliente) + " " + str(oParam['titulo'])
            response = notifications.sendSisMail(titulo, oParam['texto'])
            return response
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def initValidation(self, name, data):
        return self.ctx.blackstar_petroleum_albaranes_initValidation(name, data)

    def getForeignFields(self, model, template):
        return self.ctx.blackstar_petroleum_albaranes_getForeignFields(model, template)

    def getFilters(self, model, name, template):
        return self.ctx.blackstar_petroleum_albaranes_getFilters(model, name, template)

    def envioPresupuesto(self, model, oParam):
        return self.ctx.blackstar_petroleum_albaranes_envioPresupuesto(model, oParam)

