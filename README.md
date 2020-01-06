# dada_openapi_client
达达开放平台的签名封装

## dada_client

### 支持的功能
1. 根据达达开放平台的签名规则进行签名  
[签名规则](https://newopen.imdada.cn/#/development/file/safety?_k=n7uzsr)

### 安装
```shell script
pip install dada_openapi_client
```

### 使用
```python
from dada_openapi_client.dada_client import DdMakeSign

body = {
    "source_id": "73753",
    "v": "1.0",
    "format": "json",
    "body": "{\"order_id\":\"111111111\"}",
    "timestamp": "1574927842"
}
d = DdMakeSign(appKey='dada11111111111', app_secret='111111111111111111111111')
print(d.make_sign(body=body))
```
