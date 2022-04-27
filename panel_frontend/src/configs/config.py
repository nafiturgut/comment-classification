import os


class AppConfig:
    NAT_LINKEDIN = "https://www.linkedin.com/in/nafi-ahmet-turgut-1903/"
    MODEL_PATH = "./models/tensor_model_with_training.pth"
    API_URL = os.environ.get("API_URL", "http://localhost:5000/api")
