from PIL import Image
from child import Child

class RewardChart:
    def __init__(self, child, cell_size):
        self.child = child

        self.rows = self.child.major_reward
        self.cols = self.child.records_max / self.child.major_reward
        self.cell_size = cell_size

        self.width = int(self.cols * self.cell_size)
        self.height = int(self.rows * self.cell_size)

        self.canvas = Image.new("RGBA", (self.width, self.height), (255, 255, 255, 255))

        self.sticker = Image.open('smile.png').resize((80,80))

    def draw_canvas(self):
        
        for index, has_reward in enumerate(self.child.records):
            if has_reward and index < self.child.records_current:
                row = index // self.child.major_reward
                col = index % self.child.major_reward

                x = col * self.cell_size + 10
                y = row * self.cell_size + 10

                self.canvas.paste(self.sticker, (x, y),  self.sticker)

        self.canvas.show()
        self.canvas.save("reward_chart.png")

    

child = Child.LoadChildFromFile('Jackson')
chart = RewardChart(child, 100)

chart.draw_canvas()