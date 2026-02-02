from Curso import Curso

class VideoCourse(Curso):

    def __init__(self, titulo, instructor, precio, clases, length_video):
        super().__init__(titulo, instructor, precio, clases)
        self.length_video = length_video


new_Course = VideoCourse("Python", "p1", 4500, 2, 14)

new_Course.show_details("Python")