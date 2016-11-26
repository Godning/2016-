# -*- coding:utf-8 -*-
'''
Created on 2016-11-23

@author: Godning
'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
#pagerank
from numpy import *

m = mat([[0,1,1],[0,0,0],[0,0,0]])

pr = mat([[1],[1],[1]])

for i in range(100):
    pr = 0.15 + 0.85 * m * pr
    print i
    print pr
"""
import jieba,codecs,math

text = u"近日，一直以“携程挑战者”形象存在的美团酒店，遭遇了携程的强力反击。携程日前举办首届全球酒店合作伙伴峰会，" \
       u"吸引了众多酒店行业领袖参会，意在向美团“秀肌肉”。事实上，不止面临携程“亮牙齿”，美团酒店早已陷入困局中难以自拔。一方面，" \
       u"它至今仍陷巨亏泥潭，而核心的中低星酒店业务又被去哪儿全面超越。另一方面，中低星酒店市场失守后，美团试图进军高星酒店市场，" \
       u"却被频频爆出存价格欺诈现象，侵犯消费者利益。互联网进入“下半场”，美团酒店业务被拆分并进行独立融资的消息传的沸沸扬扬，" \
       u"或许卖身帮美团“输血”已是其最终的命运。中低星酒店市场溃败 美团酒店盈利系伪命题近几年，美团酒店一直喜欢用“晒成绩”的方式刷存在感，" \
       u"刚过去不久的国庆黄金周显然也不例外。美团官方口径称，10月1日当天，入住间夜量突破80万。不过，这一次却被对手用数据打脸。" \
       u"去哪儿网COO张强发布内部信称，国庆长假期间，去哪儿网十一单日离店有效间夜量超过100万。同时，百度糯米十月一日当天间夜增幅接近350%，" \
       u"交易额近亿元。此外，十一期间百度糯米酒店客单价为280元，远远超过美团的189元。值得注意的是，美团酒店以中低端酒店为主，" \
       u"但这一起家业务悄然落败。张强的内部信透露，去哪儿网不仅占据中低星酒店市场第一，还实现了季度盈利，给了美团当头一棒。要知道，" \
       u"美团酒店此前宣称，在中低星酒店市场占据上风。针对美团培养的价格敏感型消费者，去哪儿网开打“价格战”，返现力度、" \
       u"价格均比美团更有优势，全力争夺用户。更致命的是，知名经济型酒店纷纷抵制美团，使得美团遭受釜底抽薪式打击。有记者调查发现，" \
       u"包括汉庭、7天、如家、锦江之星等在内的经济型酒店取消了与美团合作，从美团下线门店数量近3000家，何时恢复不得而知。" \
       u"业内人士透露，美团酒店团购模式扰乱价格体系，是合作中断的主因。面对竞争对手的强势进攻，美团酒店只能继续“烧钱”守住阵地。" \
       u"一边是烧钱根本停不下来，一边是低至6%的佣金水平，再加上被知名经济型酒店“抛弃”，引发用户大规模流失，美团酒店实现盈利的说辞不攻自破。" \
       u"价格欺诈被曝光 进军高端酒店被阻击美团酒店在中低星市场的优势被打破后，又高调宣布进入利润丰厚的高星酒店市场，企图从中分一杯羹。" \
       u"按照美团官方说法，目前平台上合作高星酒店数量便已经超过1万家，增速高达60%。实际情况是，高星酒店成了美团的取款机，" \
       u"随意加价销售是惯用伎俩，疯狂收割用户。据媒体报道，今年10月份，杭州市民王小姐通过美团网团购了当地香格里拉的一间房间，" \
       u"不仅比携程、途牛等网站贵了400到600元，甚至比直接在酒店前台预订还要高出200元。无独有偶，武汉等地多位消费者也有同样经历，" \
       u"纷纷投诉美团价格欺诈。有记者调查发现，在北京、上海、成都、杭州等热门旅游城市，部分美团高星酒店价格比携程、艺龙、去哪儿以及同程等在线旅游网站高出20%左右，" \
       u"平均价差在100元以上。由于不满美团存在欺诈消费者行为，并且未建立起服务体系，国内部分高星酒店集团旗下的大多数酒店从美团酒店频道下线。" \
       u"其中一家酒店负责人表示，他们注重消费者的服务体验，已选择更靠谱的在线旅游平台进行合作。对于入驻美团，高星酒店品牌仍持谨慎态度。" \
       u"美团频频被合作伙伴“抛弃”，与竞争对手差距越拉越大。9月至今，携程先后与国内数千家酒店签署“总经销协议”，共同打造新型酒店生态圈，" \
       u"获得更多高星酒店认可。这些酒店加入携程“战队”，相当于给予携程在线上销售方面的优先权，凸显了其对上游资源掌控能力。" \
       u"举办首届全球酒店合作伙伴峰会，更展示了携程强大的朋友圈。这也表明，携程正不断巩固高星酒店市场领先地位，加速围剿美团这一新的竞争者，" \
       u"彻底打消美团进入这一市场的企图。中低星市场失利，高星市场难以进入，美团酒店陷入进退两难困境。值得关注的是，长期巨亏的美团，" \
       u"已从规模导向转到盈利导向，不会再容忍酒店业务烧钱“抢市场”。由此来看，美团酒店未来去向已注定，或将走上猫眼电影的老路，缓解美团缺钱的燃眉之急"

stop_words_file = "stopwords.txt"
stop_words = []

for word in codecs.open(stop_words_file, 'r', 'utf-8', 'ignore'):
    stop_words.append(word.strip())

sentences = text.split(u'。')
seg_list = []
for item in sentences:
    seg_list.append([word for word in jieba.cut(item, cut_all=False) if word not in stop_words])
    #seg_list.append(jieba.cut(item, cut_all=False))
for i in range(len(seg_list)):
    print "Result "+str(i+1)+" : ", "/ ".join(seg_list[i])

def sen_similarity_calc(seg_list):
    w = []
    for i in range(len(seg_list)):
        w.append([])
        for j in range(len(seg_list)):
            common = [word for word in seg_list[i] if word in seg_list[j]]
            ans = len(common) / (math.log(len(seg_list[i]))+math.log(len(seg_list[j])))
            if ans>0.6:
                w[i].append(1)
            else:
                w[i].append(0)
    return w

w = sen_similarity_calc(seg_list)

for i in range(len(w)):
    for j in range(len(w[i])):
        print w[i][j],' ',
    print

from numpy import *

m = mat(w)

pr = []
for i in range(len(w)):
    pr.append([1])
pr = mat(pr)
for i in range(100):
    pr = 0.15 + 0.85 * m * pr

print pr