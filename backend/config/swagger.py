# System
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.utils import swagger_auto_schema

schema_view = get_schema_view(
    openapi.Info(
        title="Will API Swagger",
        default_version="v1",
        description="Will API Swagger",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
)


class Swagger:
    def __init__(self, res, path=None, body=None) -> None:
        self.path = []
        self.body = {}
        self.res = {}

        if not path:
            path = []

        if not body:
            body = []

        for p in path:
            self.path.append(
                openapi.Parameter(
                    p["name"],
                    openapi.IN_PATH,
                    type=p["type"],
                    default=p["default"],
                    required=p["required"],
                    description=p["description"],
                )
            )

        for b in body:
            self.body[b["name"]] = openapi.Schema(
                type=openapi.TYPE_STRING,
                description=b["description"],
            )

        for r in res:
            self.res[r["name"]] = openapi.Response(
                description=r["description"],
                examples={"application/json": r["res"]},
            )

        if body:
            self.req = openapi.Schema(type=openapi.TYPE_OBJECT, properties=self.body)
        else:
            self.req = None

    @property
    def swagger(self):
        return swagger_auto_schema(manual_parameters=self.path, request_body=self.req, responses=self.res)
