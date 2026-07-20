from fpdf import FPDF, Align, XPos

class PDF(FPDF):
    
    def header(self):
        self.set_font("Times", size=52)
        self.cell(0,40,"CS50 Shirtificate", border=0, align=Align.C, new_x=XPos.LMARGIN)
   
    def name_on_shirt(self, name):
        self.set_font("Times", size=24)
        self.set_text_color(255,255,255)
        self.cell(0,220,f"{name} took CS50", border=0, align=Align.C, )
   


def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.image("shirtificate.png",x=Align.C ,y=60,w=180,h=180, keep_aspect_ratio=True)
    pdf.set_auto_page_break(auto=False)
    pdf.name_on_shirt(name)
    pdf.output("finished_shirt.pdf")


    
if __name__ == "__main__":
    main()

#recieve user input
#initalize a new pdf with the shirtificate pasting it over an amige
#adding text to shritificate (header / footer?)

#should probably create classes to do this