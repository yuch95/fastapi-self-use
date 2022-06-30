### 描述
##### 该文件是对fastapi-restful的自用改造，主要是基于资源类进行构建路由试图

# resource
## Resource
该类属于公共资源类，可以对该类进行重写来增加公共数据，方便在接口视图中获取

## Api
该类继承自APIRouter,属于路由类。根据restful的Api类进行的改造。
### add_resource(resource, *urls)
根据资源参数方法添加路由

