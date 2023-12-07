class LikingSystem:
    likes = []
    dislikes = []

    def __init__(self, data_set):
        self.data_set = data_set

    def like(self, idx):
        item = self.data_set.get_item(idx)
        self.likes.append(item)

    def dislike(self, idx):
        item = self.data_set.get_item(idx)
        self.dislikes.append(item)

    def get_likes(self):
        return self.likes

    def get_dislikes(self):
        return self.dislikes


