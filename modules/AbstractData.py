#!/usr/bin/env python
""" HIAS AI Model Data Abstract Class.

Provides the HIAS AI Model with the required required data
processing functionality.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files(the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Contributors:
- Adam Milton-Barker - First version - 2021-5-1

"""

from abc import ABC, abstractmethod

class AbstractData(ABC):
	""" HIAS AI Model Data Abstract Class.

	Provides the HIAS AI Model with the required required data
	processing functionality.
	"""

	def __init__(self, helpers):
		"Initializes the AbstractData object."
		super().__init__()

		self.helpers = helpers
		self.confs = self.helpers.confs

		self.seed = self.Helpers.confs["data"]["seed"]
		self.dim = self.Helpers.confs["data"]["dim"]

		seed(self.seed)
		random.seed(self.seed)

		self.data = []
		self.labels = []

		self.helpers.logger.info("Data class initialization complete.")

	@abstractmethod
	def pre_process_data(self, img):
		""" Processes the image. """
		pass

	@abstractmethod
	def encode_labels(self):
		""" One Hot Encodes the labels. """
		pass

	@abstractmethod
	def convert_data(self):
		""" Converts the training data to a numpy array. """
		pass

	@abstractmethod
	def shuffle(self):
		""" Shuffles the data and labels. """
		pass

	@abstractmethod
	def get_split(self):
		""" Splits the data and labels creating training and validation datasets. """
		pass

	@abstractmethod
	def reshape(self, img):
		""" Processes the image. """
		pass