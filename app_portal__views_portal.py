
# @class_declaration blackstar_petroleum_albaranes #
from models.flfactppal.clientes import clientes
from models.flfactppal.agentes import agentes


class blackstar_petroleum_albaranes(yblogin):

    def blackstar_petroleum_albaranes_createUsers(self, request):
        pass
        # users = open(path.join(settings.PROJECT_ROOT, 'fichero.csv'), "rU")
        # data = csv.DictReader(users)
        # i = 0
        # for row in data:
        #     print(i)
        #     username = row["username"]
        #     password = row["password"]
        #     try:
        #         user = User.objects.create_user(username=username, password=password)
        #         user.is_staff = False
        #         user.groups.add(Group.objects.get(name='clientes'))
        #         user.save()
        #     except Exception as e:
        #         print(e)
        #         print(username)
        #     # time.sleep(0.5)
        #     i = i + 1
        # return False

    def blackstar_petroleum_albaranes_auth_login(self, request):
        if request.method == "POST":
            action = request.POST.get("action", None)
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            print(username)
            print(password)
            if action == "login":
                user = authenticate(username=username, password=password)
                print(user)
                if user is not None:
                    login_auth(request, user)
                else:
                    return self.iface.login(request, "Error de autentificación")
                accessControl.accessControl.registraAC()
                return HttpResponseRedirect("/")
        return self.iface.login(request)

    def __init__(self, context=None):
        super().__init__(context)

    def createUsers(self, request):
        return self.ctx.blackstar_petroleum_albaranes_createUsers(request)

    def auth_login(self, request):
        return self.iface.blackstar_petroleum_albaranes_auth_login(request)

