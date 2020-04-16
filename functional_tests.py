from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_index(self):
        # เธอได้ยินมาว่ามีเว็บในการคำนวณเกรดและอยากจะใช้งาน
        # จึงเข้าเว็บไปที่หน้า Homepage
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''

        # test GradeGuide's header text
        # เธอสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # test home page link
        # เธอเห็น link home page ของ GradeGuide
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        # test sign up link
        # เธอเห็น link สำหรับ sign up 
        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        # test log in link
        # เธอเห็น link สำหรับ log in
        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        # test Welcome's header text
        # เธอเห็นคำว่า Welcome to GradeGuide !
        welcome_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Welcome to GradeGuide !', welcome_text)

        # test paragraph text
        # เธอเห็นคำว่า Total users registered: 
        totaluser_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Total users registered:', totaluser_text)

        # เธอกด log in 
        login_click = self.browser.find_element_by_link_text('Log in')
        login_click.click()

        # test username label
        # เธอเห็นคำว่า Username:
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)

        # test username's textbox
        # เธอเห็น textbox ไว้สำหรับกรอกชื่อ
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )

        # test password label
        # เธอเห็นคำว่า Password:
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)

        # test password's textbox
        # เธอเห็น textbox ไว้สำหรับกรอก password ของเธอลงไป
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )

        # test log in button
        # เธอเห็นปุ่มไว้สำหรับ log in เข้าใช้งาน GradeGuide
        login_button = self.browser.find_element_by_tag_name("button")
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )

    def test_login_fail(self):
        # เธอเข้าเว็บไปที่หน้า Homepage
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''

        # test username label
        # เธอเห็นคำว่า Username:
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)

        # test username's textbox
        # เธอเห็น textbox ไว้สำหรับกรอกชื่อ
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )

        # test password label
        # เธอเห็นคำว่า Password:
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)

        # test password's textbox
        # เธอเห็น textbox ไว้สำหรับกรอก password ของเธอลงไป
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )

        # test log in button
        # เธอเห็นปุ่มไว้สำหรับ log in เข้าใช้งาน GradeGuide
        login_button = self.browser.find_element_by_tag_name("button")
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )

        # test error message
        # เธอเห็น error message ว่า Please enter a correct username and password. Note that both fields may be case-sensitive.
        error_message = self.browser.find_element_by_tag_name('ul').text
        self.assertIn('Please enter a correct username and password. Note that both fields may be case-sensitive.',
                      error_message)

        time.sleep(20)

    def test_login_pass(self):
        # เธอเข้าเว็บไปที่หน้า Homepage
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''

        # test username label
        # เธอเห็นคำว่า Username:
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)

        # test username's textbox
        # เธอเห็น textbox ไว้สำหรับกรอกชื่อ
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )

        # test password label
        # เธอเห็นคำว่า Password:
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)

        # test password's textbox
        # เธอเห็น textbox ไว้สำหรับกรอก password ของเธอลงไป
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )

        # test log in button
        # เธอเห็นปุ่มไว้สำหรับ log in เข้าใช้งาน GradeGuide
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )

        # เธอกรอก username ลงไปว่า jesselingard
        username_box.send_keys('jesselingard')

        # หลังจากนั้นเธอกรอก password ลงไปว่า lingard123456789
        password_box.send_keys('lingard123456789')

        # แล้วจึงคลิกที่ปุ่ม log in เพื่อทำการเข้าใช้งาน
        login_button.click()
        
        # test redirect to home page link
        # หลังจาก log in เรียบร้อยแล้ว
        # เว็บเด้งหน้า home page ของ GradeGuide ขึ้นมาดังเดิม
        # ดังนั้นเธอจึงเห็นว่าเป็น link home page ของ GradeGuide
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        # test log out link
        # และที่เปลี่ยนไปคือตรง log in เปลี่ยนมาเป็น log out แทน
        logout_link = self.browser.find_element_by_link_text('Log out').text
        self.assertIn('Log out', logout_link)

        # test ID's header text
        # ในส่วนที่เพิ่มมาคือ ID ของผู้ใช้
        # ในที่นี้เธอใช้ username ในการ log in ว่า jesselingard
        # เธอจึงเห็นคำว่า ID : jesselingard
        id_text = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('ID : jesselingard', id_text)

    def test_subjects_button_flow(self):
        # เธอคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')
        time.sleep(5)

        # test Flow H1 text
        # เธอเห็นคำว่า Flow ซึ่งเป็นหัวข้อใหญ่
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('Flow', header_text)

        # เธอเห็นประโยคที่อยู่ก่อนหน้าปุ่ม subjects
        defination = self.browser.find_element_by_tag_name('p1').text
        self.assertEqual("If you can't remember the subject's name , The Subjects button will help you. :)",defination)

        # test subjects button
        # เธอจำชื่อวิชาไม่ได้
        # เธอจึงคลิกไปที่ปุ่ม subjects เพื่อที่เธอจะได้ดูชื่อวิชา
        subject_button = self.browser.find_element_by_id("subject_button")
        subject_button.click()
        time.sleep(5)

        self.fail('Finish the test!')

    def test_search_flow(self):
        # เธอคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')

        self.assertIn('', self.browser.title)

        # test search box
        # เธอเห็นช่องสำหรับใส่ชื่อวิชาเพื่อค้นหาวิชาที่เป็นตัวต่อกัน
        # เธอจึงพิมพ์วิชา Programming Fundamental ลงไป
        subject_placeholder = self.browser.find_element_by_id("search_placeholder")
        self.assertEqual(
            subject_placeholder.get_attribute('type'),
            'text'
        )

        subject_placeholder.send_keys('Programming Fundamental')
        time.sleep(5)

        # test submit button
        # เธอจึงกดปุ่ม search เพื่อทำการหาตัวต่อของวิชา Programming Fundamental
        submit_button = self.browser.find_element_by_id("submit_button")
        self.assertEqual(
            submit_button.get_attribute('type'),
            'submit'
        )
        submit_button.click()
        time.sleep(10)

        # test input Search text
        # เธอเห็นหัวข้อ subject
        # หลังจากที่เธอกด search แล้ว เธอพบว่าวิชาที่เธฮ search ไปปรากฏอยู่หลังหัวข้อ subject
        subject_head = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual('subject : Programming Fundamental', subject_head)

        # test search result
        # เธอเห็นผลของการ search ของเธอ หลังจากที่กดปุ่ม search ไป
        result_search = self.browser.find_element_by_tag_name('p2').text
        self.assertEqual("Semister2 : Algorithms and Data Structures\nSemister5 : Operating Systems",result_search)

        # test Note
        # เธอเห็นประโยคด้านล่างเกี่ยวกับวิชาเลือก
        note = self.browser.find_element_by_tag_name('p3').text
        self.assertEqual("Note : Elective Subjects don't connect to each other but I want to show how many elective subjects are in this flow.", note)

        self.fail('Finish the test!')
        
    def test_flow_pic(self):
        # เธอคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')
        time.sleep(5)

        # test fullflow button
        # เธออยากดูภาพรวมของวิชาทั้งหมดที่เธอต้องเรียน
        # เธอจึงคลิกไปที่ปุ่ม Full Flow เพื่อไปยังรูป flow
        flow_button = self.browser.find_element_by_id("fullflow_button")
        flow_button.click()

        # test can find the flow picture
        # เธอเห็นภาพวิชาตัวต่อทั้งหมด
        flow_image = self.browser.find_element_by_id("image")
        self.assertEqual(
            flow_image.get_attribute('id'),
            'image'
        )
        time.sleep(10)

        self.fail('Finish the test!')
        
    def test_home(self):
        # เมื่อเธอกดเข้าไปที่หน้า signup
        self.browser.get('http://localhost:8000/signup')

        username_box = self.browser.find_element_by_id("id_username")

        password_box = self.browser.find_element_by_id("id_password1")

        password_box2 = self.browser.find_element_by_id("id_password2")

        # test username ,password and password confirmation textbox
        # เธอทำการสมัคร username jesselingard
        # password lingard123456789
        # password2 lingard123456789
        username_box.send_keys('jesselingard')
        password_box.send_keys('lingard123456789')
        password_box2.send_keys('lingard123456789')

        # test sign up button
        # เธอทำการกดปุ่ม signup
        signup_button = self.browser.find_element_by_tag_name("button")
        signup_button.click()
        time.sleep(2)

        # test log in 's header text
        # เธอเข้าไปที่หน้า login
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', header_text)

        username_login_box = self.browser.find_element_by_id("id_username")

        password_login_box = self.browser.find_element_by_id("id_password")

        # test username and password textbox
        # เธอใส่ id password
        username_login_box.send_keys('jesselingard')
        password_login_box.send_keys('lingard123456789')

        # test log in button
        # เธอกดปุ่ม login
        login_button = self.browser.find_element_by_tag_name("button")
        login_button.click()
        time.sleep(2)

        # test ID's header text 
        # เธอเข้าไปที่หน้า homepage
        self.browser.get('http://127.0.0.1:8000/home')
        id_user = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('jesselingard', id_user)

        # test subject's unit
        # เธอใส่ unit ไป 1 หน่วยกิต
        unit_text = self.browser.find_element_by_id('subject1Unitid')
        unit_text.send_keys('Unit: 1')

        # test subject's grade
        # เธอใส่ Grade C+
        unit_text = self.browser.find_element_by_id('subject1Gradeid')
        unit_text.send_keys('Grade: 2.5&nbsp; (C+)')
        time.sleep(3)

        # test submit button
        # เธอกดปุ่ม submit
        submit_button = self.browser.find_element_by_id("submit")
        submit_button.click()
        time.sleep(3)

        # เธอเห็นเกรดแสดงขึ้นมาว่าเกรด 2.5
        submit_text = self.browser.find_element_by_id('gradeshow').text
        self.assertIn('2.5', submit_text)
        time.sleep(6)

        # เธอเห็นสถานะนักศึกษาของเธอว่าอยู่เกณฑ์ปกติหรือ Normal State
        self.assertIn('Normal State', submit_text)

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
