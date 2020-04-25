from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_click_to_LOGIN_link(self):
        # เธอได้ยินมาว่ามีเว็บในการคำนวณเกรดและอยากจะใช้งาน
        # จึงเข้าเว็บไปที่หน้า Homepage
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''

        # test GradeGuide's header text
        # เธอสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_partial_link_text('GRADEGUIDE').text
        self.assertEqual('GRADEGUIDE', header_text)

        # test flow link
        # เธอเห็น link สำหรับไปที่หน้า flow
        flow_link = self.browser.find_element_by_partial_link_text('FLOW').text
        self.assertEqual('FLOW', flow_link)

        # test about link
        # เธอเห็น link สำหรับไปที่หน้า about 
        about_link = self.browser.find_element_by_partial_link_text('ABOUT').text
        self.assertEqual('ABOUT', about_link)

        # test help link
        # เธอเห็น link สำหรับไปหน้า help
        help_link = self.browser.find_element_by_partial_link_text('HELP').text
        self.assertEqual('HELP', help_link)

        # test sign up link
        # เธอเห็น link สำหรับ sign up 
        signup_link = self.browser.find_element_by_partial_link_text('SIGNUP').text
        self.assertEqual('SIGNUP', signup_link)

        # test log in link
        # เธอเห็น link สำหรับ log in
        login_link = self.browser.find_element_by_partial_link_text('LOGIN').text
        self.assertEqual('LOGIN', login_link)

        # test Welcome's header text
        # เธอเห็นคำว่า Welcome to GradeGuide !
        welcome_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Welcome to GradeGuide !', welcome_text)

        # test paragraph text
        # เธอเห็นคำว่า Total users registered: 
        totaluser_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Total users registered:', totaluser_text)
        time.sleep(6)

        # เธอกด log in 
        login_click = self.browser.find_element_by_partial_link_text('LOGIN')
        login_click.click()

        # test username label
        # เธอเห็นคำว่า Username:
        username_label = self.browser.find_element_by_xpath(
            "//label[@for='id_username']"
        ).text
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
        password_label = self.browser.find_element_by_xpath(
            "//label[@for='id_password']"
        ).text
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
        login_button = self.browser.find_element_by_id('login')
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )
        time.sleep(6)

    def test_can_sign_up(self):
        # เมื่อเธอกดเข้าไปที่หน้า signup
        self.browser.get('http://localhost:8000/signup')

        username_box = self.browser.find_element_by_id("id_username")

        password_box = self.browser.find_element_by_id("id_password1")

        password_box2 = self.browser.find_element_by_id("id_password2")

        # test username ,password and password confirmation textbox
        # เธอทำการสมัคร username : Tina
        # password : happyholiday
        # password confirmation : happyholiday
        username_box.send_keys('Tina')
        password_box.send_keys('happyholiday')
        password_box2.send_keys('happyholiday')
        time.sleep(10)

        # test sign up button
        # เธอทำการกดปุ่ม signup
        signup_button = self.browser.find_element_by_id('signup')
        signup_button.click()

        # test log out link
        # และที่เปลี่ยนไปคือตรง sign up เปลี่ยนมาเป็น log out แทน
        logout_link = self.browser.find_element_by_partial_link_text('LOGOUT').text
        self.assertIn('LOGOUT', logout_link)

        # test Grade Calculator link
        # เธอเห็น link ที่เพิ่มขึ้นมาคือ Grade Calculator
        grade_calculator_link = self.browser.find_element_by_partial_link_text('GRADE CALCULATOR').text
        self.assertIn('GRADE CALCULATOR', grade_calculator_link)

        # test Result link
        # เธอเห็น link Result
        result_link = self.browser.find_element_by_partial_link_text('RESULT').text
        self.assertIn('RESULT', result_link)

        # test Graph link
        # เธอเห็น link Graph
        graph_link = self.browser.find_element_by_partial_link_text('GRAPH').text
        self.assertIn('GRAPH', graph_link)

        # test ID's header text
        # หลังจาก sign up  เรียบร้อยแล้ว
        # เว็บเด้งหน้า home page ของ GradeGuide ขึ้นมา
        # ในที่นี้เธอใช้ username ในการ log in ว่า Tina
        # เธอจึงเห็นคำว่า ID : Tina
        id_text = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('ID : Tina', id_text)
        time.sleep(5)

    def test_login_fail(self):
        # เธอเข้าเว็บไปที่หน้า LOGIN
        self.browser.get('http://localhost:8000/accounts/login/')

        # test username label
        # เธอเห็นคำว่า Username:
        username_label = self.browser.find_element_by_xpath(
            "//label[@for='id_username']"
        ).text
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
        password_label = self.browser.find_element_by_xpath(
            "//label[@for='id_password']"
        ).text
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
        login_button = self.browser.find_element_by_id('login')
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )

        # เธอใส่ username ว่า abcd
        # เธอใส่ password ว่า 123456789
        # เธอกด login
        username_box.send_keys('abcd')
        password_box.send_keys('123456789')
        time.sleep(5)
        login_button.click()

        # test error message
        # เธอเห็น error message 
        error_message = self.browser.find_element_by_tag_name('error_message').text
        self.assertIn("Please enter a correct username and password. Note that both fields may be case-sensitive.",error_message)
        time.sleep(10)

    def test_login_pass(self):
        # เธอเข้าเว็บไปที่หน้า LOGIN
        self.browser.get('http://localhost:8000/accounts/login/')
        '''Test Only Index'''

        # test username label
        # เธอเห็นคำว่า Username:
        username_label = self.browser.find_element_by_xpath(
            "//label[@for='id_username']"
        ).text
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
        password_label = self.browser.find_element_by_xpath(
            "//label[@for='id_password']"
        ).text
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
        login_button = self.browser.find_element_by_id('login')
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )

        # เธอกรอก username ลงไปว่า jesselingard
        username_box.send_keys('jesselingard')

        # หลังจากนั้นเธอกรอก password ลงไปว่า lingard123456789
        password_box.send_keys('lingard123456789')
        time.sleep(5)

        # แล้วจึงคลิกที่ปุ่ม log in เพื่อทำการเข้าใช้งาน
        login_button.click()

        # test log out link
        # และที่เปลี่ยนไปคือตรง log in เปลี่ยนมาเป็น log out แทน
        logout_link = self.browser.find_element_by_partial_link_text('LOGOUT').text
        self.assertIn('LOGOUT', logout_link)

        # test Grade Calculator link
        # เธอเห็น link ที่เพิ่มขึ้นมาคือ Grade Calculator
        grade_calculator_link = self.browser.find_element_by_partial_link_text('GRADE CALCULATOR').text
        self.assertIn('GRADE CALCULATOR', grade_calculator_link)

        # test Result link
        # เธอเห็น link Result
        result_link = self.browser.find_element_by_partial_link_text('RESULT').text
        self.assertIn('RESULT', result_link)

        # test Graph link
        # เธอเห็น link Graph
        graph_link = self.browser.find_element_by_partial_link_text('GRAPH').text
        self.assertIn('GRAPH', graph_link)
        
        # test ID's header text
        # หลังจาก log in เรียบร้อยแล้ว
        # เว็บเด้งหน้า home page ของ GradeGuide ขึ้นมา
        # ในที่นี้เธอใช้ username ในการ log in ว่า jesselingard
        # เธอจึงเห็นคำว่า ID : jesselingard
        id_text = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('ID : jesselingard', id_text)
        time.sleep(6)

    def test_can_click_subjects_button_flow_to_see_all_subjects(self):
        # เธอคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')
        time.sleep(5)

        # test Flow H1 text
        # เธอเห็นคำว่า Flow ซึ่งเป็นหัวข้อใหญ่
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('Flow', header_text)

        # เธอเห็นประโยคที่อยู่ก่อนหน้าปุ่ม subjects
        defination = self.browser.find_element_by_tag_name('p1').text
        self.assertEqual("If you can't remember the subject's name , The Subjects button will help you. :)",
                        defination
                        )

        # test subjects button
        # เธอจำชื่อวิชาไม่ได้
        # เธอจึงคลิกไปที่ปุ่ม subjects เพื่อที่เธอจะได้ดูชื่อวิชา
        subject_button = self.browser.find_element_by_id("subject_button")
        subject_button.click()
        time.sleep(5)

    def test_can_search_subject(self):
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
        # หลังจากที่เธอกด search แล้ว 
        # เธอพบว่าวิชาที่เธอ search ไปปรากฏอยู่หลังหัวข้อ subject
        subject_head = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual('subject : Programming Fundamental', subject_head)

        # test search result
        # เธอเห็นผลของการ search ของเธอ หลังจากที่กดปุ่ม search ไป
        result_search = self.browser.find_element_by_tag_name('p2').text
        self.assertEqual("""Semister2 : Algorithms and Data Structures\nSemister5 : Operating Systems""",
                        result_search
                        )

        # test Note
        # เธอเห็นประโยคด้านล่างเกี่ยวกับวิชาเลือก
        note = self.browser.find_element_by_tag_name('p3').text
        self.assertEqual("Note : Elective Subjects don't connect to each other but I want to show how many elective subjects are in this flow.",
                        note
                        )
        
    def test_can_click_full_flow_button_to_show_flow_picture(self):
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
        
    def test_can_calculate_the_grade(self):
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
        login_button = self.browser.find_element_by_id('login')
        login_button.click()
        time.sleep(6)

        # test ID's header
        # เธอเห็น ID ของเธอว่า jesselingard
        id_user = self.browser.find_element_by_tag_name('h4').text
        self.assertEqual('ID : jesselingard', id_user)

        # test subject's unit
        # เธอใส่ unit ลงไปทั้งหมด 8 วิชา
        first_subject_unit = Select(self.browser.find_element_by_id('subject1Unitid'))
        first_subject_unit.select_by_value('3')

        second_subject_unit = Select(self.browser.find_element_by_id('subject2Unitid'))
        second_subject_unit.select_by_value('1')

        third_subject_unit = Select(self.browser.find_element_by_id('subject3Unitid'))
        third_subject_unit.select_by_value('3')

        fourth_subject_unit = Select(self.browser.find_element_by_id('subject4Unitid'))
        fourth_subject_unit.select_by_value('3')

        fifth_subject_unit = Select(self.browser.find_element_by_id('subject5Unitid'))
        fifth_subject_unit.select_by_value('3')

        sixth_subject_unit = Select(self.browser.find_element_by_id('subject6Unitid'))
        sixth_subject_unit.select_by_value('3')

        seventh_subject_unit = Select(self.browser.find_element_by_id('subject7Unitid'))
        seventh_subject_unit.select_by_value('3')

        eighth_subject_unit = Select(self.browser.find_element_by_id('subject8Unitid'))
        eighth_subject_unit.select_by_value('3')

        # test subject's grade
        # เธอใส่ Grade ลงไปทั้งหมด 8 วิชา
        first_subject_grade = Select(self.browser.find_element_by_id('subject1Gradeid'))
        first_subject_grade.select_by_value('4')

        second_subject_grade = Select(self.browser.find_element_by_id('subject2Gradeid'))
        second_subject_grade.select_by_value('3')

        third_subject_grade = Select(self.browser.find_element_by_id('subject3Gradeid'))
        third_subject_grade.select_by_value('1')

        fourth_subject_grade = Select(self.browser.find_element_by_id('subject4Gradeid'))
        fourth_subject_grade.select_by_value('1.5')

        fifth_subject_grade = Select(self.browser.find_element_by_id('subject5Gradeid'))
        fifth_subject_grade.select_by_value('2')

        sixth_subject_grade = Select(self.browser.find_element_by_id('subject6Gradeid'))
        sixth_subject_grade.select_by_value('2.5')

        seventh_subject_grade = Select(self.browser.find_element_by_id('subject7Gradeid'))
        seventh_subject_grade.select_by_value('1')

        eighth_subject_grade = Select(self.browser.find_element_by_id('subject8Gradeid'))
        eighth_subject_grade.select_by_value('1.5')

        # test submit button
        # เธอกดปุ่ม submit
        submit_button = self.browser.find_element_by_id("submit_button")
        submit_button.click()

        # เธอเห็นเกรดแสดงขึ้นมาว่าเกรด 1.98
        grade_text = self.browser.find_element_by_id('demo').text
        self.assertIn('1.98', grade_text)
        time.sleep(6)

        # เธอเห็นสถานะนักศึกษาของเธอว่าติดโปรหรือ Probation
        submit_text = self.browser.find_element_by_id('student_state').text
        self.assertIn('Probation', submit_text)

    def test_can_show_result_when_click_save_button(self):
        # เธอเข้าไปที่หน้า login
        self.browser.get('http://127.0.0.1:8000/accounts/login/')

        username_login_box = self.browser.find_element_by_id("id_username")
        password_login_box = self.browser.find_element_by_id("id_password")

        # test username and password textbox
        # เธอใส่ id password
        username_login_box.send_keys('jesselingard')
        password_login_box.send_keys('lingard123456789')

        # test log in button
        # เธอกดปุ่ม login
        login_button = self.browser.find_element_by_id('login')
        login_button.click()
        time.sleep(3)

        # test save button
        # เธอกดปุ่ม save
        save_button = self.browser.find_element_by_id("save_button")
        save_button.click()

        # test error message
        # เธอไม่ได้เลือกเทอมไว้
        # เธอเห็นคำว่า Please select term before saving grade
        error_message = self.browser.find_element_by_id("forgot_to_select_term").text
        self.assertEqual('Please select term before saving grade',error_message)
        time.sleep(6)

        # test select term
        # เธอเลือกเทอม 1
        select_term = Select(self.browser.find_element_by_id('subjectTermid'))
        select_term.select_by_value('1')

        # test save button
        # เธอกดปุ่ม save
        save_button = self.browser.find_element_by_id("save_button")
        save_button.click()

        # test error message
        # เธอกดเลือกเทอมแล้ว
        # แต่เธอไม่ได้กดเลือกหน่วยกิตและเกรด
        # เธอเห็นคำว่า Plese check your infromation before saving.
        not_input = self.browser.find_element_by_id("GPA_result").text
        self.assertIn('Plese check your infromation before saving.',not_input)
        time.sleep(6)

        # test select term
        # เธอเลือกเทอม 1
        select_term = Select(self.browser.find_element_by_id('subjectTermid'))
        select_term.select_by_value('1')

        # test subject's unit
        # เธอใส่ unit ลงไป
        first_subject_unit = Select(self.browser.find_element_by_id('subject1Unitid'))
        first_subject_unit.select_by_value('3')

        # test subject's grade
        # เธอใส่ Grade ลงไป
        first_subject_grade = Select(self.browser.find_element_by_id('subject1Gradeid'))
        first_subject_grade.select_by_value('4')
        
        # test save button
        # เธอกดปุ่ม save
        save_button = self.browser.find_element_by_id("save_button")
        save_button.click()

        # test GPA result
        # เธอเห็น GPA ของเธอ
        GPA = self.browser.find_element_by_id("GPA_result").text
        self.assertIn('4.0',GPA)
        time.sleep(6)

    def test_can_save_data_and_show_data_in_result_link(self):
        # test log in 's header text
        # เธอเข้าไปที่หน้า login
        self.browser.get('http://127.0.0.1:8000/accounts/login/')

        username_login_box = self.browser.find_element_by_id("id_username")
        password_login_box = self.browser.find_element_by_id("id_password")

        # test username and password textbox
        # เธอใส่ id password
        username_login_box.send_keys('jesselingard')
        password_login_box.send_keys('lingard123456789')

        # test log in button
        # เธอกดปุ่ม login
        login_button = self.browser.find_element_by_id('login')
        login_button.click()
        time.sleep(3)

        # test select term
        # เธอเลือกเทอม 1
        select_term = Select(self.browser.find_element_by_id('subjectTermid'))
        select_term.select_by_value('1')

        # test subject's unit
        # เธอใส่ unit ลงไปทั้งหมด 8 วิชา
        first_subject_unit = Select(self.browser.find_element_by_id('subject1Unitid'))
        first_subject_unit.select_by_value('3')

        second_subject_unit = Select(self.browser.find_element_by_id('subject2Unitid'))
        second_subject_unit.select_by_value('1')

        third_subject_unit = Select(self.browser.find_element_by_id('subject3Unitid'))
        third_subject_unit.select_by_value('3')

        fourth_subject_unit = Select(self.browser.find_element_by_id('subject4Unitid'))
        fourth_subject_unit.select_by_value('3')

        fifth_subject_unit = Select(self.browser.find_element_by_id('subject5Unitid'))
        fifth_subject_unit.select_by_value('3')

        sixth_subject_unit = Select(self.browser.find_element_by_id('subject6Unitid'))
        sixth_subject_unit.select_by_value('3')

        seventh_subject_unit = Select(self.browser.find_element_by_id('subject7Unitid'))
        seventh_subject_unit.select_by_value('3')

        eighth_subject_unit = Select(self.browser.find_element_by_id('subject8Unitid'))
        eighth_subject_unit.select_by_value('3')

        # test subject's grade
        # เธอใส่ Grade ลงไปทั้งหมด 8 วิชา
        first_subject_grade = Select(self.browser.find_element_by_id('subject1Gradeid'))
        first_subject_grade.select_by_value('4')

        second_subject_grade = Select(self.browser.find_element_by_id('subject2Gradeid'))
        second_subject_grade.select_by_value('3')

        third_subject_grade = Select(self.browser.find_element_by_id('subject3Gradeid'))
        third_subject_grade.select_by_value('1')

        fourth_subject_grade = Select(self.browser.find_element_by_id('subject4Gradeid'))
        fourth_subject_grade.select_by_value('1.5')

        fifth_subject_grade = Select(self.browser.find_element_by_id('subject5Gradeid'))
        fifth_subject_grade.select_by_value('2')

        sixth_subject_grade = Select(self.browser.find_element_by_id('subject6Gradeid'))
        sixth_subject_grade.select_by_value('2.5')

        seventh_subject_grade = Select(self.browser.find_element_by_id('subject7Gradeid'))
        seventh_subject_grade.select_by_value('1')

        eighth_subject_grade = Select(self.browser.find_element_by_id('subject8Gradeid'))
        eighth_subject_grade.select_by_value('1.5')

        # test save button
        # เธอกดปุ่ม save
        save_button = self.browser.find_element_by_id("save_button")
        save_button.click()
        time.sleep(6)

        # test select term
        # เธอเลือกเทอม 2
        select_term = Select(self.browser.find_element_by_id('subjectTermid'))
        select_term.select_by_value('2')

        # test subject's unit
        # เธอใส่ unit ลงไปทั้งหมด 6 วิชา
        first_subject_unit = Select(self.browser.find_element_by_id('subject1Unitid'))
        first_subject_unit.select_by_value('3')

        second_subject_unit = Select(self.browser.find_element_by_id('subject2Unitid'))
        second_subject_unit.select_by_value('3')

        third_subject_unit = Select(self.browser.find_element_by_id('subject3Unitid'))
        third_subject_unit.select_by_value('3')

        fourth_subject_unit = Select(self.browser.find_element_by_id('subject4Unitid'))
        fourth_subject_unit.select_by_value('3')

        fifth_subject_unit = Select(self.browser.find_element_by_id('subject5Unitid'))
        fifth_subject_unit.select_by_value('3')

        sixth_subject_unit = Select(self.browser.find_element_by_id('subject6Unitid'))
        sixth_subject_unit.select_by_value('3')

        # test subject's grade
        # เธอใส่ Grade ลงไปทั้งหมด 6 วิชา
        first_subject_grade = Select(self.browser.find_element_by_id('subject1Gradeid'))
        first_subject_grade.select_by_value('4')

        second_subject_grade = Select(self.browser.find_element_by_id('subject2Gradeid'))
        second_subject_grade.select_by_value('2.5')

        third_subject_grade = Select(self.browser.find_element_by_id('subject3Gradeid'))
        third_subject_grade.select_by_value('3')

        fourth_subject_grade = Select(self.browser.find_element_by_id('subject4Gradeid'))
        fourth_subject_grade.select_by_value('4')

        fifth_subject_grade = Select(self.browser.find_element_by_id('subject5Gradeid'))
        fifth_subject_grade.select_by_value('2')

        sixth_subject_grade = Select(self.browser.find_element_by_id('subject6Gradeid'))
        sixth_subject_grade.select_by_value('2.5')

        # test save button
        # เธอกดปุ่ม save
        save_button = self.browser.find_element_by_id("save_button")
        save_button.click()
        time.sleep(6)

        # test RESULT link
        # เธอคลิกไปที่ RESULT link
        result = self.browser.find_element_by_partial_link_text('RESULT')
        result.click()
        time.sleep(3)

        # เธอเลือก Term 1
        term_result = self.browser.find_element_by_id('first_term_result')
        term_result.click()
        time.sleep(6)

        # เธอเห็น TERM 1 
        term_header = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual('TERM 1',term_header)

        # เธอเห็นคำว่า No.
        number = self.browser.find_element_by_id('num').text
        self.assertEqual('No.',number)

        # เธอเห็นคำว่า Subject
        subject = self.browser.find_element_by_id('sub').text
        self.assertEqual('Subject',subject)

        # เธอเห็นคำว่า Unit
        unit = self.browser.find_element_by_id('unt').text
        self.assertEqual('Unit',unit)

        # เธอเห็นคำว่า Grade
        grade = self.browser.find_element_by_id('grd').text
        self.assertEqual('Grade',grade)

        # เธอเห็นอันดับแรกซึ่งคือเลข 1
        subject_number = self.browser.find_element_by_id('nmbr').text
        self.assertIn('1',subject_number)

        # เธอเห็นหน่วยกิต
        first_unit = self.browser.find_element_by_class_name('table').text
        self.assertIn('3',first_unit)

        second_unit = self.browser.find_element_by_class_name('table').text
        self.assertIn('1',second_unit)

        # เธอเห็นเกรดของแต่ละวิชา
        first_grade = self.browser.find_element_by_tag_name('table').text
        self.assertIn('4',first_grade)

        second_grade = self.browser.find_element_by_tag_name('table').text
        self.assertIn('3',second_grade)

        # เธอเห็นเกรดในเทอม 1
        GPA = self.browser.find_element_by_id("GPA_first_term").text
        self.assertIn('1.98',GPA)

        # เธอเห็นเกรดรวมในทุกเทอม
        GPAX = self.browser.find_element_by_id("GPAX").text
        self.assertIn('2.49',GPAX)

        # test RESULT link
        # เธอคลิกไปที่ RESULT link
        result = self.browser.find_element_by_partial_link_text('RESULT')
        result.click()
        time.sleep(3)

        # เธอเลือก Term 2
        term_result = self.browser.find_element_by_id('second_term_result')
        term_result.click()
        time.sleep(6)

        # เธอเห็นหน่วยกิต
        second_term_unit = self.browser.find_element_by_class_name('table').text
        self.assertIn('3',second_term_unit)

        # เธอเห็นเกรดของแต่ละวิชา
        second_term_first_grade = self.browser.find_element_by_tag_name('table').text
        self.assertIn('4',second_term_first_grade)

        second_term_second_grade = self.browser.find_element_by_tag_name('table').text
        self.assertIn('2.5',second_term_second_grade)

        # เธอเห็นเกรดในเทอม 2
        GPA = self.browser.find_element_by_id("GPA_second_term").text
        self.assertIn('3.00',GPA)

        # เธอเห็นเกรดรวมในทุกเทอม
        GPAX = self.browser.find_element_by_id("GPAX").text
        self.assertIn('2.49',GPAX)

    def test_can_click_to_graph_link(self):
        # test log in 's header text
        # เธอเข้าไปที่หน้า login
        self.browser.get('http://127.0.0.1:8000/accounts/login/')

        username_login_box = self.browser.find_element_by_id("id_username")
        password_login_box = self.browser.find_element_by_id("id_password")

        # test username and password textbox
        # เธอใส่ id password
        username_login_box.send_keys('jesselingard')
        password_login_box.send_keys('lingard123456789')

        # test log in button
        # เธอกดปุ่ม login
        login_button = self.browser.find_element_by_id('login')
        login_button.click()
        time.sleep(3)

        # test select term
        # เธอเลือกเทอม 1
        select_term = Select(self.browser.find_element_by_id('subjectTermid'))
        select_term.select_by_value('1')

        # test subject's unit
        # เธอใส่ unit ลงไป
        first_subject_unit = Select(self.browser.find_element_by_id('subject1Unitid'))
        first_subject_unit.select_by_value('3')

        # test subject's grade
        # เธอใส่ Grade ลงไป
        first_subject_grade = Select(self.browser.find_element_by_id('subject1Gradeid'))
        first_subject_grade.select_by_value('4')

        # test save button
        # เธอกดปุ่ม save
        save_button = self.browser.find_element_by_id("save_button")
        save_button.click()
        time.sleep(6)

        # test GRAPH link
        # เธอคลิกไปที่ GRAPH link
        graph = self.browser.find_element_by_partial_link_text('GRAPH')
        graph.click()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
