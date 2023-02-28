from PySide6.QtWidgets import (QGroupBox, QFileDialog)
from PySide6.QtCore import (Signal, Slot, QThread, QObject)
from shutil import rmtree
from os import (mkdir, listdir, path)
from PIL import Image


class DropGroupBox(QGroupBox):

    def __init__(self, parent=None):
        super().__init__(parent)

    def dragEnterEvent(self, event):
        self.path = event.mimeData().urls()[0].toLocalFile()
        self.setPath.emit(self.path)


class RemoveWorker(QObject):
    isDone = Signal()

    @Slot(str)
    def do_its_job(self, path):
        try:
            rmtree(path)
        except:
            print("删除失败")
        self.isDone.emit()


class DeleteToolGroupBox(DropGroupBox):
    setPath = Signal(str)
    setStatus = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.worker = RemoveWorker()
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        self.setPath.connect(self.worker.do_its_job)
        self.worker_thread.started.connect(self.startedStatus)
        self.worker.isDone.connect(self.worker_thread.exit)
        self.worker.isDone.connect(self.finishedStatus)

    @Slot()
    def startedStatus(self):
        self.setStatus.emit("正在删除")

    @Slot()
    def finishedStatus(self):
        self.setStatus.emit("删除完成")

    @Slot()
    def clickToolButton(self):
        self.path = QFileDialog.getExistingDirectory(self)
        if (self.path):
            self.setPath.emit(self.path)

    @Slot()
    def clickPushButton(self):
        try:
            self.worker_thread.start()
        except:
            print("删除线程创建失败")

class ConvertWorker(QObject):
    isDone = Signal()
    Now = Signal(int)

    def convertjpg(self, jpgfile, outdir, width=128, height=128):
        img = Image.open(jpgfile)
        try:
            new_img = img.resize((width, height), Image.BILINEAR)
            new_img.save(path.join(outdir, path.basename(jpgfile)))
        except Exception as e:
            print(e)

    def convertEntireFolder(self, folder_path, size=128):
        old_folder_name = path.basename(folder_path)
        new_folder_path = path.dirname(
            folder_path) + "/" + old_folder_name + "_converted_" + str(size)
        try:
            mkdir(new_folder_path)
        except:
            print("文件夹已存在")
        now_count = 0
        for jpgfile in listdir(folder_path):
            self.convertjpg(folder_path+"/"+jpgfile,
                            new_folder_path+"/", size, size)
            now_count += 1
            self.Now.emit(now_count)

    @Slot(str, int)
    def do_its_job(self, folder_path, size):
        self.convertEntireFolder(folder_path, size)
        self.isDone.emit()

class ConvertToolGroupBox(DropGroupBox):
    setPath = Signal(str)
    sendPathAndSizeToWorker = Signal(str, int)
    setMax = Signal(int)
    setNow = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.size = 128  # default size
        self.file_count = 0  # default file count
        self.worker = ConvertWorker()
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        self.sendPathAndSizeToWorker.connect(self.worker.do_its_job)
        self.worker.Now.connect(self.setSignalNow)
        self.worker.isDone.connect(self.worker_thread.exit)

    @Slot(int)
    def setSignalNow(self, now):
        self.setNow.emit(now)

    @Slot()
    def clickToolButton(self):
        self.path = QFileDialog.getExistingDirectory(self)
        if (self.path):
            self.setPath.emit(self.path)
            for _ in listdir(self.path):
                self.file_count = self.file_count + 1  # count the number of files in the folder
            self.setMax.emit(self.file_count)

    @Slot(str)
    def setSize(self, size):
        if size.isnumeric():
            self.size = int(size)

    @Slot()
    def clickPushButton(self):
        try:
            self.sendPathAndSizeToWorker.emit(self.path, self.size)
            self.worker_thread.start()
        except:
            print("转换失败")
