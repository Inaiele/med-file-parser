import re
import pandas as pd


def save_parse_result_to_xlsx(path, input : list, columns : list):
    df = pd.DataFrame(input, columns=columns)
    datatoexcel = pd.ExcelWriter(path)
    df.to_excel(datatoexcel)
    datatoexcel.close()


class Parser:
    def __init__(self, path) -> None:
        self.path = path

    def __get_lines(self) -> list:
        lines = []
        with open(self.path, 'r', encoding='utf-8') as file:
            for line in file:
                if line:
                    if re.match(r'[ \t]+', line):
                        lines[-1] += line.strip()
                    else:
                        lines.append(line.rstrip('\n'))
        return lines


    def parse(self) -> list:
        temp_res = {}
        pmid = -1

        for line in self.__get_lines():
            sline = re.match(r'([A-Z]{2,4})\s{0,4}[-]\s{0,4}(.+)', line)
            if sline:
                name = sline[1]
                value = sline[2]
                if name == "PMID":
                    pmid = int(value)
                elif name == 'TI':
                    if pmid:
                        if pmid in temp_res:
                            temp_res[pmid]['TI'] = value
                        else:
                            temp_res[pmid] = {'TI' : value}
                elif name == 'AB':
                    if pmid:
                        if pmid in temp_res:
                            temp_res[pmid]['AB'] = value
                        else:
                            temp_res[pmid] = {'AB' : value}

        res = []
        for _, v in temp_res.items():
            line = []
            line.append(v["TI"] if 'TI' in v else "")
            line.append(v["AB"] if 'AB' in v else "")
            res.append(line)
        return res
