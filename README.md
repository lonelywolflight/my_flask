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