import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("Machine Learning GUI")

# دالة لتحميل البيانات
def load_data():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            data = pd.read_csv(file_path)
            messagebox.showinfo("Success", "Data loaded successfully!")
            update_feature_list(data.columns)  # تحديث قائمة الأعمدة المتاحة
            return data
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")
    return None

# دالة لتحديث قائمة الأعمدة
def update_feature_list(columns):
    feature_listbox.delete(0, tk.END)  # مسح العناصر القديمة
    for col in columns:
        feature_listbox.insert(tk.END, col)

# دالة لتدريب النموذج
def train_model():
    global data
    if data is None:
        messagebox.showerror("Error", "No data loaded!")
        return
    
    try:
        # الحصول على الأعمدة المختارة من المستخدم
        selected_features = [feature_listbox.get(i) for i in feature_listbox.curselection()]
        if not selected_features:
            messagebox.showerror("Error", "No features selected!")
            return

        X = data[selected_features]
        y = data[target_column.get()]  # الحصول على عمود الهدف المختار

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        
        messagebox.showinfo("Model Trained", f"Model trained successfully! Accuracy: {accuracy:.2f}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to train model: {e}")

# دالة لتحميل البيانات
data = None
def load_data_action():
    global data
    data = load_data()

# واجهة المستخدم

# حقل إدخال لاسم عمود الهدف
target_column = tk.StringVar()
target_entry = tk.Entry(root, textvariable=target_column)
target_entry.pack(pady=10)
target_entry.insert(0, "Enter target column name")

# قائمة لعرض الأعمدة المتاحة للاختيار
feature_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=10, width=50)
feature_listbox.pack(pady=10)

# زر لتحميل البيانات
load_data_button = tk.Button(root, text="Load Data", command=load_data_action)
load_data_button.pack(pady=10)

# زر لتدريب النموذج
train_model_button = tk.Button(root, text="Train Model", command=train_model)
train_model_button.pack(pady=10)

# تشغيل التطبيق
root.mainloop()
