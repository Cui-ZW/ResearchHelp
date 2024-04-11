# 常见问题

## 远程连接
- 远程的terminal中的环境变量无法重置
    - 原因：远程的vscode服务未能重启导致，需要手动关闭远程vscode服务
    - Ctrl+Shift+P, 选择Remote-SSH: Kill VS Code server on Host...

## 自动换行
- 方法一：Alt+z, 切换自动换行
- 方法二：preferences->settings->Word Wrap->on, 修改默认值为自动换行开，需要时用Alt+z， 关闭自动换行。