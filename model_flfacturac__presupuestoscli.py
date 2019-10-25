
# @class_declaration blackstar_petroleum_albaranes_presupuestoscli #
class blackstar_petroleum_albaranes_presupuestoscli(flfacturac_presupuestoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def initValidation(name, data):
        return form.iface.initValidation(name, data)

    def getForeignFields(self, template=None):
        return form.iface.getForeignFields(self, template)

    def getFilters(self, name, template):
        return form.iface.getFilters(self, name, template)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def envioPresupuesto(self, oParam):
        return form.iface.envioPresupuesto(self, oParam)

