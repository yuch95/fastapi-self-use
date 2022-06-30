# @Time    : 2022/6/30 下午4:34
# @Author  : 余冲
# @Email   : 948758821@qq.com
# @File    : main.py
# @Software: PyCharm
import uvicorn
from fastapi import FastAPI, Query

from utils.resource import Api, Resource

app = FastAPI()
api = Api(prefix='/api', tags=['测试tag'])


class MyApi(Resource):

    def get(self, book_id=Query(..., description='图书ID')):
        """测试"""
        print(self.request.method)
        return {'book_id': book_id}


api.add_resource(MyApi(), '/my')
app.include_router(api)

uvicorn.run(app)