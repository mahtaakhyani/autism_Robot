class DataClassify():
    def __init__(self,name):
        try:
            self.f = open(name,'a')
        except FileNotFoundError:
            return "File Not Found. Created a new file named %s"%name
        except PermissionError:
            i = input('Permission denied. Please close the file and hit K key to continue.')
            if lower(i)=='k': self.f = open(name,'a')

        self.name = name

    def text(self,data):
        self.f.writelines(data)

    def json(self,data):
        pass

    def sheet(self,data,headers,columns,sheet_name='main',if_sheet_exists='replace'):
        import pandas as pd
        df = pd.DataFrame(data, columns)
        df.reset_index()
        print(data)
        with pd.ExcelWriter(self.name,
                    mode='a',if_sheet_exists=if_sheet_exists) as writer:  # doctest: +SKIP
                df.to_excel(writer,header=headers, sheet_name=sheet_name)