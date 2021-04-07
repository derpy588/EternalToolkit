from Features.base import FeatureBase


class Feature(FeatureBase):
    def __init__(self):
        super().__init__(
            name="Backdoor Generator",
            description="This will generate a backdoor for post exploitation.",
            options=[
                {
                    "message": "System: ",
                    "type": "list",
                    "name": 'system',
                    "choices": ["Linux", "Windows", "Mac OSX"]
                },
                {
                    "message": "File Name: ",
                    "type": "input",
                    "name": "file_name"
                }
            ]
        )

    def function(self, options):
        print("Coming Soon")
        input('Press any key to return to main screen.')