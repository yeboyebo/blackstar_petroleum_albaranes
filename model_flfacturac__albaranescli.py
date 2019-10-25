
# @class_declaration blackstar_petroleum_albaranes_albaranescli #
class blackstar_petroleum_albaranes_albaranescli(flfacturac_albaranescli, helpers.MixinConAcciones):
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

    @helpers.decoradores.accion(aqparam=["oParam"])
    def nuevoalbaran(self, oParam):
        return form.iface.nuevoalbaran(self, oParam)

    @helpers.decoradores.accion(aqparam=["oParam", "cursor"])
    def nuevalineaalbaran(self, oParam, cursor):
        return form.iface.nuevalineaalbaran(self, oParam, cursor)

    def field_colorRow(cursor):
        return form.iface.field_colorRow(cursor)

    @helpers.decoradores.accion(tipo="O")
    def damenuevoalbaran(self):
        return form.iface.damenuevoalbaran(self)

