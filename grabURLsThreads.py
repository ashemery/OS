import xml.etree.ElementTree as etree
import requests
import time
import queue, threading


URLFeeds = ["URL1",
            "URL2",
            "URL3",
            "URL4"]

def get_info_from_url(feed_url):
    xml = requests.get(feed_url).text
    tree = etree.fromstring(xml)
    name = tree.find(".//location").text
    temperature = tree.find(".//temperature_string").text
    time.sleep(1.5)
    return name, temperature

if __name__ == "__main__":
    now = time.ctime()
    print ("Current temperature at %s" % now)
    print ("_" * 12)
    for feed in URLFeeds:
        name, temperature = get_info_from_url(feed)
        print ("\t%s : %s" % (name,temperature))
    print("")
    print("Script ended at ", time.ctime())



