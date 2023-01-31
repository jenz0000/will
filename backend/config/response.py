# System
from rest_framework import status
from rest_framework.response import Response

# Project
from config.constants import CODE


def create_response(**kwargs) -> Response:
    headers = kwargs.get("headers", None)
    status_code = kwargs.get("status", status.HTTP_200_OK)

    data = kwargs.get("data", {})
    code = kwargs.get("code", CODE.SUCCESS)

    res_dict = {}
    res_dict["data"] = data
    res_dict["code"] = code
    res_dict["success"] = code == CODE.SUCCESS

    return Response(res_dict, status=status_code, headers=headers)
