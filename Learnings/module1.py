from fpdf import FPDF

class PDF_MC_Table(FPDF):
    def __init__(self):
        super().__init__()
        self.widths = []
        self.aligns = []

    def SetWidths(self, w):
        # Set the array of column widths
        self.widths = w

    def SetAligns(self, a):
        # Set the array of column alignments
        self.aligns = a

    def Row(self, data):
        # Calculate the height of the row
        nb = 0
        for i in range(len(data)):
            nb = max(nb, self.NbLines(self.widths[i], data[i]))
        h = 7 * nb
        # Issue a page break first if needed
        self.CheckPageBreak(h)
        # Draw the cells of the row
        for i in range(len(data)):
            w = self.widths[i]
            a = self.aligns[i] if i < len(self.aligns) else 'L'
            # Save the current position
            x = self.get_x()
            y = self.get_y()
            # Draw the border
            self.rect(x, y, w, h)
            # Print the text
            self.multi_cell(w, 5, data[i], 0, a)
            # Put the position to the right of the cell
            self.set_xy(x + w, y)
        # Go to the next line
        self.ln(h)

    def CheckPageBreak(self, h):
        # If the height h would cause an overflow, add a new page immediately
        if self.get_y() + h > self.page_break_trigger:
            self.add_page(self.cur_orientation)

    def NbLines(self, w, txt):
        # Compute the number of lines a MultiCell of width w will take
        if not self.current_font:
            self.error('No font has been set')
        cw = self.current_font['cw']
        if w == 0:
            w = self.w - self.r_margin - self.x
        wmax = (w - 2 * self.c_margin) * 1000 / self.font_size
        s = str(txt).replace("\r", "")
        nb = len(s)
        if nb > 0 and s[nb - 1] == "\n":
            nb -= 1
        sep = -1
        i = 0
        j = 0
        l = 0
        nl = 1
        while i < nb:
            c = s[i]
            if c == "\n":
                i += 1
                sep = -1
                j = i
                l = 0
                nl += 1
                continue
            if c == ' ':
                sep = i
            l += cw[c]
            if l > wmax:
                if sep == -1:
                    if i == j:
                        i += 1
                else:
                    i = sep + 1
                sep = -1
                j = i
                l = 0
                nl += 1
            else:
                i += 1
        return nl
