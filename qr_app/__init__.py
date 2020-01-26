# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __init__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zytrams <zytrams@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 20:39:00 by zytrams           #+#    #+#              #
#    Updated: 2020/01/05 01:07:34 by zytrams          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask
import os

qr_app = Flask(__name__)

from qr_app import qr_routes

if __name__ == "__main__":
	if 'QR_URL' in os.environ:
		if 'QR_PORT' in os.environ:
			qr_app.run(os.environ['QR_URL'], port=os.environ['QR_PORT'])
		else:
			qr_app.run(os.environ['QR_URL'], port=8081)
	else:
		if 'URL' in os.environ:
			if 'PORT' in os.environ:
				qr_app.run(os.environ['URL'], port=(int(os.environ['PORT']) + 1))
			else:
				qr_app.run(os.environ['URL'], port=8081)
		else:
			qr_app.run('0.0.0.0')
