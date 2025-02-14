import queue
import threading
import tkinter as tk

from clean_python.session1.functions.genetic_tsp_dirty.genTSP import GeneticTSPSolver, TspData

def plot_point(canvas, width, height, x, y):
    canvas_x = width // 2 + x
    canvas_y = height // 2 - y
    canvas.create_oval(canvas_x - 3, canvas_y - 3, canvas_x + 3, canvas_y + 3, fill="blue", outline="blue")


def draw_line(canvas, width, height, x1, y1, x2, y2):
    canvas_x1 = width // 2 + x1
    canvas_y1 = height // 2 - y1
    canvas_x2 = width // 2 + x2
    canvas_y2 = height // 2 - y2

    canvas.create_line(canvas_x1, canvas_y1, canvas_x2, canvas_y2, fill="red")

def update_plane_left(points, lines):
    left_canvas.delete("all")

    for x, y in points:
        plot_point(left_canvas, plane_width, plane_height, x, y)

    for city1, city2 in lines:
        draw_line(left_canvas, plane_width, plane_height, *city1, *city2)

def update_plane_right(points, lines):
    right_canvas.delete("all")

    for x, y in points:
        plot_point(right_canvas, plane_width, plane_height, x, y)

    for city1, city2 in lines:
        draw_line(right_canvas, plane_width, plane_height, *city1, *city2)


def update_plane(pipe):
    if not pipe.empty():
       update_plane_right(*pipe.get())
    root.after(100, update_plane, pipe)



root = tk.Tk()
root.title("TSP genetic solver")
plane_height = plane_width = 600
left_canvas = tk.Canvas(root, width=plane_width, height=plane_height, bg="white")
right_canvas = tk.Canvas(root, width=plane_width, height=plane_height, bg="white")
left_canvas.pack(side="left")
right_canvas.pack(side="right")


tsp_data = TspData(plane_width, 50)
genetic_tsp_solver = GeneticTSPSolver(tsp_data)

update_plane_left(tsp_data.cities_coords, genetic_tsp_solver.string_them_up(tsp_data.cities_indices))
update_plane_right(tsp_data.cities_coords, genetic_tsp_solver.string_them_up(tsp_data.cities_indices))


pipe = queue.Queue()


def background_worker(pipe):
    genetic_tsp_solver.run(pipe)


threading.Thread(target=background_worker, args=(pipe,), daemon=True).start()

update_plane(pipe)
root.mainloop()
