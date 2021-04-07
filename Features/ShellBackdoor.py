from Features.base import FeatureBase


class Feature(FeatureBase):
    def __init__(self):
        super().__init__(
            name="Shell Backdoor",
            description="This is will open a shell for the specified backdoor.",
            options=[
                {
                    "message": "Target IP: ",
                    "type": "input",
                    "name": 'target'
                }
            ]
        )

    def function(self, options):
        print("Coming Soon")
        input('Press any key to return to main screen.')