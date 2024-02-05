# 软件安装

## Matlab  
   大部分软件都是免费的，但有些软件是商业软件需要配置密钥。这里只介绍 Matlab 的激活。
   为了离线也能正常使用，如果是清华的同学，建议使用清华账户激活，仅对个人用户有效。

- 前提先连上校园网，运行 matlab, 出现以下情况时，直接点击 Next

![](imag/072cb36b-6e37-4736-80db-11625008ac3d.png)

- 按步骤，根据清华邮箱激活即可，如果没有注册，可以用邮箱注册。

![](imag/0108e4b9-88ad-4c1b-ae40-d45d75be775f.png)

另外，在安装 matlab 的时候，请选择网络版安装，不要使用清华邮箱激活安装，否则只能是安装的用户可以打开 matlab, 其他用户不能打开。安装网络版后，再将 licenses 中的 network.lic 文件删除即可，这样就可以让其他用户通过自己清华账户激活并离线使用。网络版安装流程(网络版必须联网才能使用，不方便)，见[清华 matlab 安装手册](http://its.tsinghua.edu.cn/ggrj.jsp?urltype=tree.TreeTempUrl&wbtreeid=1079)（仅校园内网访问）。

## FFTW

FFTW3 最新版下载网站[https://www.fftw.org/](https://www.fftw.org/)

以FFTW 3.3.10版本为例

###  解压

```shell
tar -zxvf fftw-3.3.10.tar.gz
```

```
cd fftw-3.3.10
```


### 安装
- 默认安装， 默认安装到/usr/local/bin

```shell
./configure
make -j64 ##多线程编译，取决有多少核
sudo make install
```

如果要自定义安装路径

```shell
./configure --prefix=/opt/fftw
make -j64
sudo make install
```

### 卸载

```shell
sudo make uninstall
```

其他./configure 选项见[https://www.fftw.org/fftw3_doc/Installation-on-Unix.html](https://www.fftw.org/fftw3_doc/Installation-on-Unix.html)

或者

```
./configure --help
```

### 配置
在编译时添加以下编译选项即可

```
-I/opt/fftw/include -L/opt/fftw/lib -lfftw3 -lm 
```
### 其他
如果使用oneAPI中的mkl内的fftw3，加载oneAPI环境后，只需要在编译的时候添加以下编译选项即可

```
-lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -liomp5 -lmkl_intel_thread
```