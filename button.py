class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image # link ảnh
		self.x_pos = pos[0] # vị trí x
		self.y_pos = pos[1] # vị trí y
		self.font = font # font chữ
		self.base_color, self.hovering_color = base_color, hovering_color # màu mặc định || màu khi di chuột vào
		self.text_input = text_input # Nội dung
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen): # cập nhật
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position): # Kiểm tra vị trí chuột
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position): # Đổi màu
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)