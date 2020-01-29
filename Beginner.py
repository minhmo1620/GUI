import tkinter as tk 

HEIGHT = 700
WIDTH = 800
root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='three_bear.png')
background_label = tk.Label(root, image = background_image)
background_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)

frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
frame.place( relx = 0.5, rely = 0.1 ,relwidth = 0.75, relheight = 0.1, anchor = 'n')

entry = tk.Entry(frame, font = 40)
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "Get Weather", font = 40)
button.place(relx = 0.7, relheight = 1, relwidth = 0.3 )

lower_frame = tk.Frame(root, bg = '#80c1ff', bd  = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relheight = 0.75, relwidth = 0.6, anchor = 'n')

# label = tk.Label(frame, text = "This is a label", bg = 'yellow')
# label.pack(side = 'right')

# entry = tk.Entry(frame, bg = 'green')
# entry.pack()

root.mainloop()