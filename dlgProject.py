import sys
from PyQt5.QtWidgets import QApplication, QDialog
from dlgProject import Ui_dlgProject  # 변환된 UI 파일

class ProjectDialog(QDialog, Ui_dlgProject):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 버튼 기능 연결
        self.pbOK.clicked.connect(self.save_project)
        self.pbCancel.clicked.connect(self.close)

    def save_project(self):
        project_name = self.leProjectName.text()
        project_description = self.teDescription.toPlainText()
        print(f"프로젝트 이름: {project_name}")
        print(f"프로젝트 설명: {project_description}")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = ProjectDialog()
    dialog.show()
    sys.exit(app.exec_())
