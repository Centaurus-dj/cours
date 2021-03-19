#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### Class ?
### Module method ?
import csv

class csvReader:
    def __init__(self, file: str, delimiter: str):
        self.file = file

        try:
            open(self.file, "tr").close()
            open(self.file, "ta").close()
            open(self.file, "br").close()
            open(self.file, "ba").close()
        except:
            raise Exception(f"File: {self.file} didn't passed the file checkup, please look if file is not corrupted.")

        with open(self.file) as file:
            self.open_file = csv.reader(file, delimiter=delimiter)
            l = list()
            for row in self.open_file:
                l.append(row)
        self.render_file = l

    def get(self):
        return self.render_file
