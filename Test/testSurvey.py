import unittest

from survey import Survey

class testing(unittest.TestCase):
  def setUp(self) -> None:
    question = "what is your tech stack? "
    self.object = Survey(question)
    self.Variable_responses = ['C++', 'C', 'Java', 'Typescript', 'Node js', 'Python']

  def test_sjnfjsdf(self):
    for response in self.Variable_responses:
      self.object.store_response(response)

    for r in self.Variable_responses:
      self.assertIn(r, self.object.response)

if __name__ == '__main__':
  unittest.main()