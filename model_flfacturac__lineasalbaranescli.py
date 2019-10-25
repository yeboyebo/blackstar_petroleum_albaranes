
# @class_declaration blackstar_petroleum_albaranes_lineasalbaranescli #
class blackstar_petroleum_albaranes_lineasalbaranescli(flfacturac_lineasalbaranescli, helpers.MixinConAcciones):
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

    def getDesc():
        return form.iface.getDesc()

    @helpers.decoradores.accion(aqparam=["oParam", "cursor"])
    def editarCantidad(self, oParam, cursor):
        return form.iface.editarCantidad(self, oParam, cursor)

    @helpers.decoradores.accion(aqparam=["oParam", "cursor"])
    def editarPvpArticulo(self, oParam, cursor):
        return form.iface.editarPvpArticulo(self, oParam, cursor)

    def field_pvparticulo(cursor):
        return form.iface.field_pvparticulo(cursor)

    def field_cuotaieh(cursor):
        return form.iface.field_cuotaieh(cursor)

