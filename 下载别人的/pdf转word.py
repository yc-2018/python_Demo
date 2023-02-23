import PySimpleGUI as sg
from pathlib import Path
from pdf2docx import Converter
from threading import Thread
from queue import Queue

RUNNING = False
message_queue = Queue()


def parse(file_path):
    global RUNNING
    RUNNING = True
    try:
        path = Path(file_path)
        output_file = path.parent.joinpath("output.docx")
        cv = Converter(file_path)
        cv.convert(str(output_file))
        cv.close()
        message_queue.put(True)
    except:
        message_queue.put(False)
    RUNNING = False


def make_window():
    layout = [
        [
            sg.Input(readonly=True, key="-file_path-"),
            sg.FileBrowse("选择pdf", file_types=(("PDF文件 *.pdf", "*.* *"),))
        ],
        [sg.Button("开始转换", key="-start-")]
    ]
    return sg.Window("pdf转word工具", layout=layout, finalize=True)


if __name__ == '__main__':
    main_window = make_window()
    success_window = None
    while True:
        window, event, values = sg.read_all_windows(timeout=20)
        if window == main_window:
            if event == sg.WIN_CLOSED:
                break
        for _ in range(message_queue.qsize()):
            m = message_queue.get()
            if m is True:
                sg.popup("成功", "转换完成\n请查看output.docx文件")
            elif m is False:
                sg.popup_error("错误", "转换失败")
        if (RUNNING is False) and (main_window["-start-"].get_text() == "转换中"):
            main_window["-start-"].update(text="开始转换", disabled=False)
        elif (RUNNING is True) and (main_window["-start-"].get_text() == "开始转换"):
            main_window["-start-"].update(text="转换中", disabled=True)
        if event == "-start-":
            if not window["-file_path-"].get():
                sg.popup_error("错误", "请先选择文件")
            elif not window["-file_path-"].get().lower().endswith(".pdf"):
                sg.popup_error("错误", "请选择pdf文件")
            else:
                Thread(target=parse, args=(window["-file_path-"].get(),), daemon=True).start()
