#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AdminPortal1.1.py
#
#  Copyright 2017 AVELAZCX <aldo.alfonsox.velasco.meza@intel.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.


""" NEED ADD TEST CASE """


import unittest
import xmlrunner
import HtmlTestRunner
from selenium import webdriver
from  datetime import datetime
from colorama import init,Fore, Back, Style
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class AdminPortalAutoTest(unittest.TestCase):
    init(autoreset=True)
    print(Back.GREEN + Fore.WHITE + "\n<======================== Win Admin Portal ========================>")
    print(Fore.GREEN + "-------------------------------------------------------------------")
    print(Fore.MAGENTA + """                            AVELAZCX
            """)


    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome("C:\Python36x64\WebDrivers\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("http://zpn-rng08/admin/#/welcome")

    def test_1_TC10517_Metrics_Telemetry_Section_Admin_Portal(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
        self.search_field = self.driver.find_element_by_id("username").clear()
        # self.driver.find_element_by_id("username").send_keys("TELMEX")
        # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
        # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()

    def test_2_TC10518_Metrics_Telemetry_Calendar_Fields(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
    #    self.search_field = self.driver.find_element_by_id("username").clear()
    #    self.driver.find_element_by_id("username").send_keys("TELMEX")
    #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
    #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()

    def test_3_TC10519_Metrics_Telemetry_FQDN_Field(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
        self.search_field = self.driver.find_element_by_id("usernsssame")
        self.search_field.clear()
        self.search_field.send_keys("TELMECO")
#
##
    def test_4_TC10520_Metrics_Telemetry_Reset_Button(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##       self.search_field = self.driver.find_element_by_id("username")
# ##       self.search_field.clear()
# ##       self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_5_TC10521_Metrics_Telemetry_Refresh_Button(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##       self.search_field = self.driver.find_element_by_id("password")
# ##       self.search_field.clear()
# ##       self.search_field.send_keys("jljdslfksjdf")
#
    def test_6_TC10522_Metrics_Telemetry_Show_BottomTop_ten_Rooms_Button(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_7_TC10523_Metrics_Telemetry_Export_Raw_Data_Button(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_8_TC10524_Metrics_Telemetry_Graphics(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##       self.search_field = self.driver.find_element_by_id("usernsssame")
# ##       self.search_field.clear()
# ##       self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_9_TC10536_SP_StaticPin_Property_True(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##       self.search_field = self.driver.find_element_by_id("username")
# ##       self.search_field.clear()
# ##       self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_10_TC10537_SP_StaticPin_Property_False(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##       self.search_field = self.driver.find_element_by_id("password")
# ##       self.search_field.clear()
# ##       self.search_field.send_keys("jljdslfksjdf")
#
    def test_11_TC10539_TP_TransparentPin_Normal(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_12_TC10540_TP_TransparentPin_Less_Than_50(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_13_TC10541_TP_TransparentPin_0(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##       self.search_field = self.driver.find_element_by_id("usernsssame")
# ##       self.search_field.clear()
# ##       self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_14_TC10542_TP_TransparentPin_Less_Than_0(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##       self.search_field = self.driver.find_element_by_id("username")
# ##       self.search_field.clear()
# ##       self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_15_TC10546_DRV_Disable_Remote_View_False(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##       self.search_field = self.driver.find_element_by_id("password")
# ##       self.search_field.clear()
# ##       self.search_field.send_keys("jljdslfksjdf")
#
    def test_16_TC10547_DRV_Disable_Remote_View_True(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         #self.search_field = self.driver.find_element_by_id("username").clear()
#         #self.driver.find_element_by_id("username").send_keys("TELMEX")
#         #self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         #self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_17_TC10543_RP_Reserve_PIN(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_18_TC10544_RP_Reserve_PIN_In_Use_PIN(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_19_TC10545_RP_UnReserve_PIN(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_20_TC10525_MM_Admin_Portal_Moderators_Add(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_21_TC10526_MM_Admin_Portal_Moderators_Add_Using_CSV_File(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_22_TC10527_MM_Admin_Portal_Moderators_Remove(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_23_TC10528_MM_Admin_Portal_Moderators_Remove_Using_CSV_File(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_24_TC10529_MM_Admin_Portal_Moderators_Remove_Bulk(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_25_TC10530_MM_Admin_Portal_Moderators_Send_Token(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_26_TC10531_MM_Admin_Portal_Moderators_Send_Token_Bulk(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_27_TC10532_MM_Admin_Portal_Moderators_CSV_Different_Actions(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_28_TC10533_MM_Admin_Portal_Moderators_CSV_Wrong_Number_Of_Colums(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_29_TC10534_MM_Admin_Portal_Moderators_CSV_Wrong_Email_Format(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_30_TC10535_MM_Admin_Portal_Moderators_CSV_Wrong_Actions(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_31_TC10461_Do_a_valid_user_registration(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_32_TC10462_Do_an_invalid_email_user_registration(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_33_TC10463_Do_an_invalid_password_user_registration(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_34_TC10464_Login_with_an_invalid_account(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_35_TC10465_Login_with_an_invalid_password(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_36_TC10466_Login_without_user_password(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_37_TC10467_Login_Lock_feature(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_38_TC10469_Homescreen_Active_devices(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_39_TC10471_CreateEdit_Device_data(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_40_TC10472_Delete_device_data(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_41_TC10473_Incorrect_Device_metadata_input(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_42_TC10474_CreateEdit_Device_groups(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_43_TC10475_Delete_device_groups(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_44_TC10476_Cancel_device_group_deletion(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_45_TC10477_Incorrect_Device_groups_input(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_46_TC10478_Groups_devices_list(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_47_TC10479_AddRemove_device_from_group(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_48_TC10480_Create_Profiles(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_49_TC10481_Incorrect_profile_creation(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_50_TC10482_Delete_profiles(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_51_TC10483_Cancel_profile_deletion(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_52_TC10484_Assign_a_Device_to_a_profile(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_53_TC10485_Assign_a_device_to_another_profile(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_54_TC10486_Remove_a_device_from_a_profile(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_55_TC10487_Change_Profile_properties(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_56_TC10488_Create_Server_properties(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_57_TC10489_Incorrect_server_property_creation(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_58_TC10490_Modify_server_properties(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_59_TC10491_Incorrect_server_properties_edit(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_60_TC10492_Copy_of_Delete_server_properties(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_61_TC10493_Cancel_server_property_deletion(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_62_TC10498_Delete_user(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_63_TC10499_Cancel_user_deletion(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_64_TC10500_Create_Roles(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_65_TC10501_Incorrect_role_creation(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_66_TC10502_Modify_role(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()

    def test_67_TC10503_Incorrect_role_edit(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_68_TC10504_Delete_role(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_69_TC10505_Cancel_role_deletion(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# #
    def test_70_TC10507_Rmove_a_user_Role(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_71_TC10508_Select_and_deselect_permission_on_a_role(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()

    def test_72_TC10509_Chart_information(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_73_TC10510_Log_off(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# #
    def test_74_TC10511_Access_a_restricted_screen(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_75_TC10512_Request_Higher_access(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_76_TC10513_Change_Password(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_77_TC10514_Change_password_incorrectly(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_78_TC10515_Connect_a_new_device_to_ranger(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_79_TC10516_Disconnect_a_device_from_ranger(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_80_TC10548_Client_WebRTC_Show_AV_Toggle(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_81_TC10549_Client_WebRTC_Hide_AV_Toggle(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_82_TC10551_Client_WebRTC_Autocreation_LastValue_Variable(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_83_TC10552_Client_WebRTC_Toggle_Reminder_LastValue(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_84_TC10553_Client_Slide_Set_Off_and_AdminPortal_OFF(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_85_TC10555_Client_AvToggleLastValue_ON_and_ShowAvToggle_Not_Created(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_86_TC11220_AP_Removed_Registration_NoLog(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_87_TC11221_AP_Removed_Registration_LogIn(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_88_TC11222_AP_Erasable_Default(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_89_TC11223_AP_Default_NonSelf_Erasable(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_90_TC11224_AP_Default_NonSelf_Erasable(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_91_TC11226_AP_Default_Role_No_Permissions(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
    def test_92_TC11227_AP_Default_No_Permissions_Upgrade(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#     #    self.search_field = self.driver.find_element_by_id("username").clear()
#     #    self.driver.find_element_by_id("username").send_keys("TELMEX")
#     #    self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#     #    self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()
#
#
    def test_93_TC11229_AP_Reset_Pass_Message_Right(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("usernsssame")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_94_TC11230_AP_Reset_Pass_Message_Wrong(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("username")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("TELMECO")
# ##
# ##
    def test_95_TC11231_AP_Email_Regex_Domain_Uppercase(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
# ##        self.search_field = self.driver.find_element_by_id("password")
# ##        self.search_field.clear()
# ##        self.search_field.send_keys("jljdslfksjdf")
#
    def test_96_TC11232_AP_Email_Regex_User_Uppercase(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()

    def test_96_TC11233_AP_Email_Regex_Closed_Pattern(self):
        self.driver.get("http://zpn-rng08/admin/#/welcome")
#         # self.search_field = self.driver.find_element_by_id("username").clear()
#         # self.driver.find_element_by_id("username").send_keys("TELMEX")
#         # self.search_field = self.driver.find_element_by_id("password").send_keys("1060469260")
#         # self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input").click()



    def tearDown(self):
        # close the browser window
        self.driver.quit()
        print(Fore.YELLOW +"\n====== * Time Result * =======  ", datetime.now())




if __name__ == '__main__':
    print(Fore.YELLOW +"\t\t ==== Test in progress ====\n")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'),failfast=False, buffer=False, catchbreak=False,verbosity=2)
    #testRunner=xmlrunner.XMLTestRunner(output='test-reports')
