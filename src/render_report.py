import json

# قراءة النتائج
with open("assets/metrics.json") as f:
    data = json.load(f)

accuracy = data["accuracy"]

# إنشاء صفحة HTML
html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>ML Report</title>
</head>
<body>
    <h1>Model Report</h1>
    <p>Accuracy: {accuracy}</p>
</body>
</html>
"""

# حفظ التقرير
with open("docs/index.html", "w") as f:
    f.write(html)

print("Report generated")