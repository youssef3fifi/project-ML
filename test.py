import pickle
from tkinter import filedialog
#import playfair
import customtkinter
#import self


frames = {}

def show_page(page_num):
    # Hide all frames
    for frame in frames.values():
        frame.pack_forget()
    # Show the selected frame
    frames[page_num].pack(padx=0, pady=60, fill="both", expand=True)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x470")


def select_file():
    # Open a file dialog for the user to select the file to add
    filename = filedialog.askopenfilename(title="Select file to add")
    # Check if a file was selected
    if filename:
        try:
            # Open the selected file for reading
            with open(filename, "r") as file:
                # Read the content of the file
                file_content = file.read()

            # Perform edits on the file content (for example, convert to uppercase)
            edited_content = file_content.upper()
            return file_content
            # Specify the path for the new file with edited content
            edited_filename = "edited_file.txt"

            # Write the edited content to the new file
            with open(edited_filename, "w") as edited_file:
                edited_file.write(edited_content)
            # Print a message indicating the successful creation of the edited file
            print("Edited file created successfully:", edited_filename)
        except Exception as e:
            # Print an error message if any exception occurs
            print("Error:", e)
# ---------------------------------------------------------------------------------------------------------------------#
home_frame = customtkinter.CTkFrame(master=root)
home_frame.pack(padx=0, pady=60, fill="both", expand=True)
frames["home"] = home_frame

label = customtkinter.CTkLabel(master=home_frame, text="Home Page", font=("Helvetica", 25))
label.grid(row=0, column=1)

# صفحه ال ceaser
frame2 = customtkinter.CTkFrame(master=root)

frames["Lodistic redrission"] = frame2
#
# صفحه الtransposition
frame3 = customtkinter.CTkFrame(master=root)
frames["DecisionTree"] = frame3

# صفحه الrote 13
frame4 = customtkinter.CTkFrame(master=root)
frames["RandomForest"] = frame4

# صفحه ال playfair
frame5 = customtkinter.CTkFrame(master=root)
frames["NN"] = frame5

# صفحه ال railfence
frame6 = customtkinter.CTkFrame(master=root)
frames["SVM"] = frame6

# صفحه ال substitution
frame7 = customtkinter.CTkFrame(master=root)
frames["GradientBoosting"] = frame7

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

button1 = customtkinter.CTkButton(master=home_frame, text="Lodistic redrission", font=("Helvetica", 15),
                                  command=lambda: show_page("Lodistic redrission"))
button1.grid(row=1, column=0, padx=10, pady=30)

button2 = customtkinter.CTkButton(master=home_frame, text="DecisionTree", font=("Helvetica", 15),
                                  command=lambda: show_page("DecisionTree"))
button2.grid(row=1, column=1, padx=10, pady=10)

button3 = customtkinter.CTkButton(master=home_frame, text="RandomForest", font=("Helvetica", 15),
                                  command=lambda: show_page("RandomForest"))
button3.grid(row=1, column=2, padx=10, pady=10)

button4 = customtkinter.CTkButton(master=home_frame, text="NN", font=("Helvetica", 15),
                                  command=lambda: show_page("NN"))
button4.grid(row=2, column=0, padx=10, pady=30)

button5 = customtkinter.CTkButton(master=home_frame, text="SVM", font=("Helvetica", 15),
                                  command=lambda: show_page("SVM"))
button5.grid(row=2, column=1, padx=10, pady=10)

button6 = customtkinter.CTkButton(master=home_frame, text="GradientBoosting", font=("Helvetica", 15),
                                  command=lambda: show_page("GradientBoosting"))
button6.grid(row=2, column=2, padx=10, pady=10)
# ---------------------------------------------------------------------------------------------------------------------#

# ceaser page components###############################################################################################


# transpotion page components###########################################################################################

# rote 13 page components###############################################################################################
# Sample list of doctor names

# Your original code setup
label4 = customtkinter.CTkLabel(master=frame4, text="RandomForest Page", font=("Helvetica", 25))
label4.grid(row=0, column=1, padx=10, pady=10)

button_file3 = customtkinter.CTkButton(master=frame4, text="Select file", font=("Helvetica", 15), command=select_file)
button_file3.grid(row=1, column=0, padx=10, pady=10)

file_input3 = customtkinter.CTkEntry(master=frame4)
file_input3.grid(row=1, column=1, padx=10, pady=10)

fields = ['Age', 'Medical Condition', 'Admission Type', 'Test Results', 'Length of Stay',
          'Admission Day', 'Admission Month', 'Admission Year', 'Discharge Day',
          'Discharge Month', 'Discharge Year']

selected_fields = {}
for idx, field in enumerate(fields):
    label = customtkinter.CTkLabel(master=frame4, text=f"Select {field}", font=("Helvetica", 15))
    label.grid(row=2 + (idx // 3) * 2, column=idx % 3, padx=5, pady=5)

    var = customtkinter.StringVar(value="Choose")

    # Custom options for specific fields
    if field == "Medical Condition":
        options = [str(i) for i in range(0, 4)]
    elif field == "Admission Type":
        options = [str(i) for i in range(0, 2)]
    else:
        options = [str(i) for i in range(1, 101)]  # Example: numbers 1-100 for other fields

    dropdown = customtkinter.CTkOptionMenu(master=frame4, variable=var, values=options)
    dropdown.grid(row=3 + (idx // 3) * 2, column=idx % 3, padx=5, pady=5)

    selected_fields[field] = var

def predict_with_rf():
    # Extract the values from the selected_fields and prepare for prediction
    input_data = [selected_fields[field].get() for field in fields]
    
    with open('RF.pkl', 'rb') as scaler_file:
        mp = pickle.load(scaler_file)
        
    prediction = mp.predict([input_data])
    print("Prediction:", prediction)

# Positioning the Predict button in the last row
predict_button = customtkinter.CTkButton(master=frame4, text="Predict", font=("Helvetica", 15), command=predict_with_rf)
predict_button.grid(row=10, column=1, padx=10, pady=10)

# Positioning the Back to Home Page button in the last row, under the Predict button
back_button = customtkinter.CTkButton(master=frame4, text="Back to Home Page", font=("Helvetica", 15), command=lambda: show_page("home"))
back_button.grid(row=11, column=1, padx=10, pady=10)


# playfair page components#############################################################################################


# railfence page components############################################################################################

# substitution page components##########################################################################################


root.mainloop()