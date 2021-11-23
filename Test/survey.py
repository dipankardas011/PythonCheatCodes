class Survey:
  def __init__(self, q) -> None:
    self.question = q
    self.response = []

  def show_question(self):
    print(self.question)

  def store_response(self, new):
    self.response.append(new)

  def display(self):
    print("Survey res")

    for r in self.response:
      print(f"- {r}")