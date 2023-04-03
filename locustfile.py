# pip3 install locust

# locust --headless -H http://127.0.0.1:8000 -u 100 -r 5 --run-time 60 --csv=example --headless -t10m

from locust import HttpUser, task, FastHttpUser

class HelloWorldUser(FastHttpUser):
    # @task
    # def welcome(self):
    #     self.client.get("/")

    @task
    def infer_ulca_or(self):
        with self.client.post("/infer_ulca_or", 
            json={
                "config": {
                    "language":{
                    "sourceLanguage": "or"
                    },
                    "transcriptionFormat": {"value":"transcript"},
                    "audioFormat": "wav"
                },
                "audio": [{
                    "audioUri": "https://github.com/djgupta/flat_files/raw/main/odiya_test.wav"
                }]
            }, 
            catch_response=True) as response:
            try:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(response.text)
            except Exception as e:
                response.failure(e)
    
#locust --headless -H http://127.0.0.1:8000 -u 10 -r 2 --run-time 180 --csv=t5