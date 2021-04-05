import json

class Settings:
    @staticmethod
    def setUp(window):
        """SetUp settings"""
        with open('settings.json') as file:
            settings = json.load(file)

        #load theme
        path = "styles/{0}.txt".format(settings['Theme'].replace(' ',''))
        with open(path) as theme:
            window.setStyleSheet(theme.read())

        #Translate
        if settings['Language'] == "English":
            with open("languages/EN.json") as lang:
                Settings._set_lang(json.load(lang),window)
        else:
            with open("languages/RU.json",encoding='utf-8') as lang:
                Settings._set_lang(json.load(lang),window)

    @staticmethod
    def _set_lang(dict,window):
        """Set language in each window"""

        if window.objectName() == "MainWindow":
            window.menuLoad.setTitle(dict["menuLoad"])
            window.label_active_session.setText(dict["label_active_session"])
            window.actionLoad_mails.setText(dict["actionLoad_mails"])
            window.menuChoose_session.setTitle(dict["menuChoose_session"])
            window.actionAdd_Session.setText(dict["actionAdd_Session"])
            window.actionDelete_Session.setText(dict["actionDelete_Session"])
            window.menuSettings.setTitle(dict["menuSettings"])
            window.actionSettings.setText(dict["actionSettings"])
            window.groupBox_Statistic.setTitle(dict['groupBox_Statistic'])
            window.label_accounts.setText(dict["label_accounts"])
            window.label_checked.setText(dict["label_checked"])
            window.label_unvalid.setText(dict["label_unvalid"])
            window.label_valid.setText(dict["label_valid"])
            window.treeWidget.headerItem().setText(0,dict["treeWidget_main_window_0"])
            window.treeWidget.headerItem().setText(1,dict["treeWidget_main_window_1"])
            window.treeWidget.headerItem().setText(2,dict["treeWidget_main_window_2"])
            window.treeWidget.headerItem().setText(3,dict["treeWidget_main_window_3"])
            window.groupBox_Filter.setTitle(dict["groupBox_Filter"])
            window.checkBox_Date.setText(dict["checkBox_Date"])
            window.checkBox_Only_Seen.setText(dict["checkBox_Only_Seen"])
            window.label_display_letters_from.setText(dict["label_display_letters_from"])
            window.groupBox_Requests.setTitle(dict["groupBox_Requests"])
            window.checkBox_Search.setText(dict["checkBox_Search"])
            window.label_from.setText(dict["label_from"])
            window.label_subject.setText(dict["label_subject"])
            window.label_body.setText(dict["label_body"])
            window.pushButton_Search.setText(dict["pushButton_Search"])

        if window.objectName() == "SettingsWindow":
            window.setWindowTitle(dict["setting_title"])
            window.groupBox_Language.setTitle(dict["groupBox_Language"])
            window.radioButton_English.setText(dict["radioButton_English"])
            window.radioButton_Russian.setText(dict["radioButton_Russian"])
            window.groupBox_Theme.setTitle(dict["groupBox_Theme"])
            window.radioButton_DarkTheme.setText(dict["radioButton_DarkTheme"])
            window.radioButton_LightTheme.setText(dict["radioButton_LightTheme"])
            window.groupBox_Save.setTitle(dict["groupBox_Save"])
            window.pushButton_Browse.setText(dict["pushButton_Browse"])
            window.pushButton_Save_Settings.setText(dict['pushButton_Save_Settings'])

        if window.objectName() == "PrevWindow":
            window.setWindowTitle(dict["prevload_title"])
            window.pushButton_Cancel_Load.setText(dict["pushButton_Cancel_Load"])
            window.pushButton_load_data_link.setText(dict["pushButton_load_data_link"])
            window.pushButton_swap_file.setText(dict["pushButton_swap_file"])
            window.pushButton_load_data_file.setText(dict["pushButton_load_data_file"])
            window.pushButton_swap_link.setText(dict["pushButton_swap_link"])
            window.pushButton_load_file.setText(dict["pushButton_load_file"])

        if window.objectName() == "MailsWindow":
            window.groupBox_Download.setTitle(dict["groupBox_Download"])
            window.setWindowTitle(dict["mailswindow_title"])
            window.pushButton_Download_All.setText(dict["pushButton_Download_All"])
            window.pushButton_Download_Selected.setText(dict["pushButton_Download_Selected"])
            window.treeWidget.headerItem().setText(0, dict["treeWidget_mails_window_0"])
            window.treeWidget.headerItem().setText(1, dict["treeWidget_mails_window_1"])
            window.treeWidget.headerItem().setText(2, dict["treeWidget_mails_window_2"])
            window.treeWidget.headerItem().setText(3, dict["treeWidget_mails_window_3"])

