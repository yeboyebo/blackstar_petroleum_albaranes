
# @class_declaration blackstar_petroleum_albaranes #
from YBLEGACY.constantes import *
from YBUTILS.viewREST import cacheController


class blackstar_petroleum_albaranes(flfacturac):

    def blackstar_petroleum_albaranes_bufferCommited_lineasalbaranescli(self, curLinea=None):
        # _i = self.iface
        curAlbaran = qsatype.FLSqlCursor(u"albaranescli")
        curAlbaran.select(ustr(u"idalbaran = ", curLinea.valueBuffer(u"idalbaran")))
        if not curAlbaran.first():
            return False
        curAlbaran.setModeAccess(curAlbaran.Edit)
        curAlbaran.refreshBuffer()
        if not qsatype.FactoriaModulos.get('formRecordalbaranescli').iface.calcularTotalesCursor(curAlbaran):
            return False
        if not curAlbaran.commitBuffer():
            return False
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def bufferCommited_lineasalbaranescli(self, curLinea=None):
        return self.ctx.blackstar_petroleum_albaranes_bufferCommited_lineasalbaranescli(curLinea)

