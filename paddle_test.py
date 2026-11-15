from paddleocr import PaddleOCRVL

pipeline = PaddleOCRVL(pipeline_version="v1.6")
output = pipeline.predict("document_image.png")
for res in output:
  res.print()
  res.save_to_json(save_path="output")
  res.save_to_markdown(save_path="output")
