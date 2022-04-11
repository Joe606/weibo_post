
from re import T
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# url = 'https://pinduoduo.com/'
# option = webdriver.ChromeOptions()
# option.add_experimental_option('detach', True)
# global driver
# driver = webdriver.Chrome('C:/Users/Neq/Downloads/Chromedriver_Win32/chromedriver_win32/chromedriver.exe', options=option)
# driver.get(url)
# time.sleep(5)
# page = driver.page_source
# print(
#     'page is : {}'.format(page)
# )
class Get_Data:
    '''get weibo data'''
    

    def __init__(self, url):
        # self.__key_word__ = key_word
    
            # Connect
            # global browser

        self.options = Options()
        self.options.page_load_strategy = 'normal'
        # self.options.page_load_strategy = 'eager'
        self.options.add_experimental_option('detach', True)
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
        self.options.add_argument('--user-agent=%s' % self.user_agent)
        
        self.service = Service(executable_path='C:/Users/Neq/Downloads/Chromedriver_Win32/chromedriver_win32/chromedriver.exe')
        self.browser = webdriver.Chrome(service=self.service, options=self.options)
        # self.browser = webdriver.Chrome(executable_path='C:/Users/Neq/Downloads/Chromedriver_Win32/chromedriver_win32/chromedriver.exe', options=options)
        # self.browser.set_window_size(1800, 900)
        self.browser.get(url)
        # self.browser.fullscreen_window()
        self.wait = WebDriverWait(self.browser, 5)
        time.sleep(5)
        self.original_window = self.browser.current_window_handle
        print('type of original_window is:{}'.format(type(self.original_window)))
        assert len(self.browser.window_handles) == 1
        print('*************original_window************* is:{}'.format(self.original_window))




    def crawl_wrapper_data(self):    
        #cut the web page html into three : head/profile, neck/classification(post/video/article/photo_album), body/post
        # html_head = self.browser.find_element(By.CLASS_NAME, 'woo-panel-main')[1]
        html_head = self.browser.find_element(By.CLASS_NAME, 'Card_bottomGap_2Xjqi')
        # html_neck = self.browser.find_element(By.CLASS_NAME, 'SecBar_secBar_2KHxF SecBar_visable_16JHY')
        html_body = self.browser.find_element(By.CLASS_NAME, 'container')

        #catch the profile data dict
        home_profile = dict()
        head_profile = html_head.text.split('\n')
        print('head_profile is:{}'.format(head_profile))
        head_key = ['名称', '粉丝', '关注', '昨日发博', '阅读数', '互动数', '视频累计播放量', '平台性质']
        for i in ['关注', '私信']:
            print(1111)
            head_profile.remove(i)

        for i in head_profile:
            print(222222)
            if re.search('昨日发博', i):
                head_profile.extend(i.split('，'))
                head_profile.remove(i)
        for j in head_profile: #split the string and the number of the data
            for i in head_key:
                print(333333)
                if re.search(i, j):
                    jj = j.replace(i, '')
                    home_profile[i] = jj
                else:
                    continue
        # home_profile['head_name'] = html_head.find_element(By.CLASS_NAME, 'ProfileHeader_name_1KbBs').text
        # home_profile['woo_picture'] = html_head.find_element(By.CLASS_NAME, '')
        # home_profile['woo_avatar_img'] = html_head.find_element(By.CLASS_NAME, '')

        print('home_profile is:{}'.format(home_profile))



        #catch the posts data dict 
        post_content = dict()
        post_box = html_body.find_elements(By.CLASS_NAME, 'vue-recycle-scroller__item-view')
        print('len of post_box is:{}'.format(len(post_box)), 'type of post_box is:{}'.format(type(post_box)))
        print('the content of post_box is{}'.format(post_box))

        for i in range(len(post_box)):
            #get time_line to act as key
            post_time_stamp_element = post_box[i].find_element(By.CLASS_NAME, 'head-info_time_6sFQg')
            post_time_stamp = post_time_stamp_element.get_attribute('title')
            #get post detail which act as the value
            # post_content[post_time_stamp] = post_box[i].text.split('\n')
            post_content[post_time_stamp] = post_box[i].find_element(By.CLASS_NAME, 'Feed_body_3R0rO').text.split('\n')
            #get retweet count #get comment count #get like count
            
            retweet_comment_like = post_box[i].find_element(By.TAG_NAME, 'footer').get_attribute('aria-label')
            post_content[post_time_stamp].append(retweet_comment_like)
            
            
            # post_content['no_1']
            # post_content['no_2']
            # post_content['no_3']
            # post_content['no_4']
              

        print('post_content is ： {}'.format(post_content))

        return home_profile, post_content



    def open_web(self, key_word):    
        try:
            # self.browser.find_element(By.NAME, 'username').send_keys('MYEMAIL', Keys.TAB, 'MYPW', Keys.ENTER)
            input_box = self.browser.find_elements(By.CLASS_NAME, 'woo-input-main')
            if input_box:
                print('the data type of input_box is:{}'.format(type(input_box)))
                # for i in input_box:
                print('the content of input_box is:{}'.format(input_box))
            search_box = input_box[0]
            # key_word = '梨视频'
            search_box.send_keys(key_word + Keys.ENTER)
            # search_box.send_keys('梨视频')
            
            # # search_button = self.browser.find_element(By.CLASS_NAME, 'woo-button-main woo-button-flat woo-button-primary woo-button-m LoginTopNav_btn_3LmVt')
            # # search_button = self.browser.find_elements(By.CLASS_NAME, 'woo-button-content')[0]
            # if search_button:
            #     print('search_button is:{}'.format(search_button.text))
            #     print('the content of search_button is: {}'.format(search_button))
            # search_button.click  
            # driver.find_element(By.LINK_TEXT, "new window").click()
            time.sleep(5)

            #switch to the new open tab window
            self.wait.until(EC.number_of_windows_to_be(2))
            no_two_window = str()
            for window_handle in self.browser.window_handles:
                if window_handle != self.original_window:
                    self.browser.switch_to.window(window_handle)
                    no_two_window = window_handle
                    break
            self.wait.until(EC.title_is('微博搜索'))
            print('EC.is_title is:{}'.format(self.browser.title))
            print('*************no_two_window************* is:{}'.format(no_two_window))
            
            
            #click ankor link to next new tab window
            self.browser.find_element(By.LINK_TEXT, key_word).click()
            self.wait.until(EC.number_of_windows_to_be(3))
            no_three_window = str()
            for window_handle in self.browser.window_handles:
                if window_handle != self.original_window and window_handle != no_two_window:
                    self.browser.switch_to.window(window_handle)
                    no_three_window = window_handle
                    break
            # self.wait.until(EC.title_is(''))
            print('EC.title_is is:{}'.format(self.browser.title))
            print('*************no_three_window************* is:{}'.format(no_three_window))
            ####add roll down to the bottom, self.wait the complication of selenium 4.3 
            time.sleep(8)

            profile, posts = dict(), dict()  #store all the result data
            for i in range(10):
                print('i: %s' % i)
                profile, mid_post = self.crawl_wrapper_data()  ####use generator
                posts.update(mid_post)

                self.browser.execute_script('window.scrollTo(0, (document.body.scrollHeight/4)*{})'.format(i))
                time.sleep(5)
                print('i+1:', i+1)

            
            
            print('the last result of the profile is : {0}, \n, the last result of the whole posts is :  {1}'.format(profile, posts))
            print('the length of the profile is: {0}, \n, the length of the whole posts is: {1}'.format(len(profile), len(posts)))

            # for i in range(4):
            #     self.browser.execute_script('window.scrollTo(0, 0)')
            #     time.sleep(5)
            #     self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            #     time.sleep(5)


        except Exception as e:
            print ('look, error fly!!! :'.upper(), e)
        else:
            print('the processing is perfect, no fault!')
            self.browser.minimize_window()
            self.browser.close()
            print('close the current the tab window.')
        finally:
            print('the current class of processing is open_web.')
            self.browser.quit()
            print('quit the self.browser completely!')

        all_in_one_account = dict()
        all_in_one_account.update(profile)
        all_in_one_account.update(posts)
        return profile, posts, all_in_one_account





if __name__ == '__main__':
    url = 'https://www.weibo.com'
    key_word = ['梨视频', '杨幂']
    # key_word = '杨幂'
    
    for key in key_word: ##use multi-threading/multi-process/Coroutines
        get_data = Get_Data(url)
        profile, posts, all_in_one_account = get_data.open_web(key)

        import json
        with open('{}.json'.format(key), 'w+', ensure_ascii=False) as f:
            json_str = json.dumps(all_in_one_account)
            f.write(json_str)
        time.sleep(5)

    for key in key_word:
        import os
        os.getcwd()
        os.listdir()
        import json
        with open('{0}.json'.format(key), 'r') as f:
            json_dict = json.load(f)
            for k,v in json_dict.items():
                print(k, '****************\n', v)