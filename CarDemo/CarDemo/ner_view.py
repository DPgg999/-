# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
 
import sys
sys.path.append("..")
from toolkit.pre_load import thuFactory,neo4jconn,domain_ner_dict
from toolkit.nlp_ner import get_ner,tempword,get_detail_ner_info,get_ner_info
from Model.neo4j_models import Neo4j_Handle
from toolkit.pre_load import thuFactory,neo4jconn,domain_ner_dict


#中文分词+词性标注+命名实体识别
def ner_post(request):
	ctx ={}
	db = neo4jconn

	if request.POST:
		#获取输入文本
		key = request.POST['user_text']
		thu1 = thuFactory
		#中文分词:提前移除空格
		key = key.strip()
		TagList = thu1.cut(key, text=False)
		text = ""
		#命名实体识别
		ner_list = get_ner(key)
		#遍历输出
		for pair in ner_list:
			if pair[1] == 0:
				text += pair[0]
				continue
			if tempword(pair[1]):
				text += "<a href='#'  data-original-title='" + get_ner_info(pair[1]) + "(暂无资料)'  data-placement='top' data-trigger='hover' data-content='"+get_detail_ner_info(pair[1])+"' class='popovers'>" + pair[0] + "</a>"
				continue


			#添加查库 返回实体识别结果和汽车地址
			herfs = ''
			data = db.matchEntityItem(pair[0])

			herfs = data[0].get("Car")['cars_addr']

			print(pair[0],herfs)

			try:
				text += "<a href= " + herfs + "  data-original-title='" + get_ner_info(
					pair[1]) + "'  data-placement='top' data-trigger='hover' data-content='" + get_detail_ner_info(
					pair[1]) + "' class='popovers'>{友情链接}" + pair[0] + "</a>"
			except:
				continue
		ctx['rlt'] = text
			
		seg_word = ""
		length = len(TagList)
		#设置显示格式
		for t in TagList:
			seg_word += t[0]+" <strong><small>["+t[1]+"]</small></strong> "
		seg_word += ""
		ctx['seg_word'] = seg_word

	return render(request, "index.html", ctx)
