from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from hasura.roles import HasuraRoles
from hasura.utils import AuthResponse


class HasuraWebHookAuth(APIView):
    permission_classes = (AllowAny,)

    def handle_auth(self, data):
        user = self.request.user
        user_role = HasuraRoles.ANONYMOUS
        if user.is_authenticated:
            user_role = HasuraRoles.USER
            if user.is_staff:
                user_role = HasuraRoles.ADMIN
        resp = AuthResponse(user_id=user.id, role=user_role)
        print(resp.data)
        print(user)
        return resp

    def post(self, request):
        data = dict(request.data)
        return self.handle_auth(data)

    def get(self, request):
        data = dict(request.query_params)
        return self.handle_auth(data)
