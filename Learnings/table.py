from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Table Example', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def add_table(self, data, col_width, row_height):
        self.set_font('Arial', '', 12)
        self.set_fill_color(200)
        self.set_text_color(0)
        self.set_draw_color(0)
        self.set_line_width(0.3)

        for row in data:
            for item in row:
                lines = self.multi_cell(col_width, row_height, item, 1, 'L', fill=True)
                remaining_lines = lines.count('\n')

                # Adjust the row height based on multiline text
                cell_height = row_height * (remaining_lines + 1)
                self.cell(col_width, cell_height, '', 1)

            self.ln(row_height * (remaining_lines + 1))

# Data for the table
table_data = [
    ['Cell 1', 'Cell 2', 'Cell 3', 'Cell 4'],
    ['Multi-line\ntext', 'Another cell', 'Some more text', 'Last cell'],
    ['Long text that spans multiple lines', 'Short cell', 'Text\non multiple\nlines', 'Final cell'],
    ['Cell 5', 'Cell 6', 'Cell 7', 'Cell 8'],
    ['Cell 9', 'Cell 10', 'Cell 11', 'Cell 12'],
    ['Cell 13', 'Cell 14', 'Cell 15', 'Cell 16'],
    ['Cell 17', 'Cell 18', 'Cell 19', 'Cell 20'],
    ['Cell 21', 'Cell 22', 'Cell 23', 'Cell 24'],
    ['Cell 25', 'Cell 26', 'Cell 27', 'Cell 28'],
    ['Cell 29', 'Cell 30', 'Cell 31', 'Cell 32']
]

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Define column width and row height
col_width = 50
row_height = 10

pdf.add_table(table_data, col_width, row_height)
pdf.output('table_example.pdf')
