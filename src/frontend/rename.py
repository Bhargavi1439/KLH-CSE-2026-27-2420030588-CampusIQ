import os

src_dir = r'c:\Users\krish\.gemini\antigravity-ide\scratch\CampusIQ\frontend\src'

replacements = {
    'EduFusion <span className="text-gradient">AI</span>': 'Campus<span className="text-gradient">IQ</span>',
    'EduFusion AI': 'CampusIQ',
    'EduFusion Portal': 'CampusIQ Portal',
    'EduFusion LangGraph': 'CampusIQ LangGraph',
    'john@edufusion.edu': 'john@campusiq.edu',
    '@edufusion.com': '@campusiq.com',
    'EduFusion': 'CampusIQ'
}

for root, _, files in os.walk(src_dir):
    for file in files:
        if file.endswith('.jsx') or file.endswith('.js') or file.endswith('.css'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            for old, new in replacements.items():
                new_content = new_content.replace(old, new)
                
            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
