# 常见问题

## 远程连接
- 远程的terminal中的环境变量无法重置
    - 原因：远程的vscode服务未能重启导致，需要手动关闭远程vscode服务
    - Ctrl+Shift+P, 选择Remote-SSH: Kill VS Code server on Host...
- 无法启动远程的vs server
    - 原因：远程网络不好，无法下载server; 或~/.vscode-server/ 下存在多个安装包，版本与本机不一致
    - 连接远程网络，删除~/.vscode-server/下的安装包，重新ssh连接

## 自动换行
- 方法一：Alt+z, 切换自动换行
- 方法二：preferences->settings->Word Wrap->on, 修改默认值为自动换行开，需要时用Alt+z， 关闭自动换行。

