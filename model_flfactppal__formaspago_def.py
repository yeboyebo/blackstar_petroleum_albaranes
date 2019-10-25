
# @class_declaration blackstar_petroleum_albaranes #


class blackstar_petroleum_albaranes(flfactppal):

    def blackstar_petroleum_albaranes_getFormasPagoLabel(self, model, oParam):
        data = []
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"formaspago")
        q.setSelect(u"codpago, descripcion")
        q.setFrom(u"formaspago")
        q.setWhere(u"UPPER(descripcion) LIKE '%" + oParam['val'].upper() + "%' OR UPPER(codpago) LIKE '%" + oParam['val'].upper() + "%' GROUP BY codpago, descripcion LIMIT 7")

        if not q.exec_():
            print("Error inesperado")
            return []
        if q.size() > 100:
            return []

        while q.next():
            descFormasPago = str(q.value(0)) + "_ " + q.value(1)
            data.append({"codpago": q.value(0), "descripcion": q.value(1), "descFormasPago": descFormasPago})

        return data

    def __init__(self, context=None):
        super().__init__(context)

    def getFormasPagoLabel(self, model, oParam):
        return self.ctx.blackstar_petroleum_albaranes_getFormasPagoLabel(model, oParam)

