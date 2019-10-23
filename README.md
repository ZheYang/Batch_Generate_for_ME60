# Batch_Generate_for_ME60
generate Pool config from iplist for Huawei ME60  
从文件读取IP列表，根据模板生成华为ME60地址池配置  

模板：
ip pool pppoe_${startNumber} bas local  
gateway ${gateway} ${netmask}  
section 0 ${ip_start} ${ip_end}  
dns-server ${dns}  

示例：
10.64.0.0/10：  

ip pool pppoe_1 bas local  
gateway 10.64.0.1 255.192.0.0  
section 0 10.64.0.2 10.127.255.254  
dns-server 114.114.114.114 119.29.29.29  
#  

