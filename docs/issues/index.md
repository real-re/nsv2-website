---
title: 问题汇总
---

## v2.1.0 已知问题

> v2.1.0版本目前已知的问题列表如下所示，如有新问题，请点击群里`在线文档`内的`反馈文档`进行反馈。
> 
> 如果问题难以描述且无法用图片表达，请录制视频发送至V2群里并`@Re`。
> 
> 如果你对哪条问题有疑义，请在群里`@Re`或在`反馈文档`中对应问题的编号后写下补充描述。

??? note "标签说明"

    <font color=green>【:material-check:已解决】</font>：此问题或BUG已经解决。

    <font color=#448aff>【非BUG】</font>：此问题非bug。

    <font color=#C2185B>【已复原BUG🐛】</font>：此bug已被开发者复原，可以更快的进行定位修复。

    <font color=#FF5252>【:material-close:待修复】</font>：等待下一版本进行修复。

    <font color=#E64A19>【待排查】</font>：此问题等待开发者排查中。

    【xx待完善】：xx需要后续完善。

    【反馈描述待完善】：需要提问者增加更详细描述信息或图片。

    【未知】：不明原因。

!!! question "1. 选人界面人物语音播放不完全，像是被掐断一样"

    <font color=#448aff>【非BUG】</font>
    【音频待完善】

    旧版音频素材问题。

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

    目前仅测试出阿飞技能会导致移动中断，应补充详细描述。

!!! bug "8. 水门飞雷神不突进问题"

    <font color=#FF5252>【:material-close:待修复】</font>

    备注：此类问题应该只会发生在克隆模式下，拥有相似功能的角色大部分未适配克隆模式，

    所以会导致结算、跟踪等特殊的操作出现问题。

    如有特殊情况，请补充详细描述。

!!! bug "9. 角都奥义无法使用，角都奥义一能用，就是放不出小黑（面具怪）"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

    合并相似问题，奥义二是被动，奥义二技能图标表现待优化。

!!! question "10. 忍具购买不显示"

    <font color=#E64A19>【待排查】</font>

!!! success "11. <font color=green>【:material-check:已解决】</font>拉面回血和被攻击掉时没有过渡动画，瞬间提高降低，非常突兀"

    <font color=#448aff>【非BUG】</font>
    【UI待完善】

!!! bug "12. 经典3v3自由选队友请回调为默认，彩蛋状态下UI错位问题"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

    补充：彩蛋下的3v3和4v4均有UI问题，3v3两个UI问题。

!!! success "13. <font color=green>【:material-check:已解决】</font>不显示新三件忍具的问题"

    未做完的，所以又移除了。

!!! question "14. 【未知】血池不回血问题"

    <font color=#E64A19>【待排查】</font>

    停止移动每隔几秒会有几百点HP回复，如果出现异常，请补充对局角色、模式、和阵营。

!!! success "15. <font color=green>【:material-check:已解决】</font>迪达拉技能一飞鸟只攻击塔和忍者，不攻击小兵问题"

    有优先等级，默认攻击塔和忍者，一直是这样的。

!!! question "16. 伤害溢出与判定问题"

    <font color=#E64A19>【待排查】</font>

!!! question "17. 电脑鸣人开奥义二之后不动的问题"

    <font color=#E64A19>【待排查】</font>

!!! question "18. 金鸣奥义二九喇嘛攻击塔的问题"

    <font color=#E64A19>【待排查】</font>

!!! question "19. 游戏过程中点击地图或其他非战斗ui闪退"

    <font color=#E64A19>【待排查】</font>

!!! failure "20. 【未知】部分机型黑屏问题"

    【反馈描述待完善】

    请补充下机型和版本号。

!!! success "21. <font color=green>【:material-check:已解决】</font>纲手奥义二无限回血问题"

    奥义时间一过就是普通状态栏，此技能特色。

!!! question "22. 纲手站立普攻自动为穿着火影袍，释放技能时为普通状"

    <font color=#448aff>【非BUG】</font>
    【素材待修复】

    素材原因，来自源码的部分素材和以前不一样，纲手只有14帧攻击是不一样的。

!!! success "23. <font color=green>【:material-check:已解决】</font>选人界面背景与人物框内颜色不一致"

    注意：当本模式可以自选角色时，为红色背景。

!!! question "24. 千代奥义一查克拉buff永久存在"

    <font color=#E64A19>【待排查】</font>

!!! question "25. 香磷奥义一回血buff永久存在"

    <font color=#E64A19>【待排查】</font>

!!! question "26. 复活时间不随等级增长"

    <font color=#E64A19>【待排查】</font>

!!! question "27. 电脑水门技能一无冷却问题"

    <font color=#E64A19>【待排查】</font>

!!! question "28. 克隆模式经验金币等资源获取有问题"

    <font color=#E64A19>【待排查】</font>

!!! question "29. 电脑长门可以重复使用奥义二"

    <font color=#E64A19>【待排查】</font>

!!! question "30. 忍术大全觉醒后失效"

    <font color=#E64A19>【待排查】</font>

!!! success "31. <font color=green>【:material-check:已解决】</font>克隆模式会出现4个人"

    唯一的彩蛋被你发现了。

!!! success "32. <font color=green>【:material-check:已解决】</font>结算界面显示不完全，结算界面UI错误"

    【UI待完善】

    合并相似问题，部分模式不会显示完全，UI设计有问题。

!!! question "33. 小樱1VS1里面也是无限回血"

    <font color=#448aff>【非BUG】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

    尚未修改技能时长，时间太长一直放技能，导致无限回血。

!!! bug "34. 阿飞放3技能虚化后走路时走一下又停一下，就像断触一样"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

!!! bug "35. 鹿丸3技能（和奥义2）命中敌人时不会连续造成伤害，只有命中敌人那一下有伤害"

    <font color=#C2185B>【已复原BUG🐛】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

!!! question "36. 心转身状态下的井野会自己吃拉面回血，如果心转身提前结束会有ai操作井野"

    <font color=#E64A19>【待排查】</font>

!!! question "37. 小樱的三技能怪力模式没有效果"

    <font color=#E64A19>【待排查】</font>

!!! question "38. 堪九郎奥义一二技能的召唤物会消失"

    <font color=#E64A19>【待排查】</font>

!!! question "39. 水门二技能飞雷神第二段原地放螺旋丸打中了也没伤害"

    <font color=#E64A19>【待排查】</font>

!!! question "40. 进入战斗时角色开大招没有语音"

    <font color=#E64A19>【待排查】</font>

!!! question "41. 选人界面君麻吕没有语音"

    <font color=#448aff>【非BUG】</font>
    <font color=#FF5252>【:material-close:待修复】</font>

    一直没做音效。

!!! bug "42. 游戏开始时可以偷跑，在战斗开始文字出现时可以放技能"

    <font color=#FF5252>【:material-close:待修复】</font>

    此问题应该仅出现于键盘操作的情况下。

!!! bug "43. 长门轮回天生之术释放成功的瞬间被打死可以自己复活自己"

    <font color=#FF5252>【:material-close:待修复】</font>

!!! question "44. 长门二技能技能描述文本出错"

    【UI待完善】

!!! failure "45. 华为 系统安卓9 进入游戏黑屏无反应"

    【未知】

    这种很棘手，多半就是华为的问题吧。

!!! question "46. 1v1阿斯玛奥二烧死不给钱"

    <font color=#E64A19>【待排查】</font>

!!! question "47. 僵直效果需要调整"

    【反馈描述待完善】

!!! question "48. (1)香磷奥二抓取效果不生效，(2)奥义一特效贴图异常"

    1. 此技能非所有状态的角色都有效

    2. <font color=#E64A19>【待排查】</font>

---

## FAQ（常见问题）

!!! warning "施工中ing..."


