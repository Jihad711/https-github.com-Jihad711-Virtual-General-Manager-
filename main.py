from flask import Flask, request, jsonify
from tasks.task_manager import TaskManager
from ai_engine.ai_core import AICore

app = Flask(__name__)

# إعداد المكونات
task_manager = TaskManager()
ai_core = AICore()

@app.route('/command', methods=['POST'])
def execute_command():
    data = request.json
    command = data.get("command", "")
    if not command:
        return jsonify({"error": "لم يتم تقديم أمر"}), 400
    
    # تحليل الأمر باستخدام الذكاء الاصطناعي
    task = ai_core.analyze_command(command)
    
    # تنفيذ المهمة
    result = task_manager.execute_task(task)
    
    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(debug=True)
