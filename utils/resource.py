# @Time    : 2022/6/30 上午9:30
# @Author  : 余冲
# @Email   : 948758821@qq.com
# @File    : resource.py
# @Software: PyCharm
from enum import Enum
from typing import Any, Optional, Union, Sequence, List

from fastapi import FastAPI, APIRouter, Request, Depends
from fastapi_restful import Api as BaseApi

from utils.cbv import cbv


class Resource:
    def __init__(self):
        self.request: Optional[Request] = None
        self.user_data = {}  # 用户信息数据

    @property
    def method(self):
        return self.request.method

    @property
    def url(self):
        return self.request.url


class GlobalDepend:
    """全局依赖 为resource添加资源数据"""
    def __init__(self, resource):
        self.resource = resource

    def __call__(self, request: Request):
        """为Resource添加request参数 可以获取请求信息"""
        self.resource.request = request


class Api(APIRouter):

    def add_resource(self, resource: Resource, *urls: str) -> None:
        # 为路由增加全局依赖
        depends = [Depends(GlobalDepend(resource))]
        self.dependencies = depends if self.dependencies is None else self.dependencies + depends

        cbv(self, type(resource), *urls, instance=resource)
