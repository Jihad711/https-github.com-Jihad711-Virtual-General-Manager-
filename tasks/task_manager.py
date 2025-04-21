class TaskManager:
    def __init__(self):
        self.tasks = []

    def execute_task(self, task):
        if task == "تحية":
            return "مرحباً! كيف يمكنني مساعدتك؟"
        elif task == "حالة النظام":
            return "النظام يعمل بشكل جيد."
        else:
            return f"المهمة '{task}' غير معروفة."
