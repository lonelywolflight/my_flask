# 项目介绍
这是一个最基础的FLASK项目。项目的结构如下：
>hello_flask<br>
>- flask的根目录
>>-run.py<br>
>>- 配置FLASK run的时候的配置，可以指定debug mode或使用其他配置
>>>-my_app<br>
>>>- 项目中的一个module目录
>>>__init__.py<br>
>>>- 用来标识当前目录是一个module，一般会在此目录构建一个FLASK对象
>>>>hello<br>
>>>>>__init__.py<br>
>>>>>models.py<br>
>>>>>- 用于放置所有的model
>>>>>views.py
>>>>>- 用于放置所有的view逻辑



## **本项目的用意**
主要是为了让大家熟悉flask项目的结构。
### ***收获***
1. 当一个项目越来越复杂时，我们就需要对业务进行分包存放
2. 通过使用缓存数据，我们做到了增、删、改、查的基本操作
3. 在此项目中，我们会在my_app中的__init__.py中import进来views中的东西。而在views文件中，我们又import了my_app。如此一来，形成了一个环。但我们并不建议这么做。


## blueprint的应用
1. 对于分多个包的时候，可以使用blueprint，将每个包当作APP
### 用法
1. 在需要blueprint的view视图中定义Blueprint
2. 在app中将blueprint注册

## flask中使用db(使用postgreSQL)
1. 准备相应的库
    1. Flask-SQLAlchemy
    2. psycopg2-binary
    3. Flask-Migrate
2. 配置数据库文件
    1. 在根目录的__init__.py中配置数据库的URI。如：
    ```
    app.config["SQLALCHEMY_DATABASE_URI"] = 
        "postgresql://postgres:Programdog666@localhost/flask_db"
    ```
    2. 创建db=SQLAlchemy()
    3. 调用db.init_app(app)
    4. 通过with初始化所有的table<br>
    ```
    with app.app_context():
        db.create_all()
    ```
3. 通过db.session进行增删改查
### note
1. 添加外键约束
```
category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
```
2. 与外表进行many-one的映射关系
```
category = db.relationship('Category', backref=db.backref('products', lazy='dynamic'))
```
3. migrate的使用
    1. 首先，对应的terminal中，必须申明了export FLASK_APP=run.py
    2. 调用flask db init，该命令会创建migrations文件夹
    3. 调用flask db migrate，该命令会生成迁移的方法
    4. 调用flask db upgrade，该方法会作用到数据库，改变数据库中的table

## redis在Flask中的使用
 1. 在电脑上[安装redis](https://redis.io/docs/data-types/tutorial/)
 2. 下载redis库的依赖
 3. 在app中的__init__.py中创建redis对象
 ```
    from redis import Redis
    
    redis = Redis
 ```
(**Note**: 当前配置使用了默认的端口号和IP)
 - 4. 在程序中调用redis.set(key, value)保存数据。并调用redis.expire(600)设置有效时间为10分钟
 - 5. 通过redis.get(key)获取对应key的值
 ### redis server
 1. 输入redis server启动redis数据库服务
 2. 输入redis-cli，进入redis命令行模式

 ## [WSL安装PostgreSQL，redis已经mongodb](https://learn.microsoft.com/zh-cn/windows/wsl/tutorials/wsl-database)
 ### postgreSQL
 1. 服务
    1. `sudo service postgresql status`
    2. `sudo service postgresql start`
    3. `sudo service postgresql stop`
 2. max 账号
 3. 连接数据库
    1. `su - postgres`，切换至postgres用户
    2. `psql flask_db`，连接flask_db数据库
### MongoDB
 1. 运行Mongo实例
    1. `sudo mongod --dbpath ~/data/db`（**由于wsl无法启动MongoDB service，所以直接运行实例**）
    2. 检查MongoDB实例是否正在运行，`ps -e | grep 'mongod' `
## MongoDB在Flask中的应用
 1. 下载flak-mongodbengine(***Note:***1.0.0版本可能需要配合Flask 2.0.0的库使用。如果使用最新的Flask库，可能会出现问题)
 2. 在app中的__init__.py中配置
 ```
 from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = [{
    "DB": 'my_app',
    "host": "localhost",
    "port": 27017,
    "alias": "default",
}]

db.init_app(app)
 ```
 3. 定义model，Product
 ```
 import datetime
from my_app import db

class Product(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    key = db.StringField(max_length=255,required=True)
    name = db.StringField(max_length=255, required=True)
    price = db.DecimalField()

    def __repr__(self):
        return '<Product %r>' % self.id
 ```
 4. [查询语句](https://flask.palletsprojects.com/en/2.3.x/patterns/mongoengine/)
    1. 单个查询
    ```
    Product.objects(key=key).get_or_404()
    ```
    2. 全部查询
    ```
    Product.objects.all()
    ```
    3. 插入
    ```
    product = Product(name=name,key=key,price=Decimal(price))
    
    product.save()
    ```
## requesst上下文
### request获取数据方式
 1. Get方法
 ```
    request.args.get('name')
 ```
 2. Post方法
 ```
    request.form.get('name')
 ```
## Class base view
 1. 继承View
 ```
from flask.typing import ResponseReturnValue
from flask.views import View, MethodView
from flask import request
from my_app import app

class GetPostRequest(View):

    methods = ['GET', 'POST']
    
    def dispatch_request(self) -> ResponseReturnValue:
        if request.method == 'GET':
            bar = request.args.get('foo', 'bar')
        else:
            bar = request.form.get('foo', 'bar')
        return 'A simple Flask request where foo is %s' % bar
    
app.add_url_rule('/a-request', view_func = GetPostRequest.as_view('a_request'))
 ```
 2. 继承MethodView
 ```
class GetMethodRequest(MethodView):

    def get(self):
        bar = request.args.get('foo', 'bar')
        return 'A simple Flask request where foo is %s' % bar
    

    def post(self):
        bar = request.form.get('foo', 'bar')
        return 'A simple Flask request where foo is %s' % bar
    
app.add_url_rule('/method-request', view_func=GetMethodRequest.as_view('method_request'))
 ```
