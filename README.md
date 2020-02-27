# 中国疫情大数据可视化

------

> 之前通过pyecharts画了河南的疫情图，但是由于颜色不直观，所以看不出疫情的情况，所以就用了几天时间，做了一个搭载在Django框架上的中国以及中国各地区的疫情图。预览如下

 <div><img src="https://github.com/chain312/epidemic/blob/master/static/images/map.gif"/></div>

##01Django框架使用
Django是python写的web MVC框架，利用此框架可以快速开发部署项目，在Django框架中提供后台管理站点和CSRF漏洞防范，能够方便站点的管理和上线后的CSRF防御。话不多说，一起来看下，在此项目中Django框架的使用。框架中的使用主要包括下面几个步骤

> * Django安装
> * 创建项目
> * 创建应用
> * 注册应用
> * 更改相关配置
###Django安装
首先要在开发环境中安装Django,笔者的开发环境是Windows环境。安装的版本为2.2.4
 <div><img src="https://github.com/chain312/epidemic/blob/master/static/images/111.jpg"/></div>
在安装时可以指定Django框架为2.2.4

    pip install Django==2.2.4 

如果你没更换pip源，可以用下面指定国内源

    pip install Django==2.2.4 -i https://pypi.tuna.tsinghua.edu.cn/simple

安装完成后，查看是否安装成功
 <div><img src="https://github.com/chain312/epidemic/blob/master/static/images/2.png"/></div>
至此，Django框架就安装成功了。
###创建项目
那么如何新建一个epidemic_map的应用呢？
Django中创建应用和其他语言如C,C#类似，都要新创建一个项目，在新项目中创建一个应用。
Django创建项目的命令为

    django-admin startproject 项目名

例如

    django-admin startproject epidemic

如果你要指定的文件夹下创建项目的话，可以先切换文件目录
例如，我把项目创建在D:\file下
 <div><img src="https://github.com/chain312/epidemic/blob/master/static/images/3.png"/></div>
项目目录如下
epidemic1 项目名
 ├── epidemic1 
 │   ├── settings.py 项目的通用配置
 │   ├── urls.py URL路由配置
 │   ├── wsgi.py 服务器与Django交互入口
 │   └── __init__.py 将项目标识为python包
 └── manage.py 项目管理
在此次开发中需要用到settings.py urls.py manage.py，这三个文件到使用的时候再进行说明。
项目创建完成后，创建应用。
进入到epidemic1中，使用manage.py文件创建应用
manage.py是每个Django项目中自动生成的一个用于管理项目的脚本文件，需要通过python命令执行。manage.py接受的是Django提供的内置命令，它的内置命令很多，在此开发中我们用到的内置命令为下面2个：
startapp  创建新的app。
runserver 启用Django为我们提供的轻量级的开发用的Web服务器。
###创建应用

    python manage.py startapp 应用名

如

    python manage.py startapp epidemic_map

epidemic_map的文件目录如下：
epidemic_map
 ├── admin.py Django自带后台管理
 ├── apps.py
 ├── migrations 应用迁移历史
 │   └── __init__.py
 ├── models.py
         modles.py写和数据库相关的内容定义模型类
 ├── tests.py
tests.py 文件用于开发测试用例使用，在实际开发中会有专门的人来测试
 ├── views.py
views.py接收请求，进行处理，定义处理函数，视图函数
 └── __init__.py  标识目录是python模块
注册应用
要想项目包含和访问应用还要在项目中注册应用
用pycharm导入项目，打开settings.py,在
INSTALLED_APPS中加入新创建的应用，如下:
 <div><img src="https://github.com/chain312/epidemic/blob/master/static/images/4.png"/></div>
###更改相关配置
还需要设置时区和使用语言，如下

    LANGUAGE_CODE = 'zh-hans' #使用中国语言
    TIME_ZONE = 'Asia/Shanghai' #使用中国上海时间

 <div><img width="655" height="361" src="https://github.com/chain312/epidemic/blob/master/static/images/5.png"/></div>
改为
 <div><img width="655" height="361" src="https://github.com/chain312/epidemic/blob/master/static/images/6.png"/></div>
至此Django框架的配置就告一段落。
总结下要点
 <div><img src="https://github.com/chain312/epidemic/blob/master/static/images/Django%E4%BD%BF%E7%94%A8.png"/></div>

##02全国各地区的数据准备

数据来源还是丁香医生，通过爬虫爬取数据，再通过正则表达式匹配到需要的数据。
网络爬虫代码为

 

    import requests
    s = requests.session()
    url = "https://3g.dxy.cn/newh5/view/pneumonia"
    response = s.get(url)
    response.encoding = 'utf-8'
    html = response.text
利用正则表达式匹配城市及疫情数据

    正则表达式可以匹配除内蒙古以外的所有地区
     dict={'beijing':'北京市','tianjin':'天津市','shanghai':'上海市','chongqing':'重庆市','hebei':'河北省','shanxi1':'山西省','liaoning':'辽宁省','jilin':'吉林省','heilongjiang':'黑龙江省','jiangsu':'江苏省','zhejiang':'浙江省','anhui':'安徽省','fujian':'福建省','jiangxi':'江西省','shandong':'山东省','henan':'河南省','hubei':'湖北省','hunan':'湖南省','guangdong':'广东省','hainan':'海南省','sichuan':'四川省','guizhou':'贵州省','yunnan':'云南省','shanxi':'陕西省','gansu':'甘肃省','qinghai':'青海省','taiwan':'台湾','neimeng':'内蒙古自治区','guangxi':'广西壮族自治区','xizang':'西藏自治区','ningxia':'宁夏回族自治区', 'xinjiang':'新疆维吾尔自治区','xianggang':'香港','aomen':'澳门'}
    regular = '(\{\\\"provinceName"\:\\\"' + dict[province] + '\\\"\,\\\"provinceShortName\\\".+?\{\\\"provinceName\\\")'
    data_json = re.findall(re.compile(regular), str(html))

    匹配内蒙古的正则表达式为
        dict={'beijing':'北京市','tianjin':'天津市','shanghai':'上海市','chongqing':'重庆市','hebei':'河北省','shanxi1':'山西省','liaoning':'辽宁省','jilin':'吉林省','heilongjiang':'黑龙江省','jiangsu':'江苏省','zhejiang':'浙江省','anhui':'安徽省','fujian':'福建省','jiangxi':'江西省','shandong':'山东省','henan':'河南省','hubei':'湖北省','hunan':'湖南省','guangdong':'广东省','hainan':'海南省','sichuan':'四川省','guizhou':'贵州省','yunnan':'云南省','shanxi':'陕西省','gansu':'甘肃省','qinghai':'青海省','taiwan':'台湾','neimeng':'内蒙古自治区','guangxi':'广西壮族自治区','xizang':'西藏自治区','ningxia':'宁夏回族自治区', 'xinjiang':'新疆维吾尔自治区','xianggang':'香港','aomen':'澳门'}
    regular = '(\{\\\"provinceName"\:\\\"' +  dict[province] + '\\\"\,\\\"provinceShortName\\\".+?\\}\\]\\}\\]\\})'
    data_json = re.findall(re.compile(regular), str(html))
匹配出数据后还要进行筛选，得到现存感染人数和对应的城市

        city_data = re.findall(re.compile(r'(\d+)'), str(data_json))
    city = re.findall(re.compile(r'([\u4E00-\u9FA5]+)'), str(data_json))
    city_name = city_name[2:len(city_name)]
    city_data = city_data[6:len(city_data):6]
其中，匹配出来的城市名和地图中的城市名称对不上，相应的还要进行修改城市名，在画图的时候还要进行修改。

##03地图配置更改
在上次画的河南疫情地图上进行修改，上次画的疫情图如下。
<div><img width="655" height="361" rc="https://github.com/chain312/epidemic/blob/master/static/images/%E4%B8%8B%E8%BD%BD%20(1).png"/></div>
需要做的修改为：

> * 将颜色根据数据大小划分
> * 去除丁香医生数据标识（不美观）
> * 在地图顶部显示省份
> * 更改选中区域颜色
> * 限制生成画板规格
> * 更改生成地图页面模板

更改成如下
<div><img src="https://github.com/chain312/epidemic/blob/master/static/images/%E6%B2%B3%E5%8D%97%E7%96%AB%E6%83%85.png"/></div>
修改后代码如下

     g = (
            Map(init_opts=opts.InitOpts(width = '1440px', height='800px'))#设置画布大小
                .add(dict[province]+"疫情地图", [list(z) for z in zip(city_name, city_data)], maptype=dict1[province],is_map_symbol_show=False,
                #is_map_symbol_show为去除地图中的小红点标注
                itemstyle_opts=opts.ItemStyleOpts(color="#ede586"),
                # 设置选中区的颜色为黄色
                )
                .set_global_opts(
                                 visualmap_opts=opts.VisualMapOpts(
                                     is_piecewise=True, 
                                     # 是否分段为是，左下角会出现分段颜色
                                     #pieces指定地图数据对应的颜色
                                     pieces=[{"min": 0, "max": 0, "label": "0",
                                              "color": "#FFFFFF"},
                                             {"min": 1, "max": 9, "label": "1-9",
                                              "color": "#FDEBCF"},
                                             {"min": 10, "max": 49, "label": "10-49",
                                              "color": "#F59E83"},
                                             {"min": 50, "max": 99, "label": "50-99",
                                              "color": "#E55A4E"},
                                             {"min": 100, "max": 199, "label": "100-199",
                                              "color": "#CB2A2F"},
                                             {"min": 200, "max": 499, "label": "200-499",
                                              "color": "#811C24"},
                                             {"min": 500, "max": 10000000000, "label": "> 500",
                                              "color": "#4F070D"}],
                                                                   ),
    
    
                                 )
        )
        g.render(path='templates/templates_map/'+province+'.html',template_name='mapmodel.html')  
        #默认使用的生成地图模板在Python\Lib\site-packages\pyecharts\render\templates\目录下，
        #可以将我们自己的模板复制到该目录下  
##04在Django 框架中实现地图生成
 在应用的view.py中添加生成地图代码，要想通过浏览器访问到该网页，要明白网络的‘路由’过程。
用户通过浏览器访问应用，首先到项目的urls.py,再路由到应用的urls.py，最后到应用的views.py.路由顺序如下
<div><img src="https://github.com/chain312/epidemic/blob/master/static/images/8.png"/></div>
    在新建应用中，没有2 urls.py文件，在应用中要新建一个urls.py文件，在‘路由过程中’，如何让项目中的1指向2呢？要在1中添加以下代码
<div><img src="https://github.com/chain312/epidemic/blob/master/static/images/9.png"/></div>
还要在2内添加
<div><img src="https://github.com/chain312/epidemic/blob/master/static/images/10.png"/></div>
2如何访问3呢？需要在2内进行以下修改
<div><img src="https://github.com/chain312/epidemic/blob/master/static/images/11.png"/></div>
‘路由’配置完后，进行代码编写。项目详情见

    https://github.com/chain312/epidemic
项目的预览为

    https://chain312.github.io/epidemic/templates/templates_map/index.html

##问题反馈
在你使用过程中,有什么建议或者问题,欢迎反馈

 - 微信:wei8896966
 - 公众号:鸡术有限

![公众号][1]


  [1]: https://github.com/chain312/epidemic/blob/master/static/images/%E5%85%AC%E4%BC%97%E5%8F%B7.jpg
