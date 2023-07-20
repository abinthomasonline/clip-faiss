from faiss import read_index
from PIL import Image

import clip
import json
import torch


class App:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model, _ = clip.load("ViT-B/32", device=self.device)
        self.model.eval()

        self.index = read_index("static/index.faiss")
        with open("static/image_paths.json") as f:
            self.image_paths = json.load(f)

    def search(self, search_text, results=1):
        text_tokens = clip.tokenize([search_text]).to(self.device)
        with torch.no_grad():
            text_features = self.model.encode_text(text_tokens).float()
        text_features /= text_features.norm(dim=-1, keepdim=True)
        text_features = text_features.cpu().numpy()

        _, indices = self.index.search(text_features, results)
        return [self.image_paths[indices[0][i]] for i in range(results)]

    def run(self):
        while True:
            search_text = input("Search: ")
            if search_text == "exit":
                break
            image_path = self.search(search_text)[0]
            image = Image.open(image_path)
            image.show()


if __name__ == "__main__":
    app = App()
    app.run()
