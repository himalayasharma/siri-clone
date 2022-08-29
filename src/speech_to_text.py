import requests
from api_secrets import ASSEMBLY_AI_API_KEY

class speechToText:

    UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"

    def __init__(self):
        pass
    
    # Read wav file
    def _read_file(self, filename, chunk_size=5242880):

        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    # UPLOAD LOCAL AUDIO TO ASSEMBLY AI
    def upload_audio(self, audio_file_path: str):

        # Specify API key in header for authentication
        headers = {'authorization': ASSEMBLY_AI_API_KEY}
        # Send POST request
        response = requests.post(url=speechToText.UPLOAD_ENDPOINT,
                                headers=headers,
                                data=self._read_file(filename=audio_file_path))
        # Return response in json format
        return response.json()

def main():
    pass

if __name__ == "__main__":
    main()