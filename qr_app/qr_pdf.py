# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    qr_pdf.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zytrams <zytrams@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/09 09:51:59 by zytrams           #+#    #+#              #
#    Updated: 2020/01/07 15:52:17 by zytrams          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from fpdf import FPDF
import os

# A class for pdf file creation
class PdfDecorator():
	A4_WIDTH = 210
	A4_HEIGHT = 297

	def __init__(self, pdfname):
		self.pdf = FPDF(unit='pt')
		self.pdf.add_font('DejaVu', '', './font/dejavu-sans-mono.ttf', uni=True)
		self.pdf.set_font("DejaVu", size = 5)
		if pdfname:
			self.pdfname = pdfname
		else:
			self.pdfname = "libqrcodes.pdf"

	def new_page(self):
		self.pdf.add_page()

	def put_label(self, x, y, string):
		while string:
			let_len = 0
			last_space = 0
			while let_len < 30:
				if let_len == len(string):
					last_space = let_len
					break
				if string[let_len] == ' ':
					last_space = let_len
				let_len += 1
			s = string[:last_space]
			self.pdf.text(x, y, s)
			y = y + 5
			string = string[last_space + 1:]

	def put_image(self, x, y, w, h, img):
		img.save('uga.png', 'PNG')
		self.pdf.image('uga.png', x, y, w=w, h=h)
		os.remove('uga.png')

	def save_pdf(self):
		self.pdf.output(self.pdfname)
