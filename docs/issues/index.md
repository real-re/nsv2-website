---
title: 问题汇总
---

> 已知问题为目前已经确认的问题或bug，问题列表如下所示，
> 如有新问题，请点击群里`在线文档`内的`反馈文档`进行反馈。
>
> 或你对哪条问题有疑义或补充，请在群里`@Re`或在`反馈文档`中对应问题的编号后写下补充描述。
>
> 反馈的具体格式参考下面的`反馈问题格式`。

???+ note "反馈问题格式"

    反馈问题，如涉及到战斗逻辑，应描述如下信息：

        1. 游戏模式（如果在进入彩蛋后的模式出现问题，应特殊标注）

        2. 对局角色：主要为你操作的角色（若受其他角色影响，应记录相应角色名）

        3. 

    如问题难以描述，最好发送一段视频到V2群里，并`@Re`

    如UI或贴图产生偏移、错位等问题，最好提供错误时的截图以及简要描述。

    如音效或其他问题，简要描述问题即可。

    做好反馈描述，不仅有利于开发者进行定位修复，
    也利于其他遇到相似问题的玩家参考和进行补充。

??? note "标签说明"

    :material-check:：表示此问题或bug已经解决。

    <font color=#448aff>【非BUG】</font>：此问题非bug。

    <font color=#C2185B>【已复原BUG🐛】</font>：此bug已被开发者复原，可以更快的进行定位修复。

    <font color=#FF5252>【:material-close:待修复】</font>：等待下一版本进行修复。

    <font color=#E64A19>【待排查】</font>：此问题等待开发者排查中。

    【xx待完善】：xx需要后续完善。

    【反馈描述待完善】：需要提问者增加更详细描述信息或图片。

    【未知】：不明原因。

## v2.1.0 已知问题

!!! question "1. 选人界面人物语音播放不完全，像是被掐断一样"

    <font color=#448aff>【非BUG】</font>
    【音频待完善】

    旧版音频素材问题，以前为了优化音频占用内存，部分音频有分割掉最后一部分。

!!! question "2. 安装包名不是旧版，而是共存，这样会让很多玩家丢失存档，并且失去情怀"

    【非稳定版本开发考虑】

    后续数据存储方式也可能会变，数据无法兼容

!!! question "3. 模式选择界面UI未应用，很久之前就做好了"

    【UI待完善】

    低分辨率向高分辨率，不能直接应用，UI缩放需要调整。

!!! question "4. 整体移动速度变慢了，玩起来手感很黏，感觉什么都很迟钝"

    <font color=#448aff>【非BUG】</font>
    【数值待完善】

    原版游戏移动速度并非固定，屏幕越宽速度越快，现在需要取一个相近的数值。

!!! question "5. BGM会出现重叠问题"

    <font color=#E64A19>【待排查】</font>

!!! bug "6. 结算时会闪退（部分情况为暂停游戏或切至后台过一段时间再加入）"

    <font color=#FF5252>【:material-close:待修复】</font>

!!! question "7. 移动时会有停顿现象"

    【反馈描述待完善】

    目前仅测试出阿飞技能会导致移动中断，部分角色可能也会导致此问题。

    应继续补充其他产生此问题角色。

!!! bug "8. 水门飞雷神不突进问题"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

    经测试，仅在克隆模式下，敌人就在眼前，但还是原地释放螺旋丸。

    备注：此类问题应该只会发生在克隆模式下，拥有相似功能的角色大部分未适配克隆模式，

    所以会导致结算、跟踪等特殊的操作出现问题。

    如有特殊情况，请补充详细描述。

!!! bug "9. 角都奥义2无法使用，角都奥义1能用，就是放不出面具怪"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

    奥义1需要有`心`，为零是无法召唤面具怪。
    奥义2是被动，但奥义2技能图标UI表现待优化。

    经测试并无无法召唤面具怪等问题。

    如果不属于以上情况，请继续反馈。

!!! success "10. 忍具购买不显示"

    重复问题，见# 13。

!!! success "11. 拉面回血和被攻击掉时没有过渡动画，瞬间提高降低，非常突兀"

    <font color=#448aff>【非BUG】</font>
    【UI待完善】

!!! bug "12. 经典3v3自由选队友请回调为默认，彩蛋状态下UI错位问题"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

    补充：彩蛋下的3v3和4v4均有UI问题，3v3两个UI问题。

!!! success "13. 不显示新三件忍具的问题"

    未做完的，所以又移除了。

!!! bug "14. 角色在主塔范围内无法触发自动回血"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

!!! success "15. 迪达拉技能1 飞鸟只攻击塔和忍者，不攻击小兵"

    该技能有优先等级，默认攻击塔和忍者，一直是这样的。

!!! question "16. 伤害溢出与判定问题"

    <font color=#E64A19>【待排查】</font>

!!! question "17. 电脑鸣人开奥义二之后不动的问题"

    <font color=#E64A19>【待排查】</font>

    相似问题# 53。

!!! question "18. 金鸣奥义二九喇嘛攻击塔的问题"

    <font color=#E64A19>【待排查】</font>

!!! bug "19. 游戏过程中点击地图或其他非战斗ui闪退"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

    经测试，有几率导致该bug，排查后可能是引擎问题。

!!! failure "20. 【未知】部分机型黑屏问题"

    【反馈描述待完善】

    请补充下机型和版本号。

!!! bug "21. 纲手奥义二无限回血问题"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

    经测试，释放奥义2后，将在较长的时间内一直处于回血状态。

!!! question "22. 纲手站立普攻自动为穿着火影袍，释放技能时为普通状"

    <font color=#448aff>【非BUG】</font>
    【素材待修复】

    素材原因，来自源码的部分素材和以前不一样，纲手只有14帧攻击是不一样的。

!!! success "23. 选人界面背景与人物框内颜色不一致"

    注意：当本模式可以自选角色时，为红色背景。

!!! question "24. 千代奥义一查克拉buff永久存在"

    <font color=#E64A19>【待排查】</font>

!!! question "25. 香磷奥义一回血buff永久存在"

    <font color=#E64A19>【待排查】</font>

!!! question "26. 复活时间不随等级增长"

    <font color=#E64A19>【待排查】</font>

!!! question "27. AI水门技能1无冷却问题"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

    经测试，AI小南也由此问题。

    可能其他角色均有此问题，如有请在# 27后进行补充。

!!! question "28. 克隆模式经验金币等资源获取有问题"

    <font color=#E64A19>【待排查】</font>

!!! question "29. 电脑长门可以重复使用奥义二"

    <font color=#E64A19>【待排查】</font>

!!! question "30. 忍术大全觉醒后失效"

    <font color=#E64A19>【待排查】</font>

!!! success "31. 克隆模式会出现4个人"

    唯一的彩蛋被你发现了。

!!! success "32. 结算界面显示不完全，结算界面UI错误"

    【UI待完善】

    部分模式不会显示完全，UI设计有问题。

!!! question "33. 小樱1VS1里面也是无限回血"

    <font color=#448aff>【非BUG】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

    尚未修改技能时长，现在的技能持续时间过长，一直放技能，导致近似无限回血。

!!! bug "34. 阿飞放3技能虚化后走路时走一下又停一下，就像断触一样"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

!!! bug "35. 鹿丸3技能（和奥义2）命中敌人时不会连续造成伤害，只有命中敌人那一下有伤害"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

!!! bug "36. (1)心转身状态下的井野会自己吃拉面回血，(2)如果心转身提前结束会有ai操作井野"

    1. <font color=#FF5252>【:material-close:待修复】</font>

    2. <font color=#FF5252>【:material-close:待修复】</font>

!!! question "37. 小樱的三技能怪力模式没有效果"

    <font color=#E64A19>【待排查】</font>

!!! success "38. 勘九郎奥义1和奥义2的召唤物会消失（3s内）"

    优化角色配置时，没有适配此类角色，通灵类忍者潜在问题，如有其他相似忍者请继续补充。

!!! question "39. 水门二技能飞雷神第二段原地放螺旋丸打中了也没伤害"

    <font color=#E64A19>【待排查】</font>

!!! success "40. 角色释放奥义2没有语音"

!!! question "41. 选人界面君麻吕没有语音"

    <font color=#448aff>【非BUG】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

    一直没做音效。

!!! bug "42. 游戏开始时可以偷跑，在战斗开始文字出现时可以放技能"

    <font color=#FF5252>【:material-close:待修复】</font>

    此问题仅在特定类型技能下发生。

!!! bug "43. 长门轮回天生之术释放成功的瞬间被打死可以自己复活自己"

    <font color=#FF5252>【:material-close:待修复】</font>

!!! question "44. 长门二技能技能描述文本出错"

    【技能描述待完善】

!!! failure "45. 华为 系统安卓9 进入游戏黑屏无反应"

    【未知】

    这种很棘手，多半就是华为的问题吧。

!!! question "46. 1v1阿斯玛奥义2烧死不给钱"

    <font color=#E64A19>【待排查】</font>

!!! question "47. 僵直效果需要调整"

    【反馈描述待完善】

!!! question "48. (1)香磷奥二抓取效果不生效，(2)奥义一特效贴图异常"

    1. 此技能非所有状态的角色都有效

    2. <font color=#E64A19>【待排查】</font>

!!! question "49. 第四张地图上方会有一条像素线"

    <font color=#FF5252>【:material-close:待修复】</font>

    为了修复地图黑线问题（引擎问题），所有地图相关的图块都需要加1像素延展，此地图图块的位置有些冲突。

!!! success "50. 刚进出装页面的时候点速走鞋没有音效"

    这个因为默认选择就是第一个装备，所以你再选择他也没有播放音频的意义。

!!! question "51. 有时结算页面塔的位置会出现贴图异常"

    <font color=#E64A19>【待排查】</font>

!!! question "52. 很多角色技能后面都多一段硬直"

    <font color=#E64A19>【待排查】</font>

!!! bug "53. 1v1模式AI角色，开局后很长一段时间不动（或者AI在两边有时不会移动）"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

!!! question "54. 千代奶奶克隆模式奥义一不生效。"

    <font color=#E64A19>【待排查】</font>

!!! bug "55. 金鸣二技能影分身之术EX召唤出来的是九喇嘛"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

    原本是金鸣分身。

!!! question "56. 小李开到杜门之后移动时会有停顿现象"

    <font color=#E64A19>【待排查】</font>

    相似问题# 7。

!!! question "57. 队友击杀敌人之后自己不会增加金币和经验收益"

    <font color=#E64A19>【待排查】</font>

!!! bug "58. 勘九郎死亡后某些情况导致程序崩溃"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

    拥有通灵、召唤类技能的角色可能存在此问题，如有相似请补充。

!!! bug "59. 不断暂停恢复游戏后，bgm没有播放完还会进行切换"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

!!! bug "60. 游戏结算时，在右侧会出现绿色长条贴图"

    <font color=#E64A19>【待排查】</font>

---

## FAQ（常见问题）

!!! warning "施工中ing..."


