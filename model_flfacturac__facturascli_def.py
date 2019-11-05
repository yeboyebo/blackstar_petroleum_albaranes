
# @class_declaration blackstar_petroleum_albaranes #
from YBLEGACY.constantes import *
from models.flfactppal.clientes import clientes


class blackstar_petroleum_albaranes(interna):

    def blackstar_petroleum_albaranes_initValidation(self, name, data):
        response = True
        if name == 'facturascli':
            usr = qsatype.FLUtil.nameUser()
            cliente = clientes.objects.filter(cifnif__exact=usr)
            if not data['DATA']['cifnif'] == cliente[0].cifnif:
                return False
        return response

    def blackstar_petroleum_albaranes_getForeignFields(self, model, template):
        return []

    def blackstar_petroleum_albaranes_getFilters(self, model, name, template):
        filters = []
        if name == 'facturascliente':
            aEjercicios = []
            codejercicios = qsatype.FactoriaModulos.get('flfactppal').iface.dameEjerciciosEmpresa(6)
            codejercicios = codejercicios.replace("'", "")
            aEjercicios = codejercicios.split(",")
            filters = [{'criterio': 'codejercicio__in', 'valor': aEjercicios}]
            usr = qsatype.FLUtil.nameUser()
            cliente = clientes.objects.filter(cifnif__exact=usr)
            filters.append({'criterio': 'codcliente__in', 'valor': [cliente[0].codcliente]})

        return filters

    def blackstar_petroleum_albaranes_facturaCliente(self, model):
        report = {}
        report['reportName'] = "biofacturaorden"
        report['params'] = {}
        report['params']['WHERE'] = "facturascli.codigo = '" + model.codigo + "'"
        return report

    def __init__(self, context=None):
        super().__init__(context)

    def initValidation(self, name, data):
        return self.ctx.blackstar_petroleum_albaranes_initValidation(name, data)

    def getForeignFields(self, model, template):
        return self.ctx.blackstar_petroleum_albaranes_getForeignFields(model, template)

    def getFilters(self, model, name, template):
        return self.ctx.blackstar_petroleum_albaranes_getFilters(model, name, template)

    def facturaCliente(self, model):
        return self.ctx.blackstar_petroleum_albaranes_facturaCliente(model)

