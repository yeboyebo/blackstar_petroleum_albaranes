
# @class_declaration blackstar_formaspago #
class blackstar_petroleum_albaranes_formaspago(flfactppal_formaspago, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    @helpers.decoradores.accion(aqparam=["oParam"])
    def getFormasPagoLabel(self, oParam):
        return form.iface.getFormasPagoLabel(self, oParam)

