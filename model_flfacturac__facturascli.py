
# @class_declaration blackstar_petroleum_albaranes_facturascli #
class blackstar_petroleum_albaranes_facturascli(flfacturac_facturascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def initValidation(name, data):
        return form.iface.initValidation(name, data)

    def getForeignFields(self, template=None):
        return form.iface.getForeignFields(self, template)

    def getFilters(self, name, template):
        return form.iface.getFilters(self, name, template)

    def facturaCliente(self):
        return form.iface.facturaCliente(self)

