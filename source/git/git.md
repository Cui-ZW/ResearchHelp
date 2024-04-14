# Git 使用快捷操作

## 提交commit消失的补救方法
有时候误操作，在git graph 会缺失commit信息
- 解决方法：
    1. git reflog 查看记录，选择对应commit的hashid
    2. git reset --hard xxxxx
