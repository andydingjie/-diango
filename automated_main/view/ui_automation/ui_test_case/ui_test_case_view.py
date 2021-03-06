# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 18:45
# @Author  : wangyinghao
# @FileName: ui_test_case_view.py
# @Software: PyCharm
from django.views.generic import View
import json
import time
from django.forms import model_to_dict
from automated_main.utils.http_format import response_success, response_failed
from automated_main.exception.my_exception import MyException
from automated_main.models.ui_automation.ui_test_case import UITestCase, UITestCaseAssociated
from automated_main.models.ui_automation.ui_project import UIProject
from automated_main.models.ui_automation.ui_page import UIPage
from automated_main.models.ui_automation.ui_page_element import UIPageElement
from automated_main.models.ui_automation.ui_element_operation import UIElementsOperation
from automated_main.form.ui_test_case import UiTestCaseForm
from selenium import webdriver
from automated_main.view.ui_automation.ui_test_case.ui_automation import base
import logging

logger = logging.getLogger('django')


class UITestCaseView(View):

    def get(self, request, ui_test_case_id, *args, **kwargs):
        """
        代表获取单个测试用例
        :param request:
        :param ui_test_case_id:
        :param args:
        :param kwargs:
        :return:
        """
        ui_test_case = UITestCase.objects.get(id=ui_test_case_id)
        ui_associated = UITestCaseAssociated.objects.filter(cid_id=ui_test_case_id)
        if ui_test_case is None:
            return response_success()
        else:
            ui_test_case_data_list = []
            for ui_associateds in ui_associated:
                ui_elements = UIPageElement.objects.get(id=ui_associateds.ui_page_elements_id)
                ui_associated_dict = {
                    "ui_page_id": ui_elements.ui_page_id,
                    "ui_associateds_id": ui_associateds.id,
                    "ui_page_element_id": ui_associateds.ui_page_elements_id,
                    "ui_element_operation_id": ui_associateds.element_operation,
                    "elements_output": ui_associateds.element_input,
                    "x_coordinates": ui_associateds.x_coordinates,
                    "y_coordinates": ui_associateds.y_coordinates,
                    "waiting_time": ui_associateds.waiting_time,
                    "steps": int(ui_associateds.case_steps),
                }
                ui_test_case_data_list.append(ui_associated_dict)
            ui_test_case_data_list_sorting = sorted(ui_test_case_data_list, key=lambda x: x['steps'])

            return response_success(
                {"ui_test_case_name": ui_test_case.ui_test_case_name, "ui_project_id": ui_test_case.ui_project_id,
                 "ui_test_case_data": ui_test_case_data_list_sorting})

    def post(self, request, ui_test_case_id, *args, **kwargs):
        """
        代表更改UI测试用例
        :param request:
        :param ui_test_case_id:
        :param args:
        :param kwargs:
        :return:
        """

        ui_test_case = UITestCase.objects.get(id=ui_test_case_id)
        if ui_test_case is None:
            return response_success()
        body = request.body
        if not body:
            return response_success()
        data = json.loads(body)
        form = UiTestCaseForm(data)

        for i in data["ui_test_case_data"]:
            ui_page_elements_id = (i['ui_page_element_id'])
            elements_operation = (i['ui_element_operation_id'])
            waiting_time = (i['waiting_time'])
            case_steps = (i['steps'])

            if elements_operation == "":
                return response_failed(30000, "元素操作未选择")

            if ui_page_elements_id == "":
                return response_failed(30000, "UI页面元素未选择")
            if case_steps == "":
                return response_failed(30000, "操作步骤未填写")
            if waiting_time == "":
                return response_failed(30000, "等待时间未填写")

        ui_test_case.ui_test_case_name = data['ui_test_case_name']
        ui_test_case.ui_project_id = data['ui_project_id']
        ui_test_case.id = data['ui_test_case_id']
        ui_test_case.save()
        UITestCaseAssociated.objects.filter(cid_id=ui_test_case_id).delete()

        if form.is_valid():
            for i in data["ui_test_case_data"]:
                ui_page_elements_id = (i['ui_page_element_id'])
                elements_operation = (i['ui_element_operation_id'])
                waiting_time = (i['waiting_time'])
                case_steps = (i['steps'])
                page_elements_output = (i['elements_output'])
                x_coordinates = (i['x_coordinates'])
                y_coordinates = (i['y_coordinates'])

                UITestCaseAssociated.objects.create(cid_id=ui_test_case_id, element_operation=elements_operation,
                                                    element_input=page_elements_output, x_coordinates=x_coordinates,
                                                    y_coordinates=y_coordinates, waiting_time=waiting_time,
                                                    case_steps=case_steps, ui_page_elements_id=ui_page_elements_id)
            return response_success("编辑UI测试用例成功")
        else:
            raise MyException()

    def delete(self, request, ui_test_case_id, *args, **kwargs):
        """
        代表删除测试用例
        :param request:
        :param ui_test_case_id:
        :param args:
        :param kwargs:
        :return:
        """

        UITestCase.objects.get(id=ui_test_case_id).delete()
        return response_success("删除UI测试用例成功")

    def put(self, request, *args, **kwargs):
        """
        代表创建UI测试用例
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        body = request.body
        if not body:
            return response_success()
        data = json.loads(body)

        form = UiTestCaseForm(data)
        if form.is_valid():
            ui_test_case = UITestCase.objects.create(**form.cleaned_data)
            ui_test_case_id = ui_test_case.id
            print(data["ui_test_case_data"])

            for i in data["ui_test_case_data"]:
                ui_page_element_id = (i['ui_page_element_id'])
                elements_operation = (i['ui_element_operation_id'])
                waiting_time = (i['waiting_time'])
                case_steps = (i['steps'])
                page_elements_output = (i['elements_output'])
                x_coordinates = (i['x_coordinates'])
                y_coordinates = (i['y_coordinates'])
                if elements_operation == "":
                    ui_test_case.delete()
                    return response_failed(30000, "元素操作未选择")

                if ui_page_element_id == "":
                    ui_test_case.delete()
                    return response_failed(30000, "UI页面元素未选择")
                if case_steps == "":
                    ui_test_case.delete()
                    return response_failed(30000, "操作步骤未填写")
                if waiting_time == "":
                    ui_test_case.delete()
                    return response_failed(30000, "等待时间未填写")
                UITestCaseAssociated.objects.create(cid_id=ui_test_case_id, element_operation=elements_operation,
                                                    element_input=page_elements_output, waiting_time=waiting_time,
                                                    case_steps=case_steps, ui_page_elements_id=ui_page_element_id,
                                                    x_coordinates=x_coordinates, y_coordinates=y_coordinates)

            return response_success("创建UI测试用例成功")
        else:
            raise MyException()


class GetUiTestCaseSelectData(View):

    def get(self, request, *args, **kwargs):
        """
        三级联动---“UI项目>UI页面>UI页面元素”
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ui_projects = UIProject.objects.all()
        data_list = []
        for project in ui_projects:
            project_dict = {
                "project_id": project.id,
                "ui_project_name": project.ui_project_name
            }

            ui_pages = UIPage.objects.filter(ui_project_id=project.id)
            page_list = []
            for ui_page in ui_pages:
                ui_page_elements = UIPageElement.objects.filter(ui_page_id=ui_page.id)
                ui_page_element_list = []
                for ui_page_element in ui_page_elements:
                    ui_page_element_list.append({
                        "ui_page_element_id": ui_page_element.id,
                        "ui_page_element_name": ui_page_element.ui_page_element_name,

                    })

                page_list.append({
                    "ui_page_id": ui_page.id,
                    "ui_page_name": ui_page.ui_page_name,
                    "ui_element_list": ui_page_element_list,
                })

            project_dict["page_list"] = page_list

            data_list.append(project_dict)

        return response_success(data_list)


class UiTestCaseDeBug(View):

    def post(self, request, *args, **kwargs):
        """
        UI测试用例得调试
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        debug_results = ""
        debug_results_message = ""

        data = request.body
        ui_case_data = json.loads(data)

        logger.info(ui_case_data)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('no-sandbox')
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
        bases = base.BaseCommon(driver)

        for i in ui_case_data["ui_test_case_data"]:
            ui_page_id = (i['ui_page_id'])
            ui_elements_id = (i['ui_page_element_id'])
            elements_operation_id = (i['ui_element_operation_id'])
            waiting_time = (i['waiting_time'])
            steps = (i['steps'])
            try:
                page_elements_output = (i['elements_output'])
                x_coordinates = (i['x_coordinates'])
                y_coordinates = (i['y_coordinates'])
            except Exception as e:
                pass
            elements_operation = UIElementsOperation.objects.get(id=elements_operation_id)
            page_element = UIPageElement.objects.get(id=ui_elements_id)
            print(type(page_element.ui_page_element_more))
            element_more = None
            if page_element.ui_page_element_more == "" or page_element.ui_page_element_more is None:
                element_more = None
            else:
                element_more = int(page_element.ui_page_element_more)

            try:
                if elements_operation.elements_operation_name == "open_url":
                    bases.open_url(page_element.ui_page_element)
                    driver.maximize_window()
                    time.sleep(int(waiting_time))
                    logger.info("打开url" + str(page_element.ui_page_element))

                if elements_operation.elements_operation_name == "send_keys":
                    bases.send_keys(page_element.ui_element_positioning.locating_method, page_element.ui_page_element,
                                    page_elements_output, element_more)
                    time.sleep(int(waiting_time))
                    logger.info("元素输入操作：" + str(page_element.ui_page_element_name))

                if elements_operation.elements_operation_name == "click":
                    bases.click(page_element.ui_element_positioning.locating_method, page_element.ui_page_element, element_more)
                    time.sleep(int(waiting_time))
                    logger.info("元素点击操作：" + str(page_element.ui_page_element_name))

                if elements_operation.elements_operation_name == "double_click":
                    bases.double_click(page_element.ui_element_positioning.locating_method,
                                       page_element.ui_page_element, element_more)
                    time.sleep(int(waiting_time))
                    logger.info("元素双击操作：" + str(page_element.ui_page_element_name))

                if elements_operation.elements_operation_name == "ifram":
                    bases.switch_frame(page_element.ui_page_element)
                    time.sleep(int(waiting_time))
                    logger.info("进入ifram：" + str(page_element.ui_page_element_name))

                if elements_operation.elements_operation_name == "switch_to_alert":
                    bases.switch_to_alert(page_element.ui_element_positioning.locating_method,
                                          page_element.ui_page_element)
                    time.sleep(int(waiting_time))
                    logger.info("切换alert窗口：" + str(page_element.ui_page_element_name))

                if elements_operation.elements_operation_name == "click_and_hold":
                    bases.click_and_hold(page_element.ui_element_positioning.locating_method,
                                         page_element.ui_page_element, element_more)
                    time.sleep(int(waiting_time))
                    logger.info("鼠标长按左键：" + str(page_element.ui_page_element_name))

                if elements_operation.elements_operation_name == "get_page_title":
                    bases.get_page_title()
                    time.sleep(int(waiting_time))
                    logger.info("获取网页Title:" + str(page_element.ui_page_element_name))

                if elements_operation.elements_operation_name == "set_timeout":
                    bases.set_timeout()
                    time.sleep(int(waiting_time))
                    logger.info("设置超时时间:" + str(page_element.ui_page_element_name))

                if elements_operation.elements_operation_name == "drag_and_drop":
                    bases.drag_and_drop(page_element.ui_element_positioning.locating_method,
                                        page_element.ui_page_element, x_coordinates, y_coordinates, element_more)
                    time.sleep(int(waiting_time))
                    logger.info("拖拽元素:" + str(page_element.ui_page_element_name))

                if elements_operation.elements_operation_name == "script":
                    bases.script(page_element.ui_element_positioning.locating_method, page_element.ui_page_element,
                                 x_coordinates, y_coordinates, element_more)
                    time.sleep(int(waiting_time))
                    logger.info("滑动滚动条:" + str(page_element.ui_page_element_name))

                if elements_operation.elements_operation_name == "mouse_suspension":
                    bases.mouse_suspension(page_element.ui_element_positioning.locating_method,
                                           page_element.ui_page_element, element_more)
                    time.sleep(int(waiting_time))
                    logger.info("鼠标悬浮:" + str(page_element.ui_page_element_name))

                if elements_operation.elements_operation_name == "change_window_handle":
                    bases.change_window_handle()
                    time.sleep(int(waiting_time))
                    logger.info("切换窗口:" + str(page_element.ui_page_element_name))

                if elements_operation.elements_operation_name == "copy":
                    bases.copy()
                    time.sleep(int(waiting_time))
                    logger.info("复制粘贴:" + str(page_element.ui_page_element_name))

                if elements_operation.elements_operation_name == "keyboard_clear_contents":
                    bases.keyboard_clear_contents(page_element.ui_element_positioning.locating_method,
                                                  page_elements_output)
                    time.sleep(int(waiting_time))
                    logger.info("利用键盘清空输入框内容:" + str(page_element.ui_page_element_name))
            except Exception as e:
                logger.info("这是错误的步骤: " + str(steps))
                logger.info("这是异常信息: " + str(e))

                debug_results = "这是错误的步骤: " + str(steps)
                debug_results_message = "这是异常信息: " + str(e)
                driver.quit()
                return response_failed(3000, {"debug_results": debug_results,
                                              "debug_results_message": debug_results_message}
                                       )
        driver.quit()

        return response_success({"debug_results": debug_results,
                                 "debug_results_message": debug_results_message})
