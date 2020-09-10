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
			"deptid": 71877,
			"text": "信息科学与工程学院-计算机科学与技术(卓越计划)-计科F1701"
		},
		"areaStr": "{\"streetNumber\":\"\",\"street\":\"\",\"district\":\"中原区\",\"city\":\"郑州市\",\"province\":\"河南省\",\"town\":\"\",\"pois\":\"河南工业大学(莲花街校区)学生公寓C区-3座\",\"lng\":113.5603279999956,\"lat\":34.83964596227749,\"address\":\"中原区河南工业大学(莲花街校区)学生公寓C区-3座\",\"text\":\"河南省-郑州市\",\"code\":\"\"}",
		"reportdate": 1599743266849,
		"customerid": 43,
		"deptid": 71877,
		"source": "app",
		"templateid": "clockSign3",
		"stuNo": "201716010515",
		"username": "夏克伟",
		"userid": 12658292,
		"updatainfo": [{
			"propertyname": "temperature",
			"value": "36.6"
		}, {
			"propertyname": "symptom",
			"value": "无症状"
		}],
		"customerAppTypeRuleId": 148,
		"clockState": 0
	},
	"token": "638b7d2c-d9f3-4a30-952c-3111a4575eb2"
}

nowhour = datetime.datetime.now().hour
if nowhour > 21:
	jsons["jsonData"]["customerAppTypeRuleId"] = 146
elif nowhour > 12:
	jsons["jsonData"]["customerAppTypeRuleId"] = 148

response = requests.post(check_url, json=jsons)

res = json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False)
print(res)
