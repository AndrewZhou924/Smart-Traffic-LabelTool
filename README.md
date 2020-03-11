# 车道线数据标注说明

*AI组 Zhanke Zhou*

------

### 打标工具使用方法

- 将待标注图片文件夹重命名为src，放在`label.py`同一路径下
- 在终端输入`python3 label.py`
  - 会显示每张待标注图片，并在终端提示一共还剩余多少张图片待标注
- 根据每张图片的情况进行判断
  - 若存在违规，则输入y
  - 若没有违规，则输入n
  - 若图片受损或无法看清，则输入o
  - 若上一张图片输入有误，按z进行撤回
- 中途退出程序 输入q
- 打标的结果保存在`output`文件夹中
- 注意：
  - 需针对某一类违规情况做二分类标注，如压线或逆行，暂不支持对两种及以上违规情况做同时标注
    - 通俗来讲，便是一次只可以对一种数据集进行打标
  - 标注前，请仔细查看打标的标准

### 运行环境

- python3
- opencv-python

### 问题反馈

- 请提 Issue
- 或联系 andrewzhou924@qq.com

### TODO

- [ ] 支持多标签标注