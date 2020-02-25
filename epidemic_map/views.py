from django.shortcuts import render
from pyecharts import options as opts
from pyecharts.charts import Map
import requests
import re
dict={'beijing':'北京市','tianjin':'天津市','shanghai':'上海市','chongqing':'重庆市','hebei':'河北省','shanxi1':'山西省','liaoning':'辽宁省','jilin':'吉林省','heilongjiang':'黑龙江省','jiangsu':'江苏省','zhejiang':'浙江省','anhui':'安徽省','fujian':'福建省','jiangxi':'江西省','shandong':'山东省','henan':'河南省','hubei':'湖北省','hunan':'湖南省','guangdong':'广东省','hainan':'海南省','sichuan':'四川省','guizhou':'贵州省','yunnan':'云南省','shanxi':'陕西省','gansu':'甘肃省','qinghai':'青海省','taiwan':'台湾','neimeng':'内蒙古自治区','guangxi':'广西壮族自治区','xizang':'西藏自治区','ningxia':'宁夏回族自治区', 'xinjiang':'新疆维吾尔自治区','xianggang':'香港','aomen':'澳门'}
dict1={'beijing':'北京','tianjin':'天津','shanghai':'上海','chongqing':'重庆','hebei':'河北','shanxi1':'山西','liaoning':'辽宁','jilin':'吉林','heilongjiang':'黑龙江','jiangsu':'江苏','zhejiang':'浙江','anhui':'安徽','fujian':'福建','jiangxi':'江西','shandong':'山东','henan':'河南','hubei':'湖北','hunan':'湖南','guangdong':'广东','hainan':'海南','sichuan':'四川','guizhou':'贵州','yunnan':'云南','shanxi':'陕西','gansu':'甘肃','qinghai':'青海','taiwan':'台湾','neimeng':'内蒙古','guangxi':'广西','xizang':'西藏','ningxia':'宁夏', 'xinjiang':'新疆','xianggang':'香港','aomen':'澳门'}

# dict={'beijing':'北京市','tianjin':'天津市','shanghai':'上海市','chongqing':'重庆市','hebei':'河北省','shanxi':'山西省','liaoning':'辽宁省','jilin':'吉林省','heilongjiang':'黑龙江省','jiangsu':'江苏省','zhejiang':'浙江省','anhui':'安徽省','fujian':'福建省','jiangxi':'江西省','shandong':'山东省','henan':'河南省','hubei':'湖北省','hunan':'湖南省','guangzhou':'广东省','hainan':'海南省','sichuan':'四川省','guizhou':'贵州省','yunnan':'云南省','shanxi':'陕西省','gansu':'甘肃省','qinghai':'青海省','taiwan':'台湾省','neimeng':'内蒙古自治区','guangxi':'广西壮族自治区','xizang':'西藏自治区','ningxia':'宁夏回族自治区', 'xinjing':'新疆维吾尔自治区','xianggang':'香港特别行政区','aomen':'澳门特别行政区'}
def getepodemicdata():
    """
    爬虫获取数据

    :return: html
    """
    s = requests.session()
    url = "https://3g.dxy.cn/newh5/view/pneumonia"
    response = s.get(url)
    response.encoding = 'utf-8'
    html = response.text
    print(html)
    # #print(dict[province])
    # regular = '(\{\\\"provinceName"\:\\\"'+dict[province]+'\\\"\,\\\"provinceShortName\\\".+?\{\\\"provinceName\\\")'
    #
    #
    # print(regular)
    # #regular=r'(\{\"provinceName"\:\"{}省\"\,\"provinceShortName\".+?\{\"provinceName\")'.format(province)
    # data_json = re.findall(re.compile(regular), str(html))
    # print(data_json)
    # city_data = re.findall(re.compile(r'(\d+)'), str(data_json))
    # # print(len(city_data))
    # # print(city_data)
    # city = re.findall(re.compile(r'([\u4E00-\u9FA5]+)'), str(data_json))
    # # print(city)
    #
    # city_name = []
    # for i in city:
    #     city_name.append("".join([i, "市"]))
    # city_name=city_name[4:len(city_name)]
    # city_data=city_data[7:len(city_data):6]
    return html

def drawmap(province):

    html =  getepodemicdata()

    # regular = '(\{\\\"provinceName"\:\\\"' + dict[province] + '\\\"\,\\\"provinceShortName\\\".+?\{\\\"provinceName\\\")'
    if dict[province] != '西藏自治区':
        regular = '(\{\\\"provinceName"\:\\\"' + dict[province] + '\\\"\,\\\"provinceShortName\\\".+?\{\\\"provinceName\\\")'

    else:
        regular = '(\{\\\"provinceName"\:\\\"' +  dict[province] + '\\\"\,\\\"provinceShortName\\\".+?\\}\\]\\}\\]\\})'
    data_json = re.findall(re.compile(regular), str(html))
    # print(regular)
    # regular=r'(\{\"provinceName"\:\"{}省\"\,\"provinceShortName\".+?\{\"provinceName\")'.format(province)
    data_json = re.findall(re.compile(regular), str(html))
    # print(data_json)
    city_data = re.findall(re.compile(r'(\d+)'), str(data_json))
    # print(len(city_data))
    # print(city_data)
    city = re.findall(re.compile(r'([\u4E00-\u9FA5]+)'), str(data_json))
    # print(city)

    city_name = []
    if province == 'hubei' or  province == 'zhejiang' or province=='anhui' or province=='jiangxi' or province=='hunan' or province=='jiangsu' or province=='shandong'\
            or province=='guangdong' or province=='heilongjiang' or province=='beijing' or province=='fujian' or province=='hebei' or province=='guangxi'or province=='shanxi'\
          or province=='liaoning' or province=='shanxi1'or province=='tianjin' \
            or province=='neimeng'  or province=='gansu' or province=='ningxia' \
            or province=='qinghai' or province=='xizang':
        # city_name = city[2:len(city)]
        # city_data = city_data[6:len(city_data):6]
        # print('*'*100)
        for i in city:
            if '区' in i or '县' in i or '盟' in i:
                city_name.append(i)
                # print('*' * 100)
                continue

            elif i =='大兴安岭':
                city_name.append('大兴安岭地区')
                continue
            elif i=='恩施州':
                city_name.append('恩施土家族苗族自治州')
                continue
            elif i =='湘西自治州':
                city_name.append('湘西土家族苗族自治州')
                continue
            else:
                city_name.append("".join([i, "市"]))
        city_name = city_name[2:len(city_name)]
        city_data = city_data[6:len(city_data):6]
    # city_name = city_name[4:len(city_name)]
    # city_data = city_data[7:len(city_data):6]
    elif province=='henan':
        for i in city:
            if '区' in i:
                city_name.append(i)
                continue
            elif i=='恩施州':
                city_name.append('恩施土家族苗族自治州')
                continue
            else:
                city_name.append("".join([i, "市"]))
        city_name = city_name[4:len(city_name)]
        city_data = city_data[7:len(city_data):6]
    elif province=='chongqing':
        for i in city:
            if  i =='石柱县':
                city_name.append('石柱土家族自治县')
                continue
            elif i =='彭水县':
                city_name.append('彭水苗族土家族自治县')
                continue

            elif i =='酉阳县':
                city_name.append('酉阳土家族苗族自治县')
                continue
            elif i =='秀山县':
                city_name.append('秀山土家族苗族自治县')
                continue
            elif i =='梁平区':
                city_name.append('梁平县')
                continue
            elif '区' in i or '县' in i:
                city_name.append(i)
                continue
            elif i=='恩施州':
                city_name.append('恩施土家族苗族自治州')
                continue
            elif i =='湘西自治州':

                city_name.append('湘西土家族苗族自治州')

            else:
                city_name.append("".join([i, "市"]))
        city_name = city_name[2:len(city_name)]
        city_data = city_data[6:len(city_data):6]
    elif province == 'sichuan':
        for i in city:
            if i == '甘孜州':
                city_name.append('甘孜藏族自治州')
                continue
            elif i == '阿坝州':
                city_name.append('阿坝藏族羌族自治州')
                continue

            elif i == '凉山州':
                city_name.append('凉山彝族自治州')
                continue

            elif '区' in i or '县' in i :
                city_name.append(i)
                continue
            else:
                city_name.append("".join([i, "市"]))
        city_name = city_name[2:len(city_name)]
        city_data = city_data[6:len(city_data):6]
    elif province=='shanghai':
        city_name=city[6:len(city)]
        city_data=city_data[13:len(city_data):6]
    elif  province=='yunnan':
        for i in city:
            if i=='红河州':
                city_name.append('红河哈尼族彝族自治州')
                continue
            elif i=='大理州':
                city_name.append('大理白族自治州')
                continue
            elif i=='德宏州':
                city_name.append('德宏傣族景颇族自治州')
                continue
            elif i =='楚雄州':
                city_name.append('楚雄彝族自治州')
                continue
            elif i =='文山州':
                city_name.append('文山壮族苗族自治州')
                continue
            elif i=='西双版纳':
                city_name.append('西双版纳傣族自治州')
                continue
            else:
                city_name.append(''.join([i,"市"]))

        city_name = city_name[2:len(city_name)]
        city_data = city_data[6:len(city_data):6]
    elif province == 'hainan':
        for i in city:
            if i=='定安' or i =='屯昌' or i == '澄迈' or i =='临高':
                city_name.append(''.join([i,'县']))
                continue
            elif i =='昌江':
                city_name.append('昌江黎族自治县')
                continue
            elif i =='乐东':
                city_name.append('乐东黎族自治县')
                continue
            elif i =='琼中':
                city_name.append('琼中黎族苗族自治县')
                continue
            elif i=='保亭':
                city_name.append('保亭黎族苗族自治县')
                continue
            elif i =='陵水':
                city_name.append('陵水黎族自治县')
                continue
            else:
                city_name.append(''.join([i, '市']))
        city_name = city_name[2:len(city_name)]
        city_data = city_data[6:len(city_data):6]
    elif  province=='guizhou':
        # print('*'*100)
        for i in city:
            if i == '黔西南州':
                city_name.append('黔西南布依族苗族自治州')
                continue
            elif i == '黔南州':
                city_name.append('黔南布依族苗族自治州')
                continue
            elif i == '黔东南州':
                city_name.append('黔东南苗族侗族自治州')
                continue
            else:
                city_name.append(''.join([i, '市']))
        city_name = city_name[2:len(city_name)]
        city_data = city_data[6:len(city_data):6]
    elif province == 'jilin':
        # print('*'*100)
        for i in city:
            if i == '延边':
                city_name.append('延边朝鲜族自治州')
                continue

            elif '市' in i:
                city_name.append(i)
                continue
            else:
                city_name.append(''.join([i, '市']))
        city_name = city_name[2:len(city_name)]
        city_data = city_data[6:len(city_data):6]

    # print("最近传入数据",city_data)
    # print("最后城市",city_name)
    # print(dict[province].strip('省'))
    g = (
        Map(init_opts=opts.InitOpts(width = '1440px', height='800px'))
            .add(dict[province]+"疫情地图", [list(z) for z in zip(city_name, city_data)], maptype=dict1[province],is_map_symbol_show=False,itemstyle_opts=opts.ItemStyleOpts(color="#ede586"),)
            # .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"),
            .set_global_opts(
            # title_opts=opts.TitleOpts(title="Map-基本示例"),
                             visualmap_opts=opts.VisualMapOpts(
                                 # max_=city_data[0],
                                 #                            range_color=['#FDEBCF','#F59E83','#E55A4E','#CB2A2F','#811C24','#4F070D'],split_number=6,is_piecewise=True,
                                 is_piecewise=True,
                                 # range_color=['#FDEBCF','#F59E83','#E55A4E','#CB2A2F','#811C24','#4F070D'],split_number=6,is_piecewise=True,
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
    # print('templates_map/'+province+'.html')
    g.render(path='templates/templates_map/'+province+'.html',template_name='mapmodel.html')
def drewindex():
    html = getepodemicdata()
    city_data1 = []
    city_name=[]
    for value in dict.values():
        if value != '西藏自治区':
            regular = '(\{\\\"provinceName"\:\\\"' + value + '\\\"\,\\\"provinceShortName\\\".+?\{\\\"provinceName\\\")'

        else:
            regular = '(\{\\\"provinceName"\:\\\"' + value + '\\\"\,\\\"provinceShortName\\\".+?\\}\\]\\}\\]\\})'
        data_json = re.findall(re.compile(regular), str(html))
        # print(data_json)
        #
        # print(len(city_data))
        # print(city_data)
        # if len(city_data) == 0:
        #     print(value + "!!!!!!!!!!!!!!!!!!!!!!")
        #     continue
        # print(city_data[0])
        city_data = re.findall(re.compile(r'(\d+)'), str(data_json))
        city_data1.append(city_data[0])
        city_data2=[int(i) for i in city_data1]

    # print(city_data1)
    # print(dict1.values())
    g = (
            Map(init_opts=opts.InitOpts(width = '1440px', height='800px'))

                .add("中国疫情地图", [list(z) for z in zip(dict1.values(), city_data1)], maptype="china",is_map_symbol_show=False,itemstyle_opts=opts.ItemStyleOpts(color="#ede586"),is_roam=False)
                # .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"),
                .set_global_opts(
                # title_opts=opts.TitleOpts(title="Map-基本示例"),
                                 visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                                # range_color=['#FDEBCF','#F59E83','#E55A4E','#CB2A2F','#811C24','#4F070D'],split_number=6,is_piecewise=True,
                                                                   pieces=[{"min": 0, "max": 0, "label": "0",
                                                                            "color": "#FFFFFF"},
                                                                           {"min": 1, "max": 9, "label": "1-9",
                                                                            "color": "#FDEBCF"},
                                                                           {"min": 10, "max": 99, "label": "10-99",
                                                                            "color": "#F59E83"},
                                                                           {"min": 100, "max": 499, "label": "100-499",
                                                                            "color": "#E55A4E"},
                                                                           {"min": 500, "max": 999, "label": "500-999",
                                                                            "color": "#CB2A2F"},
                                                                           {"min": 1000, "max": 10000, "label": "1000-10000",
                                                                            "color": "#811C24"},
                                                                           {"min": 10001, "max": 10000000000, "label": "> 10000",
                                                                            "color": "#4F070D"}],
                                                                   ),


                                 )
        )
    # print('emplates_map/index.html')

    g.render(path='templates/templates_map/index.html',template_name='mapmodel.html')
# Create your views here.
def index(request):
    # print("中国")
    drewindex()
    return render(request,'templates_map/index.html')

def provincemap(request):
    # html= getepodemicdata()
    # print("省")
    pro=request.GET.get('province')
    drawmap(pro)
    return  render(request,'templates_map/'+pro+'.html')
def xinjiang(request):
    html = getepodemicdata()
    province = request.GET.get('province')
    if province != '西藏自治区':
        regular = '(\{\\\"provinceName"\:\\\"' + dict[
            province] + '\\\"\,\\\"provinceShortName\\\".+?\{\\\"provinceName\\\")'

    else:
        regular = '(\{\\\"provinceName"\:\\\"' + dict[province] + '\\\"\,\\\"provinceShortName\\\".+?\\}\\]\\}\\]\\})'
    data_json = re.findall(re.compile(regular), str(html))
    # print(regular)
    # regular=r'(\{\"provinceName"\:\"{}省\"\,\"provinceShortName\".+?\{\"provinceName\")'.format(province)
    data_json = re.findall(re.compile(regular), str(html))
    # print(data_json)
    city_data = re.findall(re.compile(r'(\d+)'), str(data_json))
    data=city_data[0]
    return render(request, 'templates_map/errormap.html', {'data':data,'province':dict[province]})
def error(request):
    return render(request,'templates_map/404.html')