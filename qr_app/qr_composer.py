# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    qr_composer.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zytrams <zytrams@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/10 09:08:13 by zytrams           #+#    #+#              #
#    Updated: 2019/11/10 12:54:15 by zytrams          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image as I, ImageColor as IC
from qr_image import QrImage


class QrComposer():
	A4_W = 2481
	A4_H = 3508

	def __init__(self, x_times, y_times):
		self.xchunksize = int(self.A4_W / x_times)
		self.ychunksize = int(self.A4_H / y_times)
		self.x_size = x_times
		self.y_size = y_times
		self.xoffset = 0
		self.yoffset = 0
		self.resized_h = int(self.ychunksize / 2)

	def put_qrs(self, qr_list):
		x = 0
		y = 0
		img_id = 0
		a4_img = I.new('RGB', (self.A4_W, self.A4_H), color=IC.getrgb('white'))
		for img in qr_list:
			resized_img = img.img.resize((self.resized_h, self.resized_h))
			a4_img.paste(resized_img,(self.xoffset
			+ int((self.xchunksize - self.resized_h) / 2), self.yoffset))
			x += 1
			self.xoffset += self.xchunksize
			if (x >= self.x_size):
				x = 0
				self.xoffset = 0
				y += 1
				self.yoffset += self.ychunksize
				if (y >= self.y_size):
					y = 0
					self.yoffset = 0
					img_id += 1
					print ('qr_image0' + str(img_id) + '.png')
					QrComposer.save(a4_img, 'qr_image0' + str(img_id) + '.png')
					a4_img = I.new('RGB', (self.A4_W, self.A4_H), color=IC.getrgb('white'))
		img_id += 1
		QrComposer.save(a4_img, 'qr_image0' + str(img_id) + '.png')

	# Static method
	@staticmethod
	def create_image_filled(qr_img, x_times, y_times, A4_W = 2481, A4_H = 3508):
		a4_img = I.new('RGB', (A4_W, A4_H), color=IC.getrgb('white'))
		new_w = int(A4_W / x_times)
		new_h = int(A4_H / y_times)
		resized_img = qr_img.img.resize((new_w, new_h / 2))
		x_offset = 0
		for x in range(0, x_times):
			y_offset = 0
			for y in range (0, y_times):
				a4_img.paste(resized_img, (x_offset, y_offset))
				y_offset += new_h
			x_offset += new_w
		return a4_img

	@staticmethod
	def save(img, fname):
		img.save(fname, 'PNG')

if	__name__ == "__main__":
	qr_composer = QrComposer(8, 8)
	qr1 = QrImage()
	qr2 = QrImage('https://ya.ru')
	l = [qr1, qr2] * 20
	qr_composer.put_qrs(l)
