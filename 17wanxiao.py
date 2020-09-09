import time
import datetime
import json
import requests

check_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"

jsons = {
	"businessType": "epmpics",
	"method": "submitUpInfoSchool",
	"jsonData": {
		"deptStr": {
			"deptid": 71881,
			"text": "信息科学与工程学院-计算机科学与技术(*)-计科F1705"
		},
		"areaStr": "{\"streetNumber\":\"\",\"street\":\"莲花街辅路\",\"district\":\"中原区\",\"city\":\"郑州市\",\"province\":\"河南省\",\"town\":\"\",\"pois\":\"河南工业大学(莲花街校区)\",\"lng\":113.55341700000157,\"lat\":34.83379196292185,\"address\":\"中原区莲花街辅路河南工业大学(莲花街校区)\",\"text\":\"河南省-郑州市\",\"code\":\"\"}",
		"reportdate": round(time.time()*1000),
		"customerid": 43,
		"deptid": 71881,
		"source": "app",
		"templateid": "clockSign2",
		"stuNo": "201716010501",
		"username": "梅杨",
		"userid": 13604407,
		"updatainfo": [{
			"propertyname": "temperature",
			"value": "35.8"
		}, {
			"propertyname": "symptom",
			"value": "无症状"
		}],
		"customerAppTypeRuleId": 147,
		"clockState": 0
	},
	"token": "270c27a3-594b-4ca1-a4f5-7b411660e502"
}

nowtime = datetime.time.now()
if nowtime.hour > 22:
	jsons["customerAppTypeRuleId"] = 146
if nowtime.hour > 13:
	jsons["customerAppTypeRuleId"] = 148

response = requests.post(check_url, json=jsons)

res = json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False)
print(res)


SCKEY = "SCU112803Td38eb92d00cfce7b66d8c1d48415edd25f5796cb03f08"

now_time = datetime.datetime.now()
bj_time = now_time + datetime.timedelta(hours=8)

test_day = datetime.datetime.strptime('2020-12-19 00:00:00','%Y-%m-%d %H:%M:%S')
date = (test_day - bj_time).days
desp = f"""
------
### 现在时间：
```
{bj_time.strftime("%Y-%m-%d %H:%M:%S %p")}
```
### 打卡信息：
```
{res}
```
> 关于打卡信息
>
> 1、成功则打卡成功
>
> 2、系统异常则是打卡频繁

### ⚡考研倒计时:
```
{date}天
```

>
> [GitHub项目地址](https://github.com/ReaJason/17wanxiaoCheckin-Actions) 
>
>期待你给项目的star✨
"""

headers = {
    "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
}

send_url = f"https://sc.ftqq.com/{SCKEY}.send"

params = {
    "text": f"完美校园健康打卡---{bj_time.strftime('%H:%M:%S')}",
    "desp": desp
}
    
# 发送消息
response = requests.post(send_url, data=params, headers=headers)
if response.json()["errmsg"] == 'success':
        print("Server酱推送服务成功")
else:
        print("Something Wrong")
