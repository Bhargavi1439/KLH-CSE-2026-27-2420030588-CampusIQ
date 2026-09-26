import os
import re
import json
import uuid

def parse_java_controller(filepath):
    endpoints = []
    class_request_mapping = ""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # Find class level RequestMapping
        class_mapping_match = re.search(r'@RequestMapping\s*\(\s*(?:value\s*=\s*)?["\']([^"\']+)["\']\s*\)', content)
        if class_mapping_match:
            class_request_mapping = class_mapping_match.group(1)
            if not class_request_mapping.startswith('/'):
                class_request_mapping = '/' + class_request_mapping
            if class_request_mapping.endswith('/'):
                class_request_mapping = class_request_mapping[:-1]

        # Find all method level mappings
        mapping_patterns = [
            (r'@GetMapping\s*\(\s*(?:value\s*=\s*)?["\']([^"\']*)["\']\s*\)', 'GET'),
            (r'@GetMapping', 'GET'),
            (r'@PostMapping\s*\(\s*(?:value\s*=\s*)?["\']([^"\']*)["\']\s*\)', 'POST'),
            (r'@PostMapping', 'POST'),
            (r'@PutMapping\s*\(\s*(?:value\s*=\s*)?["\']([^"\']*)["\']\s*\)', 'PUT'),
            (r'@PutMapping', 'PUT'),
            (r'@DeleteMapping\s*\(\s*(?:value\s*=\s*)?["\']([^"\']*)["\']\s*\)', 'DELETE'),
            (r'@DeleteMapping', 'DELETE'),
        ]
        
        # We need a more robust way to parse methods, but a simple regex might suffice if we look line by line
        lines = content.split('\n')
        for i, line in enumerate(lines):
            for pattern, method in mapping_patterns:
                match = re.search(pattern, line)
                if match:
                    path = ""
                    if len(match.groups()) > 0:
                        path = match.group(1)
                        if not path.startswith('/') and path != "":
                            path = '/' + path
                    
                    full_path = class_request_mapping + path
                    
                    # Extract query parameters or path variables (simple heuristic)
                    variables = re.findall(r'\{([^}]+)\}', full_path)
                    
                    endpoints.append({
                        'method': method,
                        'path': full_path,
                        'name': f"{method} {full_path}"
                    })
                    break # Only match one mapping per line
                    
    return endpoints

def generate_postman_collection(backend_dir):
    collection = {
        "info": {
            "_postman_id": str(uuid.uuid4()),
            "name": "CampusIQ Services",
            "description": "Generated Postman Collection for CampusIQ Backend Services",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "item": [],
        "variable": [
            {
                "key": "base_url",
                "value": "http://localhost:8080",
                "type": "string"
            }
        ]
    }
    
    # Iterate over directories
    for service_dir in os.listdir(backend_dir):
        full_service_path = os.path.join(backend_dir, service_dir)
        if os.path.isdir(full_service_path) and service_dir.endswith('-service'):
            service_item = {
                "name": service_dir,
                "item": []
            }
            
            src_dir = os.path.join(full_service_path, 'src', 'main', 'java')
            if os.path.exists(src_dir):
                for root, _, files in os.walk(src_dir):
                    for file in files:
                        if file.endswith('Controller.java'):
                            endpoints = parse_java_controller(os.path.join(root, file))
                            if endpoints:
                                for ep in endpoints:
                                    # Handle path variables for postman
                                    path_parts = [p.replace('{', ':').replace('}', '') for p in ep['path'].strip('/').split('/') if p]
                                    
                                    request_item = {
                                        "name": ep['name'],
                                        "request": {
                                            "method": ep['method'],
                                            "header": [],
                                            "url": {
                                                "raw": "{{base_url}}/" + "/".join(path_parts),
                                                "host": [
                                                    "{{base_url}}"
                                                ],
                                                "path": path_parts
                                            }
                                        },
                                        "response": []
                                    }
                                    
                                    if ep['method'] in ['POST', 'PUT']:
                                        request_item['request']['body'] = {
                                            "mode": "raw",
                                            "raw": "{}",
                                            "options": {
                                                "raw": {
                                                    "language": "json"
                                                }
                                            }
                                        }
                                        
                                    service_item['item'].append(request_item)
            
            if len(service_item['item']) > 0:
                collection['item'].append(service_item)
                
    return collection

if __name__ == "__main__":
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    collection = generate_postman_collection(backend_dir)
    
    output_file = os.path.join(backend_dir, 'CampusIQ_Postman_Collection.json')
    with open(output_file, 'w') as f:
        json.dump(collection, f, indent=4)
        
    print(f"Postman collection generated successfully at {output_file}")
