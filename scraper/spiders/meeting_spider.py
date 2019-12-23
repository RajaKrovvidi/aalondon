import scrapy
import os
import pandas as pd
from bs4 import BeautifulSoup
import re
import csv
from scraper.items import MeetingItem






from scrapy import Spider
from scrapy.http import FormRequest,Request
from scrapy.utils.response import open_in_browser
 

intergroups = {117:"City Of London",36:"East London",123:"Chelsea",124:"Chelsea & Fulham",118:"London North East",51:"London North",64:"London North Middlesex",
    63:"London North West",62:"London South Middlesex",119:"London West End",120:"London Westway",75:"London Croydon Epsom & Sutton",55:"London North Kent",
    122:"London South East (East)",121:"London South East (West)",77:"London South",42:"London South West"} 

class AASpider(scrapy.Spider):
    name = 'aameetings'
    intergroup_urls = {x[0]:f'https://www.alcoholics-anonymous.org.uk/markers.do?ig={x[0]}'  for x  in intergroups.items()}
    member_ids = []
    with open('aameetings.csv', 'w', newline='\n', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["marker_title", "marker_time","marker_lat","marker_lng","marker_address","marker_postcode"\
                ,"marker_code","marker_day","marker_hearing","marker_wheelchair","marker_url","detail_url","detail_line_one","detail_line_two","detail_line_three"\
                    ,"detail_line_four","detail_line_five","detail_line_six","detail_line_seven","detail_line_eight","detail_line_nine"])

    def start_requests(self):
        for intergroup_id,url in self.intergroup_urls.items():
            yield Request(url,callback=self.parse,meta={'intergroup_id':intergroup_id})
   
    def parse(self, response):

        soup = BeautifulSoup(response.text, 'html.parser') 
        meetings=soup.find_all('marker')
        for meeting in meetings:
            marker_title = meeting.get('title')
            marker_address = meeting.get('address')
            marker_code = meeting.get('code')
            marker_day = meeting.get('day')
            hearing = meeting.get('hearing')
            marker_lat = meeting.get('lat') or None
            marker_lng = meeting.get('lng') or None
            marker_postcode = meeting.get('postcode')
            slat = meeting.get('slat')
            slng = meeting.get('slng')
            marker_time = meeting.get('time')
            marker_wheelchair = meeting.get('wheelchair')
            marker_hearing = meeting.get('hearing')
            marker_time = marker_time.replace(".",":")
            marker_url = response.url
            
            meeting_data = {'code':marker_code,'day':marker_day,'hearing':marker_hearing,'lat':marker_lat,'lng':marker_lng,'postcode':marker_postcode,'time':marker_time,\
               'duration':'','title':marker_title,'wheelchair':marker_wheelchair,'intergroup':''}     
          
          


            url = f'https://www.alcoholics-anonymous.org.uk/detail.do?id={marker_code}'
            
            yield Request(url=url,callback=self.get_meeting_detail,meta={'meeting_data':meeting_data})

    
    def get_meeting_detail(self,response):
        meeting_data = response.meta.get('meeting_data')

        data = response.text
        soup = BeautifulSoup(data, features="lxml")
        dpanel = soup.find('div',{"class": "dpanel"})
        table = soup.find('div',{"class": "dpanel"}).find_parent("table")
        header = soup.find('div',{"class": "dpanel"}).findChild("h3")
        detail_url = response.url
        
                   
        lines =  [line for line in dpanel.strings] 

        detail = "\n".join(lines[3:])
        meeting_data['detail'] = detail
        item = MeetingItem(meeting_data)
        yield item
        

    