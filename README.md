## 简介：

Btznb是一款由Aogo技术栈官方制作的宝塔面板单站点数据备份工具，目前包含linux shell,python3等多个版本...

## 作用：
对指定站点进行数据备份操作并自动生成压缩包
- 网站源文件
- 数据库文件【.sql】
- 站点伪静态配置
- 站点nginx总配置
- 站点SSL配置文件...

## 优势：
1. 极速不等待：操作本地化基础上再优化，比你在自己电脑上压缩文件都快多了，更别谈跟官方的蜗牛速比了；
2. 简洁不冗余：除最终生成的数据压缩包外不会有多余的无用文件生成；
3. 轻便易使用：使用超级简单，仅执行一条命令即可，全程极速到几秒即可完成；
4. 优化易下载：采用多重压缩机制，在不损坏数据文件的前提下使得最终压缩包体积更小，易于用户下载及传输。

## 使用条件：
- 操作系统为Linux（推荐使用CentOS 7.6，64位）
- 必须以root身份执行
- 已安装Python3支持

> CentOS安装Python3：
>> yum install -y python3

> Ubuntu/Debian安装Python3：
>> apt install -y python3

## 使用方法：
> 首次使用会自动安装相关依赖，这个过程在10s以内完成！

- 一键使用命令：
在服务器终端键入以下命令并回车等待即可：
```
python3 <(curl -Ls https://raw.githubusercontent.com/BaicHome/btznb-script/master/btznb.py) -y 站点主域名 -d 站点对应的数据库名
```

示例：
```
python3 <(curl -Ls https://raw.githubusercontent.com/BaicHome/btznb-script/master/btznb.py) -y www.aogo.cc -d dbaomi
```

- 手动输入相关参数：
> 执行命令后，需要根据提示手动输入相关参数

```
python3 <(curl -Ls https://raw.githubusercontent.com/BaicHome/btznb-script/master/btznb.py)
```

## 定时自动备份方法：

1. 将三方云的对象存储挂载至云服务器；
2. 使用 计划任务-执行shell 实现定时备份并改名、移动至对象存储。
> 推荐重命名格式为 
>> ［网站英文名］［当前时间］.zip

PS：需要自行编写命令，很简单，自由定制

## 定时自动备份方法（白嫖党）：
- 在宝塔面板-计划任务处添加一个计划任务，类型为【Shell】，内容就是本工具的一键使用命令，注意把主域名和数据库名换成你自己的，时间看你自己，比如每周五晚上九点。
- 添加成功后他就会在你设定的时间自动备份你指定的站点数据并生成压缩包

PS：推荐配合宝塔官方免费插件【阿里云OSS】使用，添加个计划任务，时间设定为周五晚上九点半，他就会在九点半时把备份工具生成的数据压缩包自动传输到你的OSS对象存储中，全程无需任何手动操作。

- 除了阿里云，像又拍云、七牛云、腾讯云、百度网盘、自定义FTP服务器指定目录等等都行。
- 在指定时间全自动备份+传输到你的云存储，从此不用担心备份问题。
- 可以设定保留多份数据备份文件，随时找回历史版本！

## 生成的压缩包如何下载？
我们推荐以下方式：
- 直接在宝塔面板为最终数据压缩包文件生成下载外链（文件分享）
- 使用宝塔官方提供的第三方存储插件（如阿里云OSS、百度网盘备份等）将最终数据压缩包传输至您的对象存储、云盘、网盘中。

PS:可添加计划任务，配合上文中的【定时自动备份方法】达到定时备份站点所有数据并传输到指定网盘中的效果。

- 可以使用免费的文件外链服务站-API接口获取文件下载链接。
- 使用我们提供的【文件外链一键生成】服务-（速度慢，嫌勿用）。

PS：后续会开发更多功能，关注【Aogo技术栈】，及时享受免费更新权益！

<div style='text-align:center'><strong>使用授权：永久免费使用</strong></div>

<div style='text-align:center'><strong>转载授权：无需授权，但必须声明出处。</strong></div>

<div style='text-align:center'><strong>作者站点：Aogo技术栈 -欢迎来玩，不嫌弃的话可以互换友链嗷！</strong></div>

<div style='text-align:center'><strong>原创地址：https://www.aogo.cc/?p=118</strong></div>