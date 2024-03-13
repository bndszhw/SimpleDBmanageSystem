import csv
import sys
import os

class SimpleDB:
    def __init__(self):
        self.selected_table = None
        self.tables = {}
        self._load_existing_tables()
        self.read_flag = False
    
    def _load_existing_tables(self):
        for file in os.listdir('.'):  # 检查当前目录下的所有文件
            if file.endswith('.csv'):
                self.tables[file] = self._get_columns(file)

    def _get_columns(self, filename):
        encodings = ['utf-8', 'utf-16', 'GBK', 'ASCII']  # 常见编码列表
        for encoding in encodings:
            try:
                with open(filename, mode='r', newline='', encoding=encoding) as file:
                    reader = csv.reader(file)
                    columns = next(reader, [])  # 读取第一行，即列头
                return columns
            except UnicodeDecodeError:
                continue
        print(f"Error: 文件 {filename} 无法被读取，可能是编码不兼容。")
        return []

    def _ensure_csv_extension(self, filename):
        if not filename.endswith('.csv'):
            return filename + '.csv'
        return filename

    def create_table(self, filename, *columns):
        filename = self._ensure_csv_extension(filename)
        original_filename = filename
        i = 1
        while os.path.exists(filename):
            print(f"Table '{filename}' already exists.")
            filename = f"{original_filename.split('.csv')[0]}({i}).csv"
            i += 1
        self.tables[filename] = list(columns)
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)
        print(f"Table created with name: {filename}")

    def select_table(self, filename):
        filename = self._ensure_csv_extension(filename)
        if filename in self.tables:
            self.selected_table = filename
            print(f"Table '{filename}' is selected.")
            self.view_table_head()
        else:
            print(f"Table '{filename}' does not exist. Please create it first.")
    
        

    # def view_table_head(self):
    #     if not self.selected_table:
    #         print("No table selected. Please select a table first.")
    #         return
    #     print("Table columns:", self.tables[self.selected_table])
    
    def view_table_head(self):
        if not self.selected_table:
            print("No table selected. Please select a table first.")
            return
        columns = self._get_columns(self.selected_table)
        if columns:
            print("Table columns:", columns)
        else:
            print("Unable to retrieve table columns.")

    def input(self, *data):
        if not self.selected_table:
            print("No table selected. Please select a table first.")
            return

        columns = self.tables[self.selected_table]
        if len(data) > len(columns):
            print("Warning: More data provided than columns in the table. Excess data will be ignored.")
            print("Table columns:", columns)
            print("Provided data:", data[:len(columns)])
            data = data[:len(columns)]

        with open(self.selected_table, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
            print("Input successful:", data)
            
    def view_column(self, column_name):
        if not self.selected_table:
            print("No table selected. Please select a table first.")
            return

        unique_elements = set()
        
        encodings = ['utf-8', 'utf-16', 'GBK', 'ASCII']  # 常见编码列表
        for encoding in encodings:
            try:
                with open(self.selected_table, mode='r', newline='', encoding=encoding) as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        unique_elements.add(row[column_name])

                print("Unique elements in column '{}':".format(column_name))
                print(' '.join(unique_elements))
                self.read_flag = True
            except UnicodeDecodeError:
                continue
        if not self.read_flag:
            print(f"Error: 文件无法被读取，可能是编码不兼容。")
        else:
            self.read_flag = False
        return []
        
        


        
    def output_table(self):
        if not self.selected_table:
            print("No table selected. Please select a table first.")
            return

        filepath = os.path.join(os.getcwd(), self.selected_table)
        if os.path.exists(filepath):
            print(f"Table path: {filepath}")
            # 也可以在这里添加代码以打开并显示CSV文件的内容，例如：
            with open(filepath, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        else:
            print("Selected table does not exist on the filesystem.")

def main():
    db = SimpleDB()
    print("SimpleDB Command Interface. Type 'CTRL+C' to exit.")
    
    while True:
        try:
            command_input = input("Enter command: ").strip().split()
            cmd = command_input[0] if command_input else ''
            
            if cmd == 'create_table':
                filename = command_input[1]
                columns = command_input[2:]
                db.create_table(filename, *columns)
            elif cmd == 'select_table':
                filename = command_input[1]
                db.select_table(filename)
            elif cmd == 'input':
                data = command_input[1:]
                db.input(*data)
            elif cmd == 'view_table_head':
                db.view_table_head()
            elif cmd == 'output_table':
                db.output_table()
            elif cmd == 'view_column':
                data = command_input[1:]
                db.view_column(*data)
            elif cmd == '':
                continue  # Handle empty input
            else:
                print("Unknown command.")
        except KeyboardInterrupt:
            print("\nExiting program.")
            break
        except UnicodeDecodeError as e:
            print("Encoding error: ", e)
        except FileNotFoundError as e:
            print("File not found: ", e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
if __name__ == "__main__":
    main()

