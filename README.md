# fork的如下https://github.com/moyada/stealer

项目使用 `python3` + `Vue` 开发，安装所需依赖:

`pip install -r requirements.txt --index-url https://pypi.douban.com/simple`
OR
```shell script
pip install Django
pip install requests
pip install enum34
pip install django-cors-headers
```

下载解压完运行 `start.sh` 或 `run.sh`，通过浏览器打开 [localhost:8000](http://localhost:8000) 进入使用页面。

- 点击`下载`直接下载视频
- 点击`解析`获取下载地址

[~~试用地址~~](http://127.0.0.01:8000/#/) 暂无空余服务器可用 

### Docker 方式部署

1. 构建镜像，拉取镜像 `docker pull xueyikang/stealer` 
2. 启动容器，执行命令 `docker run -d -p 8000:8000 xueyikang/stealer`, 应用地址为：127.0.0.1:8000
