from data_get import Instance
import tkinter as tk

instance = Instance()

def on_button_clickS(session, frame):
    instance.get_drivers(session)
    for widget in frame.winfo_children():
        widget.destroy()
    select_driver(frame)
    global selectedSession
    selectedSession = session

def on_button_clickD(driver, frame):
    instance.get_laps(driver, selectedSession)
    for widget in frame.winfo_children():
        widget.destroy()
    show_laps(frame)

def select_session(frame):
    for session in instance.sessions:
        button = tk.Button(frame, text=str(session), command=lambda e=session: on_button_clickS(e, frame))
        button.pack(fill='x', padx=5, pady=5)

def select_driver(frame):
    for driver in instance.drivers:
        button = tk.Button(frame, text=str(driver), command=lambda e=driver: on_button_clickD(e, frame))
        button.pack(fill='x', padx=5, pady=5)

def show_laps(frame):
    fastest = tk.Label(frame, text=instance.selectedFastLap)
    fastest.pack(fill='x', padx=5, pady=5)
    for lap in instance.laps:
        text = tk.Label(frame, text=str(lap))
        text.pack(fill='x', padx=5, pady=5)

def create_scrollFrame(root):
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(main_frame)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    return frame

root = tk.Tk()
root.title("F1 Lap Time Analyzer")

frame1 = create_scrollFrame(root)

instance.get_sessions()
select_session(frame1)

root.mainloop()