from PIL import Image, ImageDraw
from child import Child

class RewardChart:
    def __init__(self, child, cell_size):
        self.child = child

        self.cols = self.child.major_reward
        self.rows = self.child.records_max // self.child.major_reward
        self.cell_size = cell_size
        self.sticker = Image.open('smile.png').resize((80,80))

    def draw_canvas(self):

        width = int(self.cols * self.cell_size)
        height = int(self.rows * self.cell_size)

        canvas = Image.new("RGBA", (width, height), (255, 255, 255, 255))
        draw = ImageDraw.Draw(canvas)

        for col in range(self.cols + 1):
            x = col * self.cell_size
            draw.line([(x, 0), (x, height)], fill="black", width=2)

        for row in range(self.rows + 1):
            y = row * self.cell_size
            draw.line([(0, y), (width, y)], fill="black", width=2)

        for index, has_reward in enumerate(self.child.records):
            if has_reward and index < self.child.records_current:
                row = index // self.child.major_reward
                col = index % self.child.major_reward

                x = col * self.cell_size + 10
                y = row * self.cell_size + 10

                canvas.paste(self.sticker, (x, y),  self.sticker)

        canvas.show()
        canvas.save("reward_chart.png")
