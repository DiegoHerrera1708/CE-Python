from Curso import Curso

class PdfCourse(Curso):

    def __init__(self, titulo, instructor, precio, clases, pages):
        super().__init__(titulo, instructor, precio, clases)
        self.pages = pages

new_Course = PdfCourse("IA", "p1", 4500, 2, 14)

new_Course.show_details("IA")