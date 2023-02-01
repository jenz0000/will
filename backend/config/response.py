# System
from django.http import HttpRequest
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
    res_dict["code"] = code[0]
    res_dict["message"] = code[1]
    res_dict["success"] = code == CODE.SUCCESS

    return Response(res_dict, status=status_code, headers=headers)


def get_ip(request: HttpRequest):
    """
    Return the IP of the request, accounting for the possibility of being behind a proxy.
    """

    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_user_agent(request: HttpRequest):
    return request.META.get("HTTP_USER_AGENT", "")
