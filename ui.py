import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests


# initialize the root
root = tk.Tk()
root.title("Mind Body Health")
root.geometry("600x600")
root.minsize(600, 600)
root.maxsize(600,600)

# header for all pages contained in root
header_frame = tk.Frame(root)
header_frame.pack(fill='x')

header_label = ttk.Label(header_frame, text="Mind Body Health", font=('Lato', 40))
header_label.pack(padx=15, pady=15)


# notebook widget contained in root
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)








# homepage
home_frame = ttk.Frame(notebook)

notebook.add(home_frame, text="Home")
mission_text = "Take control of your life by enhancing your physical and mental health.\n" \
                 "Our all-in-one application has tools to assist you with generating workout ideas, " \
                    "tracking your steps and water intake, and journaling your thoughts."
mission_label = ttk.Label(home_frame, text=mission_text, wraplength=500, font=('Lato', 16))
mission_label.pack(pady=15)

note_text = "* NOTE: Our hydration tool only utilizes the Imperial system. Water intake is tracked by number of cups consumed."
note_label = ttk.Label(home_frame, text =note_text, wraplength=500, font=('Lato', 16))
note_label.pack(pady=15)

tips_text = "* Tips: Feel free to navigate to the About tab to learn more about the tools or just dive right in!"
tips_label = ttk.Label(home_frame, text = tips_text, wraplength=500, font=('Lato', 16))
tips_label.pack()








# about 
about_frame = ttk.Frame(notebook)
notebook.add(about_frame, text="About")

workout_about_text = "Workout Ideas: Let us help you plan your next workout! No need to waste time trying to come up with an idea yourself. Just click the generate button and an exercise idea will appear on your screen."
workout_about_label = ttk.Label(about_frame, text = workout_about_text, wraplength=500, font = ('Lato', 16))
workout_about_label.pack(pady=15)

hydration_about_text = "Hydration: You need 6-8 cups of water daily to maintain your health. Let us help you keep track. You can adjust your water intake with the arrows on the screen or enter it manually!"
hydration_about_label = ttk.Label(about_frame, text = hydration_about_text, wraplength=500, font=('Lato', 16))
hydration_about_label.pack(pady=15)

memos_about_text = "Memos: Journaling is a great way to reflect on your day and relax. Our memo tool allows you to enter and delete memos as you please."
memos_about_label = ttk.Label(about_frame, text = memos_about_text, wraplength=500, font=('Lato', 16))
memos_about_label.pack()








# workout 
# function to get a workout
def get_workout():
    response = requests.get('http://127.0.0.1:5003/workout')
    data = response.json()
    workout_label.config(text= f"Your workout today: {data}")

workout_frame = ttk.Frame(notebook)
notebook.add(workout_frame, text="Workout Ideas")

generate_label = ttk.Label(workout_frame, text="Click the Generate button below and a workout idea will appear on your screen.",  wraplength=500, font=('Lato', 16))
generate_label.pack(padx = 15, pady = 15)
generate_button = ttk.Button(workout_frame, text="Generate", command=get_workout)
generate_button.pack(padx=15, pady=15)

# creates a label to dynamically display the workout generated 
workout_label = ttk.Label(workout_frame, text="", font=('Lato', 16))
workout_label.pack(padx=15, pady=15)










# steps
step_frame = ttk.Frame(notebook)
step_frame.grid(row = 0, column = 0)
step_frame.columnconfigure([0, 1,2,3], weight=1)  
step_frame.rowconfigure(0, weight=0)
notebook.add(step_frame, text="Steps")

step_info_text = "How to adjust your steps: \n"\
                        "Manually enter the amount in the box and click Confirm. \n"\
                        "\n"\
                        "Click Reset to set the number of steps to 0."
step_about_label = ttk.Label(step_frame, text = step_info_text, font=('Lato', 16))
step_about_label.grid(row=0, column=0, columnspan=3, pady=15)

step_label = ttk.Label(step_frame, text="Current steps: 0 steps", font=('Lato', 18))
step_label.grid(row=1, column=0, columnspan = 3, pady=(0, 15))

def step_edit():
    manual_entry = step_entry.get()
    response = requests.post('http://127.0.0.1:5002/step/edit', json=(manual_entry))
    data = response.json()
    step_label.config(text=f"Current steps: {data} steps")
    step_entry.delete(0, tk.END)

def reset():
    response = requests.post('http://127.0.0.1:5002/step/reset')
    data = response.json()
    step_label.config(text=f"Current steps: {data} steps")
    step_entry.delete(0, tk.END)


step_entry_label = ttk.Label(step_frame, text="Enter Steps:", font=('Lato', 16))
step_entry_label.grid(row=4, column=0)

step_entry = ttk.Entry(step_frame, width=10)
step_entry.grid(row=4, column=1)

confirm_button = ttk.Button(step_frame, text="Confirm", command=step_edit)
confirm_button.grid(row=4, column=2)

step_reset_button = ttk.Button(step_frame, text="Reset", command=reset)
step_reset_button.grid(row=5, column=0,columnspan = 3, pady = (30,0))












# hydration
# function to display water intake 

# global water variable 
hydration_frame = ttk.Frame(notebook)
hydration_frame.grid(row = 0, column = 0)
hydration_frame.columnconfigure([0, 1,2,3], weight=1)  
hydration_frame.rowconfigure(0, weight=0)
notebook.add(hydration_frame, text="Hydration")

hydration_info_text = "There are two ways to adjust your water intake: \n"\
                        "1) Use the arrow to increment and decrement as needed. \n"\
                        "2) Manually enter the amount in the box and click Confirm. \n"\
                        "\n"\
                        "Click Reset to set the number of cups to 0."
hydration_about_label = ttk.Label(hydration_frame, text = hydration_info_text, font=('Lato', 16))
hydration_about_label.grid(row=0, column=0, columnspan=3, pady=15)

water_intake_label = ttk.Label(hydration_frame, text="Current water intake: 0 cups", font=('Lato', 18))
water_intake_label.grid(row=1, column=0, columnspan = 3, pady=(0, 15))

hydration_url = 'http://127.0.0.1:5001/hydration'

def increment_water():
    response = requests.post('http://127.0.0.1:5001/hydration/increment')
    data = response.json()
    water_intake_label.config(text=f"Current water intake: {data} cups")

def decrement_water():
    response = requests.post('http://127.0.0.1:5001/hydration/decrement')
    data = response.json()
    water_intake_label.config(text=f"Current water intake: {data} cups")

def manual_edit():
    manual_entry = water_manual_entry.get()
    response = requests.post('http://127.0.0.1:5001/hydration/manual', json=(manual_entry))
    data = response.json()
    water_intake_label.config(text=f"Current water intake: {data} cups")
    water_manual_entry.delete(0, tk.END)

def reset():
    response = requests.post('http://127.0.0.1:5001/hydration/reset')
    data = response.json()
    water_intake_label.config(text=f"Current water intake: {data} cups")

increment_arrow = ttk.Button(hydration_frame, text="▲", command=increment_water)
increment_arrow.grid(row=2, column=0, pady= (0, 15), columnspan = 3)

decrement_arrow = ttk.Button(hydration_frame, text="▼", command=decrement_water)
decrement_arrow.grid(row=3, column = 0, pady= (0,15),  columnspan = 3)

manual_entry_label = ttk.Label(hydration_frame, text="Enter Manually:", font=('Lato', 16))
manual_entry_label.grid(row=4, column=0)

water_manual_entry = ttk.Entry(hydration_frame, width=10)
water_manual_entry.grid(row=4, column=1)

confirm_button = ttk.Button(hydration_frame, text="Confirm", command=manual_edit)
confirm_button.grid(row=4, column=2)

water_reset_button = ttk.Button(hydration_frame, text="Reset", command=reset)
water_reset_button.grid(row=5, column=0,columnspan = 3, pady = (30,0))








# memos

# function to get memos 
def get_memos():
    # clear existing memos to prevent duplicates
    memo_listbox.delete(0, tk.END)
    response = requests.get('http://127.0.0.1:5000/memo/list')
    data = response.json()
    for memo in data:
        memo_listbox.insert(tk.END, memo)
    memo_entry.delete(0, tk.END)
# function to add a memo 
def add_memo():
    user_input = memo_entry.get()
    if user_input:
        requests.post('http://127.0.0.1:5000/memo/add', json={'memo': user_input})
        get_memos()

# Function to delete a memo
def delete_memo():
    selected_memo = memo_listbox.curselection()
    if selected_memo:
        warning = messagebox.askyesno("Delete Memo", "Warning!\n" "Are you sure you want to delete this memo?")
        if warning:
            requests.post('http://127.0.0.1:5000/memo/delete', json={'memo': selected_memo[0]})
            get_memos()

memo_frame = ttk.Frame(notebook)
notebook.add(memo_frame, text="Memos")

memo_info_text = "Enter a memo in the text box below and click Confirm to add it to the list \n"\
                    "To delete a memo from the list, select the memo from the box and click Delete Selected Memo."
memo_info_label = ttk.Label(memo_frame, text = memo_info_text, wraplength= 500, font=('Lato', 16))
memo_info_label.grid(row = 0, pady=15)

memo_entry = ttk.Entry(memo_frame, width=40)
memo_entry.grid(row=1, pady =(0,15))

add_button = ttk.Button(memo_frame, text="Add Memo", command=add_memo)
add_button.grid(row=2, pady =(0,15))

memo_listbox = tk.Listbox(memo_frame,  width=50, height = 8)
memo_listbox.grid(row=3, pady =(0,15))

delete_button = ttk.Button(memo_frame, text="Delete Selected Memo", command=delete_memo)
delete_button.grid(row=4, pady =(0,15))

memo_frame.grid_columnconfigure(0, weight=1)

root.mainloop()
