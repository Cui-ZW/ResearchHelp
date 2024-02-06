# 常见问题

## 远程连接
- 远程的terminal中的环境变量无法重置
    - 原因：远程的vscode服务未能重启导致，需要手动关闭远程vscode服务
    - Ctrl+Shift+P, 选择Remote-SSH: Kill VS Code server on Host...