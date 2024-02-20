# linux 系统常用命令
## 系统相关常用指令
- cd: 转移目录
- ls: 查看目录下的文件及子目录
- mkdir: 创建子目录
- cp: 复制文件。如果复制目录，需要-r
- mv：移动文件（目录）/重命名
- rm：删除文件（不可恢复！）。如果删除目录，需要-r。-f强制删除，小心使用！
- chmod：修改文件属性
- ip a ：查询ip地址
- man: 查看某个命令的帮助文档，主要可用于一些可选参数的查找
- top：动态查看当前运行进程
- jobs: 当前终端的所有进程信息
- fg/bg: 进程转后台/前台运行
- du：统计某个目录所占磁盘空间
    - du -h --max-depth=1（du -lh -d 1） 一级子目录各自所占空间大小
- history:查看当前用户的历史命令
    - !<num>可以再次执行num这一行的命令
- echo：显示变量的值
- kill ：终止进程（后加进程号<pid>）
    - -9（或-kill）：强制杀死进程
    - -19（或-stop）：暂停一个进程
    - -18（或-cont）：重新恢复暂停的进程的运行
- ssh：远程访问其他服务器
    - ssh <username>@<hostname> 然后输密码
- ll: 查看文件/目录的详细信息
- pwd: 显示当前目录位置
- ln：创建链接
    - 软连接 ln –s <target name> <link name> 相当于快捷方式，可用于文件/目录
    - 硬链接：文件副本
- grep：搜索文件中的内容
- find: 查找目录下的文件

## 快捷指令
- Ctrl C：终止当前命令
- Tab：自动补全命令
- 上下键：回溯历史命令
- 鼠标选中：即复制选中内容（和windows不同）
- 右键：即粘贴剪贴板中的内容

## 文件相关指令
- cat：显示文件，也可用于合并文件
- more：分页的方式显示文件
- head：显示文件的头部（前若干行）
- tail：显示文件的尾部（后若干行）
    - -f：循环读取（可用于查看程序输出）
- scp：远程复制文件
    - 可以复制到本地(windows需要开启ssh)
- \>/>> ：重定向（把输出追加到指定文件里），一般用于程序输出到记录文件
    - \>：从头开始
    - \>>：从原有部分继续
- |：管道符（将前面命令的输出作为后面命令的输入）
- vim编辑器（建议自学一下）
    - i进入编辑模式
    - :q退出编辑器，:wq保存并退出
- rsync: 远程同步，用于同步本地或者远程的文件。默认以文件大小和修改时间决定文件是否需要更新
    - -r, 递归
    - -a, 除了可以递归同步外，还可以同步信息（比如修改时间，权限等）
    - -v, 输出信息
    - -n, 模拟执行操作
    - 其他操作见系统说明文档
## 其他技巧
- 命令后加&，转到当前终端的后台运行（但是关掉shell题会掉）
    - 解决上述问题：运行前加nohup 或 setsid（推荐！），这样关掉shell还能继续在后台运行
- 环境变量（每个用户是独立的）：
    - ubuntu系统为~/.bashrc（带.的文件是隐藏文件）
    - 如有更改，改后source ~/.bashrc才生效（有些可能需要重启shell生效）
    - 可用alias定义一些别称，简化命令，以openfoam为例
    ```
        alias of8='source /opt/openfoam8/etc/bashrc'
        alias ofmpirun='/usr/bin/mpirun'
    ```
- 关于用户的使用限制修改：
    - stack overflow时： ulimit –s unlimited 取消栈大小的限制,建议直接写在环境变量中，一劳永逸.
    - ulimit -a
    ```bash
        core file size          (blocks, -c) 0
        data seg size           (kbytes, -d) unlimited
        scheduling priority             (-e) 0
        file size               (blocks, -f) unlimited
        pending signals                 (-i) 7823
        max locked memory       (kbytes, -l) 64
        max memory size         (kbytes, -m) unlimited
        open files                      (-n) 65536
        pipe size            (512 bytes, -p) 8
        POSIX message queues     (bytes, -q) 819200
        real-time priority              (-r) 0
        stack size              (kbytes, -s) 8192
        cpu time               (seconds, -t) unlimited
        max user processes              (-u) 7823
        virtual memory          (kbytes, -v) unlimited
        file locks                      (-x) unlimited
    ```
    - 也可在环境变量中解除以下限制
    ```bash
    ulimit -c unlimited
    ulimit -s unlimited
    ulimit -m unlimited
    ulimit -d unlimited
    ulimit -t unlimited
    ulimit -v unlimited
    ```
-  tldr 用于查找一些命令的习惯用法
    - 比如 tldr tar可以查找压缩相关的常用用法
    - 在线版本[tldr](https://tldr.inbrowser.app/)
