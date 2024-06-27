import pytest
    
def test_zabbix_agent_running(host):
    zabbix_agent = host.service("zabbix-agent")
    assert zabbix_agent.is_running

def test_zabbix_agent_enabled(host):
    zabbix_agent = host.service("zabbix-agent")
    assert zabbix_agent.is_enabled
