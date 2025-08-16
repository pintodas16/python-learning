from pathlib import Path
file_path = Path(__file__).parent / 'one.txt'

# if file_path.exists():
#     print('file found')
# else:
#     file_path.write_text('Hello world!')
#     print('file created')

file = open (file_path,'r')
content = file.read()
for line in content:
    print(line.strip())