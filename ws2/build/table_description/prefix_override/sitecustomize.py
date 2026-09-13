import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/osboxes/ece569-fall2026/ECE569-Lab2/ws2/install/table_description'
