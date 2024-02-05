# GitHub 常见问题
## 使用ssh进行push和pull
由于http和https在国内不太稳定，经常在push和pull过程中断开，在此使用ssh连接

- [使用ssh进行连接](https://docs.github.com/zh/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux)
- [新增SSH密钥到GitHub账户](https://docs.github.com/zh/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

## timed out 解决方案

最近在更新了本地代码 node 版本后，提交代码时报错如下
```
$ git pull project develop
ssh: connect to host github.com port 22: Connection timed out
fatal: Could not read from remote repository.
```
参考 github 官网给的 [解决办法](https://help.github.com/en/github/authenticating-to-github/using-ssh-over-the-https-port)，使用 ssh 443端口

1. 先测试可用性
```
ssh -T -p 443 git@ssh.github.com
```
2. 编辑~/.ssh/config文件，并添加以下内容
```
Host github.com
    Hostname ssh.github.com
    Port 443
    User git
```
3. 再次测试
```
$ ssh -T git@github.com
> Hi USERNAME! You've successfully authenticated, but GitHub does not
> provide shell access.
```