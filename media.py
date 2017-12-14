
class Media():
    """this class provides a way to access abstract human-formatted media objects and serves as the root class for more specific human-formatted media types"""
    VALID_EXPERIENCE_VECTORS = ["AURAL","VISUAL","OLFACTORY", "GUSTATORY" "TACTILE"]
    def __init__(self, title, description, representative_image, experience_vectors):
        self.title = title
        self.description = description
        self.representative_image = representative_image
        self.experience_vectors = []
        for experience_vector in experience_vectors:
            if experience_vector in Media.VALID_EXPERIENCE_VECTORS:
                self.experience_vectors.append(experience_vector)
            else:
                self.experience_vectors.append = "INVALID EXPERIENCE VECTOR '" + str(experience_vector) + "' INPUT AT THIS INDEX.  PLEASE CHECK COMPATIBILITY OF VECTOR WITH CURRENT EXISTENTIAL MODALITY"

class Movie(Media):
    """this class provides a convenient way to access media objects commonly considered to be movies"""
    def __init__(self, title, description, representative_image, trailer, genre):
        Media.__init__(self, title, description, representative_image, ["AURAL", "VISUAL"])
        self.trailer = trailer
        self.genre = genre
    def show_attributes(self):
        print(self.title, self.description, self.representative_image, self.experience_vectors, self.trailer, self.genre)

class Show(Media):
    """this class provides a convenient way to access media objects commonly considered to be shows"""
    def __init__(self, title, description, representative_image, seasons, genre):
        Media.__init__(self, title, desription, representative_image, ["AURAL", "VISUAL"])
        self.seasons = seasons
        self.genre = genre
    def show_attributes(self):
        print(self.title, self.description, self.representative_image, self.experience_vectors, self.seasons, self.genre)


hannibal = Movie("hannibal", "a cannibal has fun in italy", "testimage", "testtrailer", "5/5")
hannibal.show_attributes()
